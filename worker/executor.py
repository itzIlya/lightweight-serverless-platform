from __future__ import annotations

import io
from dataclasses import dataclass
import json
import os
from pathlib import Path
from pathlib import PurePosixPath
import tarfile
import tempfile
import time
from typing import Any


class ExecutionError(RuntimeError):
    pass


@dataclass
class ExecutionResult:
    status: str
    result: dict
    stdout: str
    stderr: str
    exit_code: int | None
    duration_ms: int
    error_message: str = ""
    cold_start: bool = True


def get_docker_client():
    import docker

    return docker.from_env()


class DockerExecutor:
    def __init__(self, docker_client=None, backend_client=None) -> None:
        self.docker_client = docker_client or get_docker_client()
        self.backend_client = backend_client

    def run(self, job: dict) -> ExecutionResult:
        image_ref = job.get("image_ref")
        if not image_ref:
            raise ExecutionError(
                "Function version has no image_ref yet. Build service must create an image before execution."
            )

        config = job.get("config") or {}
        timeout_seconds = int(config.get("timeout_seconds", 60))
        memory_mb = int(config.get("memory_mb", 256))
        event = job.get("event") or {}
        runtime_root = Path(os.getenv("FUNCTION_RUNTIME_ROOT", "/runtime-sandboxes"))
        runtime_root.mkdir(parents=True, exist_ok=True)

        started = time.monotonic()
        with tempfile.TemporaryDirectory(
            prefix=f"invocation-{job['request_id']}-",
            dir=runtime_root,
        ) as root:
            root_path = Path(root)
            input_dir = root_path / "input"
            input_files_dir = input_dir / "files"
            output_dir = root_path / "output"
            input_dir.mkdir()
            input_files_dir.mkdir()
            output_dir.mkdir()

            (input_dir / "event.json").write_text(
                json.dumps(event),
                encoding="utf-8",
            )
            input_files = self._prepare_input_files(job, input_files_dir)
            sandbox_volume = self.docker_client.volumes.create(
                name=f"invocation-{job['request_id']}"
            )
            container = self.docker_client.containers.create(
                image_ref,
                detach=True,
                environment={
                    "FUNCTION_EVENT_PATH": "/sandbox/input/event.json",
                    "FUNCTION_EVENT_JSON": json.dumps(event),
                    "FUNCTION_INPUT_FILES_DIR": "/sandbox/input/files",
                    "FUNCTION_INPUT_FILES_JSON": json.dumps(input_files),
                    "FUNCTION_OUTPUT_DIR": "/sandbox/output",
                    "FUNCTION_HANDLER": job.get("handler", "handler.main"),
                    "FUNCTION_REQUEST_ID": job["request_id"],
                },
                mem_limit=f"{memory_mb}m",
                network_disabled=True,
                volumes={sandbox_volume.name: {"bind": "/sandbox", "mode": "rw"}},
            )

            try:
                self._copy_directory_into_container(container, input_dir, "/sandbox")
                container.start()
                exit_code = self._wait_for_exit(container, timeout_seconds)
                stdout = self._read_logs(container, stdout=True, stderr=False)
                stderr = self._read_logs(container, stdout=False, stderr=True)
                self._copy_directory_from_container(
                    container,
                    "/sandbox/output",
                    output_dir,
                )
                result = self._read_result(output_dir, stdout)
                status = "succeeded" if exit_code == 0 else "failed"
                duration_ms = int((time.monotonic() - started) * 1000)
                error_message = "" if exit_code == 0 else "Container exited with a non-zero status."

                return ExecutionResult(
                    status=status,
                    result=result,
                    stdout=stdout,
                    stderr=stderr,
                    exit_code=exit_code,
                    duration_ms=duration_ms,
                    error_message=error_message,
                )
            finally:
                self._remove_container(container)
                self._remove_volume(sandbox_volume)

    def _wait_for_exit(self, container, timeout_seconds: int) -> int | None:
        deadline = time.monotonic() + timeout_seconds
        while time.monotonic() < deadline:
            container.reload()
            state = container.attrs.get("State", {})
            if not state.get("Running", False):
                return state.get("ExitCode")
            time.sleep(0.5)

        container.kill()
        raise ExecutionError(f"Function execution timed out after {timeout_seconds} seconds.")

    def _read_logs(self, container, *, stdout: bool, stderr: bool) -> str:
        logs = container.logs(stdout=stdout, stderr=stderr)
        return logs.decode("utf-8", errors="replace")

    def _read_result(self, output_dir: Path, stdout: str) -> dict:
        result_path = output_dir / "result.json"
        if not result_path.exists():
            matches = list(output_dir.rglob("result.json"))
            if matches:
                result_path = matches[0]
            else:
                return self._read_result_from_stdout(stdout)

        if not result_path.exists():
            return self._read_result_from_stdout(stdout)

        try:
            return json.loads(result_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {"raw_result": result_path.read_text(encoding="utf-8")}

    def _read_result_from_stdout(self, stdout: str) -> dict:
        for line in reversed(stdout.splitlines()):
            if line.startswith("__FUNCTION_RESULT__="):
                payload = line.split("=", 1)[1]
                try:
                    return json.loads(payload)
                except json.JSONDecodeError:
                    return {"raw_result": payload}
        return {}

    def _prepare_input_files(self, job: dict, input_files_dir: Path) -> list[dict[str, Any]]:
        if self.backend_client is None:
            return []

        request_id = job["request_id"]
        records = self.backend_client.list_invocation_inputs(request_id)

        prepared: list[dict[str, Any]] = []
        for record in records or []:
            file_id = record["id"]
            safe_name = self._safe_filename(record.get("original_name", "input"))
            local_name = f"{int(record.get('position', 0)):03d}-{safe_name}"
            destination = input_files_dir / local_name
            self.backend_client.download_invocation_input(
                request_id,
                file_id,
                destination,
            )
            prepared.append(
                {
                    "id": file_id,
                    "name": record.get("original_name", local_name),
                    "content_type": record.get("content_type", ""),
                    "size_bytes": record.get("size_bytes", 0),
                    "path": f"/sandbox/input/files/{local_name}",
                }
            )
        return prepared

    def _copy_directory_into_container(
        self,
        container,
        source_dir: Path,
        target_path: str,
    ) -> None:
        container.put_archive(target_path, self._build_tar_archive(source_dir))

    def _copy_directory_from_container(
        self,
        container,
        source_path: str,
        destination_dir: Path,
    ) -> None:
        archive_stream, _ = container.get_archive(source_path)
        archive_bytes = b"".join(archive_stream)
        self._extract_tar_archive(archive_bytes, destination_dir)

    def _build_tar_archive(self, source_dir: Path) -> bytes:
        buffer = io.BytesIO()
        with tarfile.open(fileobj=buffer, mode="w") as archive:
            for path in sorted(source_dir.rglob("*")):
                archive.add(path, arcname=str(path.relative_to(source_dir.parent)))
        return buffer.getvalue()

    def _extract_tar_archive(self, archive_bytes: bytes, destination_dir: Path) -> None:
        destination_dir.mkdir(parents=True, exist_ok=True)
        with tarfile.open(fileobj=io.BytesIO(archive_bytes), mode="r:*") as archive:
            for member in archive.getmembers():
                self._validate_tar_member(member, destination_dir)
            archive.extractall(path=destination_dir, filter="data")

    def _validate_tar_member(self, member: tarfile.TarInfo, destination_dir: Path) -> None:
        resolved_root = destination_dir.resolve()
        resolved_member = (destination_dir / member.name).resolve(strict=False)
        if resolved_root != resolved_member and resolved_root not in resolved_member.parents:
            raise ExecutionError("Refusing to extract files outside the sandbox.")

    def _safe_filename(self, value: str) -> str:
        safe = PurePosixPath(str(value).replace("\\", "/")).name
        return safe.replace(":", "_") or "input"

    def _remove_container(self, container) -> None:
        try:
            container.remove(force=True)
        except Exception:
            pass

    def _remove_volume(self, volume) -> None:
        try:
            volume.remove(force=True)
        except Exception:
            pass
