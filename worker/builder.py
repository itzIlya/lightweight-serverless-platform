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
import time

RUNNER_STARTED_NS = time.perf_counter_ns()

import importlib
from contextlib import redirect_stderr, redirect_stdout
from http.server import BaseHTTPRequestHandler, HTTPServer
import io
import json
import mimetypes
import os
from pathlib import Path, PurePosixPath
import shutil
import sys
import traceback
from urllib import error as urlerror
from urllib import request as urlrequest

RUNNER_MODULE_IMPORTS_MS = int(
    (time.perf_counter_ns() - RUNNER_STARTED_NS) / 1_000_000
)


def elapsed_ms(started_ns):
    return int((time.perf_counter_ns() - started_ns) / 1_000_000)


def load_handler(handler_path):
    module_name, _, function_name = handler_path.partition(".")
    if not module_name or not function_name:
        raise ValueError("Handler must use the form module.function")
    module = importlib.import_module(module_name)
    return getattr(module, function_name)


def truthy(value):
    return str(value or "").strip().lower() in {"1", "true", "yes", "on"}


def env_get(env, name, default=""):
    source = env if env is not None else os.environ
    return source.get(name, default)


def int_env(name, default, env=None):
    try:
        return int(env_get(env, name, default))
    except (TypeError, ValueError):
        return int(default)


def safe_output_name(value):
    name = str(value or "").strip().replace("\\", "/")
    path = PurePosixPath(name)
    if (
        not name
        or path.is_absolute()
        or path.name != name
        or name in {".", ".."}
        or any(part == ".." for part in path.parts)
    ):
        return None
    return name


def collect_declared_output_files(output_dir, declared, max_files, max_file_size, max_total_size):
    if not isinstance(declared, list):
        raise ValueError("Declared output files must be a list.")

    collected = []
    total_size = 0
    for raw_name in declared:
        name = safe_output_name(raw_name)
        if name is None or name == "result.json":
            raise ValueError(f"Declared output file name is unsafe or reserved: {raw_name!r}")
        path = output_dir / name
        if not path.exists():
            continue
        if not path.is_file():
            raise ValueError(f"Declared output path is not a file: {name}")
        size = path.stat().st_size
        collected.append(
            {
                "original_path": name,
                "path": path,
                "size_bytes": size,
            }
        )
        total_size += size
        if size > max_file_size:
            raise ValueError(
                f"Output file {name} is {size} byte(s), "
                f"but the per-file limit is {max_file_size} byte(s)."
            )

    if collected and max_files <= 0:
        raise ValueError("Function version does not allow output files.")
    if len(collected) > max_files:
        raise ValueError(
            f"Invocation produced {len(collected)} declared output file(s), "
            f"but the limit is {max_files}."
        )
    if total_size > max_total_size:
        raise ValueError(
            f"Invocation produced {total_size} byte(s) of declared output, "
            f"but the total limit is {max_total_size} byte(s)."
        )
    return collected


def upload_file(url, token, job_id, dispatch_attempt, completion_id, item, position, timeout):
    body = item["path"].read_bytes()
    content_type = mimetypes.guess_type(item["path"].name)[0] or "application/octet-stream"
    http_request = urlrequest.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Content-Type": content_type,
            "X-Runner-Upload-Token": token,
            "X-Job-Id": job_id,
            "X-Dispatch-Attempt": str(dispatch_attempt),
            "X-Completion-Id": completion_id,
            "X-Original-Path": item["original_path"],
            "X-Position": str(position),
        },
    )
    try:
        with urlrequest.urlopen(http_request, timeout=timeout) as response:
            response_body = response.read().decode("utf-8")
            payload = json.loads(response_body) if response_body else {}
    except urlerror.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"direct output upload failed with HTTP {exc.code}: {detail}"
        ) from exc
    except urlerror.URLError as exc:
        raise RuntimeError(f"direct output upload failed: {exc}") from exc
    return {
        "original_path": item["original_path"],
        "size_bytes": item["size_bytes"],
        "checksum_sha256": payload.get("checksum_sha256", ""),
    }


