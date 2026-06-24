from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path, PurePosixPath
import re
import shutil
import tempfile
import textwrap
import time
import zipfile


class BuildError(RuntimeError):
    pass


class BuildCancelled(BuildError):
    pass


@dataclass
class BuildResult:
    image_ref: str
    build_log: str
    duration_ms: int


RUNNER_SOURCE = r'''
import importlib
import json
import os
from pathlib import Path
import sys
import traceback


def load_handler(handler_path):
    module_name, _, function_name = handler_path.partition(".")
    if not module_name or not function_name:
        raise ValueError("Handler must use the form module.function")
    module = importlib.import_module(module_name)
    return getattr(module, function_name)


def main():
    event_path_value = os.environ.get("FUNCTION_EVENT_PATH", "")
    event_json = os.environ.get("FUNCTION_EVENT_JSON", "")
    output_dir_value = os.environ.get("FUNCTION_OUTPUT_DIR", "")
    handler_path = os.environ.get("FUNCTION_HANDLER", "handler.main")
    request_id = os.environ.get("FUNCTION_REQUEST_ID", "")

    if event_json:
        event = json.loads(event_json)
    else:
        event = json.loads(Path(event_path_value).read_text(encoding="utf-8"))

    sys.path.insert(0, "/function")
    output_dir = Path(output_dir_value) if output_dir_value else None
    if output_dir is not None:
        output_dir.mkdir(parents=True, exist_ok=True)
    handler = load_handler(handler_path)
    result = handler(event, {"request_id": request_id})

    result_payload = result
    try:
        serialized = json.dumps(result_payload)
    except TypeError:
        result_payload = {"repr": repr(result_payload)}
        serialized = json.dumps(result_payload)

    if output_dir is not None:
        try:
            result_path = output_dir / "result.json"
            result_path.write_text(serialized, encoding="utf-8")
        except Exception:
            pass

    print(f"__FUNCTION_RESULT__={serialized}")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
'''


DOCKERFILE_TEMPLATE = """
FROM {base_image}

ENV PYTHONDONTWRITEBYTECODE=1 \\
    PYTHONUNBUFFERED=1

WORKDIR /function

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /function
COPY .serverless/runner.py /runner.py

ENTRYPOINT ["python", "/runner.py"]
"""


def get_docker_client():
    import docker

    return docker.from_env()


class DockerBuilder:
    def __init__(self, docker_client=None) -> None:
        self.docker_client = docker_client or get_docker_client()

    def build(
        self,
        job: dict,
        source_bundle: Path,
        should_cancel=None,
    ) -> BuildResult:
        image_ref = job.get("image_ref")
        if not image_ref:
            raise BuildError("Build job has no image_ref.")

        started = time.monotonic()
        log_lines = []
        try:
            check_cancelled(should_cancel)
            with tempfile.TemporaryDirectory(prefix="function-build-") as build_root:
                build_path = Path(build_root)
                prepare_build_context(
                    source_bundle,
                    build_path,
                    runtime=job.get("runtime", "python3.13"),
                )
                check_cancelled(should_cancel)
                _, build_logs = self.docker_client.images.build(
                    path=str(build_path),
                    tag=image_ref,
                    rm=True,
                )
                log_lines.extend(format_docker_logs(build_logs))
                check_cancelled(should_cancel)
                push_logs = self.docker_client.images.push(
                    image_ref,
                    stream=True,
                    decode=True,
                )
                for item in push_logs:
                    check_cancelled(should_cancel)
                    log_lines.extend(format_docker_logs([item]))
        except BuildCancelled:
            raise
        except Exception as exc:
            detail = "\n".join(log_lines).strip()
            message = f"Build failed: {exc}"
            if detail:
                message = f"{detail}\n{message}"
            raise BuildError(message) from exc

        duration_ms = int((time.monotonic() - started) * 1000)
        return BuildResult(
            image_ref=image_ref,
            build_log="\n".join(log_lines).strip() or "Build completed.",
            duration_ms=duration_ms,
        )


def check_cancelled(should_cancel) -> None:
    if should_cancel is not None and should_cancel():
        raise BuildCancelled("Build cancelled by user.")


def prepare_build_context(
    source_bundle: Path,
    build_path: Path,
    *,
    runtime: str,
) -> None:
    extract_source_bundle(source_bundle, build_path)
    serverless_dir = build_path / ".serverless"
    serverless_dir.mkdir(exist_ok=True)
    (serverless_dir / "runner.py").write_text(
        textwrap.dedent(RUNNER_SOURCE).strip() + "\n",
        encoding="utf-8",
    )
    dockerfile = DOCKERFILE_TEMPLATE.format(
        base_image=base_image_for_runtime(runtime),
    )
    (build_path / "Dockerfile").write_text(
        textwrap.dedent(dockerfile).strip() + "\n",
        encoding="utf-8",
    )


def base_image_for_runtime(runtime: str) -> str:
    match = re.fullmatch(r"python(\d+\.\d+)", runtime)
    if not match:
        raise BuildError(f"Unsupported runtime: {runtime}")
    return f"python:{match.group(1)}-slim"


def extract_source_bundle(source_bundle: Path, build_path: Path) -> None:
    try:
        with zipfile.ZipFile(source_bundle) as archive:
            for info in archive.infolist():
                if info.is_dir():
                    continue
                target = safe_archive_target(build_path, info.filename)
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(info) as src, target.open("wb") as dst:
                    shutil.copyfileobj(src, dst)
    except zipfile.BadZipFile as exc:
        raise BuildError("Function bundle is not a valid zip archive.") from exc


def safe_archive_target(root: Path, name: str) -> Path:
    if "\\" in name:
        raise BuildError(f"Bundle contains unsafe path: {name}")
    path = PurePosixPath(name)
    if path.is_absolute() or ".." in path.parts:
        raise BuildError(f"Bundle contains unsafe path: {name}")
    return root / Path(*path.parts)


def format_docker_logs(logs) -> list[str]:
    lines = []
    for item in logs or []:
        if isinstance(item, bytes):
            lines.append(item.decode("utf-8", errors="replace").rstrip())
        elif isinstance(item, str):
            lines.append(item.rstrip())
        elif isinstance(item, dict):
            message = item.get("stream") or item.get("status") or item.get("error")
            if message:
                lines.append(str(message).rstrip())
    return [line for line in lines if line]