def upload_declared_outputs_directly(output_dir, timings, env=None):
    if output_dir is None or not truthy(env_get(env, "FUNCTION_OUTPUT_DIRECT_UPLOAD_ENABLED")):
        return None

    upload_url = env_get(env, "FUNCTION_OUTPUT_UPLOAD_URL", "")
    upload_token = env_get(env, "FUNCTION_OUTPUT_UPLOAD_TOKEN", "")
    job_id = env_get(env, "FUNCTION_OUTPUT_UPLOAD_JOB_ID", "")
    completion_id = env_get(env, "FUNCTION_OUTPUT_UPLOAD_COMPLETION_ID", "")
    dispatch_attempt = int_env("FUNCTION_OUTPUT_UPLOAD_DISPATCH_ATTEMPT", 0, env=env)
    timeout = int_env("FUNCTION_OUTPUT_UPLOAD_TIMEOUT_SECONDS", 10, env=env)
    if not upload_url or not upload_token or not job_id or not completion_id or dispatch_attempt < 1:
        raise RuntimeError("Direct output upload is enabled but upload metadata is incomplete.")

    scan_started = time.perf_counter_ns()
    declared = json.loads(env_get(env, "FUNCTION_DECLARED_OUTPUT_FILES", "[]") or "[]")
    output_files = collect_declared_output_files(
        output_dir,
        declared,
        int_env("FUNCTION_OUTPUT_MAX_FILES", len(declared), env=env),
        int_env("FUNCTION_OUTPUT_MAX_FILE_SIZE_BYTES", 10 * 1024 * 1024, env=env),
        int_env("FUNCTION_OUTPUT_MAX_TOTAL_SIZE_BYTES", 25 * 1024 * 1024, env=env),
    )
    timings["runner_output_scan_ms"] = elapsed_ms(scan_started)

    upload_started = time.perf_counter_ns()
    manifest = [
        upload_file(
            upload_url,
            upload_token,
            job_id,
            dispatch_attempt,
            completion_id,
            item,
            position,
            timeout,
        )
        for position, item in enumerate(output_files)
    ]
    timings["runner_output_upload_ms"] = elapsed_ms(upload_started)
    return manifest


def clean_directory(path):
    path.mkdir(parents=True, exist_ok=True)
    for child in path.iterdir():
        if child.is_dir() and not child.is_symlink():
            shutil.rmtree(child)
        else:
            child.unlink()


def apply_function_environment(env):
    for key, value in (env or {}).items():
        if key.startswith("FUNCTION_"):
            os.environ[key] = str(value)


def run_loaded_handler(handler, payload, base_env):
    started_ns = time.perf_counter_ns()
    timings = {
        "runner_module_imports_ms": 0,
        "runner_handler_import_ms": 0,
        "runner_resident_reused": 1,
    }
    environment_started = time.perf_counter_ns()
    env = dict(base_env)
    env.update(payload.get("environment") or {})
    apply_function_environment(env)
    request_id = str(payload.get("request_id") or env_get(env, "FUNCTION_REQUEST_ID", ""))
    output_dir_value = env_get(env, "FUNCTION_OUTPUT_DIR", "/sandbox/output")
    output_dir = Path(output_dir_value) if output_dir_value else None
    timings["runner_environment_read_ms"] = elapsed_ms(environment_started)

    event_started = time.perf_counter_ns()
    if "event" in payload:
        event = payload["event"]
    else:
        event = json.loads(Path(env_get(env, "FUNCTION_EVENT_PATH", "")).read_text(encoding="utf-8"))
    timings["runner_event_load_ms"] = elapsed_ms(event_started)

    setup_started = time.perf_counter_ns()
    if output_dir is not None:
        clean_directory(output_dir)
    timings["runner_setup_ms"] = elapsed_ms(setup_started)

    stdout_buffer = io.StringIO()
    stderr_buffer = io.StringIO()
    exit_code = 0
    result_payload = {}
    serialized = "{}"
    output_manifest = None
    with redirect_stdout(stdout_buffer), redirect_stderr(stderr_buffer):
        try:
            handler_started = time.perf_counter_ns()
            result = handler(event, {"request_id": request_id})
            timings["runner_handler_execution_ms"] = elapsed_ms(handler_started)

            serialize_started = time.perf_counter_ns()
            result_payload = result
            try:
                serialized = json.dumps(result_payload)
            except TypeError:
                result_payload = {"repr": repr(result_payload)}
                serialized = json.dumps(result_payload)
            timings["runner_result_serialize_ms"] = elapsed_ms(serialize_started)

            write_started = time.perf_counter_ns()
            if output_dir is not None:
                try:
                    result_path = output_dir / "result.json"
                    result_path.write_text(serialized, encoding="utf-8")
                except Exception:
                    pass
            timings["runner_result_write_ms"] = elapsed_ms(write_started)

            output_manifest = upload_declared_outputs_directly(output_dir, timings, env=env)
        except Exception:
            exit_code = 1
            traceback.print_exc(file=stderr_buffer)

    timings["runner_total_ms"] = elapsed_ms(started_ns)
    return {
        "exit_code": exit_code,
        "result": result_payload,
        "stdout": stdout_buffer.getvalue(),
        "stderr": stderr_buffer.getvalue(),
        "output_manifest": output_manifest,
        "timings": timings,
    }


class ResidentRunnerHandler(BaseHTTPRequestHandler):
    server_version = "ServerlessResidentRunner/0.1"

    def log_message(self, format, *args):
        return

    def do_GET(self):
        if self.path != "/health":
            self.send_error(404)
            return
        self._send_json({"ok": True})

    def do_POST(self):
        try:
            if self.path == "/prepare":
                clean_directory(Path("/sandbox/input"))
                clean_directory(Path("/sandbox/output"))
                self._send_json({"ok": True})
                return
            if self.path != "/invoke":
                self.send_error(404)
                return
            payload = self._read_json()
            response = run_loaded_handler(
                self.server.function_handler,
                payload,
                self.server.base_environment,
            )
            self._send_json(response)
        except Exception as exc:
            self._send_json(
                {
                    "exit_code": 1,
                    "result": {},
                    "stdout": "",
                    "stderr": "".join(
                        traceback.format_exception(type(exc), exc, exc.__traceback__)
                    ),
                    "output_manifest": None,
                    "timings": {},
                }
            )

    def _read_json(self):
        content_length = int(self.headers.get("Content-Length", "0") or "0")
        if content_length <= 0:
            return {}
        body = self.rfile.read(content_length).decode("utf-8")
        payload = json.loads(body)
        if not isinstance(payload, dict):
            raise ValueError("Request payload must be an object.")
        return payload

    def _send_json(self, payload):
        body = json.dumps(payload, sort_keys=True).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def serve_resident_runner():
    sys.path.insert(0, "/function")
    handler_path = os.environ.get("FUNCTION_HANDLER", "handler.main")
    import_started = time.perf_counter_ns()
    handler = load_handler(handler_path)
    startup_ms = elapsed_ms(import_started)
    host = os.environ.get("FUNCTION_RESIDENT_RUNNER_HOST", "0.0.0.0")
    port = int_env("FUNCTION_RESIDENT_RUNNER_PORT", 8765)
    server = HTTPServer((host, port), ResidentRunnerHandler)
    server.function_handler = handler
    server.base_environment = dict(os.environ)
    print(
        f"__FUNCTION_RESIDENT_READY__={json.dumps({'handler_import_ms': startup_ms})}",
        flush=True,
    )
    server.serve_forever()


def main():
    timings = {"runner_module_imports_ms": RUNNER_MODULE_IMPORTS_MS}
    environment_started = time.perf_counter_ns()
    event_path_value = os.environ.get("FUNCTION_EVENT_PATH", "")
    event_json = os.environ.get("FUNCTION_EVENT_JSON", "")
    output_dir_value = os.environ.get("FUNCTION_OUTPUT_DIR", "")
    handler_path = os.environ.get("FUNCTION_HANDLER", "handler.main")
    request_id = os.environ.get("FUNCTION_REQUEST_ID", "")
    timings["runner_environment_read_ms"] = elapsed_ms(environment_started)

    event_started = time.perf_counter_ns()
    if event_json:
        event = json.loads(event_json)
    else:
        event = json.loads(Path(event_path_value).read_text(encoding="utf-8"))
    timings["runner_event_load_ms"] = elapsed_ms(event_started)

    setup_started = time.perf_counter_ns()
    sys.path.insert(0, "/function")
    output_dir = Path(output_dir_value) if output_dir_value else None
    if output_dir is not None:
        output_dir.mkdir(parents=True, exist_ok=True)
    timings["runner_setup_ms"] = elapsed_ms(setup_started)

    import_started = time.perf_counter_ns()
    handler = load_handler(handler_path)
    timings["runner_handler_import_ms"] = elapsed_ms(import_started)

    handler_started = time.perf_counter_ns()
    result = handler(event, {"request_id": request_id})
    timings["runner_handler_execution_ms"] = elapsed_ms(handler_started)

    serialize_started = time.perf_counter_ns()
    result_payload = result
    try:
        serialized = json.dumps(result_payload)
    except TypeError:
        result_payload = {"repr": repr(result_payload)}
        serialized = json.dumps(result_payload)
    timings["runner_result_serialize_ms"] = elapsed_ms(serialize_started)

    write_started = time.perf_counter_ns()
    if output_dir is not None:
        try:
            result_path = output_dir / "result.json"
            result_path.write_text(serialized, encoding="utf-8")
        except Exception:
            pass
    timings["runner_result_write_ms"] = elapsed_ms(write_started)

    output_manifest = upload_declared_outputs_directly(output_dir, timings)
    timings["runner_total_ms"] = elapsed_ms(RUNNER_STARTED_NS)

    print(f"__FUNCTION_RESULT__={serialized}")
    if output_manifest is not None:
        print(f"__FUNCTION_OUTPUT_MANIFEST__={json.dumps(output_manifest, sort_keys=True)}")
    print(f"__FUNCTION_TIMING__={json.dumps(timings, sort_keys=True)}")


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1 and sys.argv[1] == "--serve":
            serve_resident_runner()
        else:
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
