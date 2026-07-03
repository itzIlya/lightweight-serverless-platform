from __future__ import annotations

import io
import hashlib
from dataclasses import dataclass, field
import json
import logging
import mimetypes
import os
from pathlib import Path
from pathlib import PurePosixPath
import tarfile
import tempfile
import time
from typing import Any

from requests.exceptions import ReadTimeout


SANDBOX_EXPORT_PATH = "/sandbox/export"
SANDBOX_EXPORT_OUTPUT_PATH = "/sandbox/export/output"
logger = logging.getLogger("worker.executor")


class ExecutionError(RuntimeError):
    pass


class OutputValidationError(ExecutionError):
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
    timing_ms: dict[str, int] = field(default_factory=dict)
    output_manifest: list[dict[str, Any]] = field(default_factory=list)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(64 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


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
        output_tmpfs_size_bytes = self._output_tmpfs_size_bytes(job)
        event = job.get("event") or {}
        runtime_root = Path(os.getenv("FUNCTION_RUNTIME_ROOT", "/runtime-sandboxes"))
        runtime_root.mkdir(parents=True, exist_ok=True)

        started = time.monotonic()
        timing: dict[str, int] = {}

        def record_step(name: str, step_started: float) -> None:
            timing[name] = int((time.monotonic() - step_started) * 1000)

        with tempfile.TemporaryDirectory(
            prefix=f"invocation-{job['request_id']}-",
            dir=runtime_root,
        ) as root:
            setup_started = time.monotonic()
            root_path = Path(root)
            input_dir = root_path / "input"
            input_files_dir = input_dir / "files"
            export_dir = root_path / "export"
            input_dir.mkdir()
            input_files_dir.mkdir()
            export_dir.mkdir()

            (input_dir / "event.json").write_text(
                json.dumps(event),
                encoding="utf-8",
            )
            input_files = self._prepare_input_files(job, input_files_dir)
            record_step("sandbox_prepare_ms", setup_started)

            volume_started = time.monotonic()
            sandbox_volume = self.docker_client.volumes.create(
                name=f"invocation-{job['request_id']}"
            )
            record_step("docker_volume_create_ms", volume_started)

            create_started = time.monotonic()
            container = self.docker_client.containers.create(
                image_ref,
                command=[
                    "-c",
                    self._runner_export_command(),
                ],
                detach=True,
                entrypoint=["sh"],
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
                tmpfs={
                    "/sandbox/output": f"size={output_tmpfs_size_bytes}",
                },
                volumes={sandbox_volume.name: {"bind": "/sandbox", "mode": "rw"}},
            )
            record_step("docker_container_create_ms", create_started)

            try:
                input_copy_started = time.monotonic()
                self._copy_directory_into_container(container, input_dir, "/sandbox")
                record_step("docker_input_copy_ms", input_copy_started)

                start_started = time.monotonic()
                container.start()
                record_step("docker_container_start_ms", start_started)

                wait_started = time.monotonic()
                exit_code = self._wait_for_exit(container, timeout_seconds)
                record_step("docker_wait_ms", wait_started)

                logs_started = time.monotonic()
                stdout = self._read_logs(container, stdout=True, stderr=False)
                stderr = self._read_logs(container, stdout=False, stderr=True)
                record_step("docker_logs_read_ms", logs_started)
                timing.update(self._read_runner_timings(stdout))

                export_started = time.monotonic()
                self._copy_directory_from_container(
                    container,
                    SANDBOX_EXPORT_PATH,
                    export_dir,
                )
                record_step("docker_export_copy_ms", export_started)

                result_started = time.monotonic()
                effective_export_dir = self._effective_export_dir(export_dir)
                copy_exit_code = self._read_export_status(
                    effective_export_dir,
                    "output_copy_exit_code",
                )
                effective_output_dir = self._effective_output_dir(effective_export_dir)
                result = self._read_result(effective_output_dir, stdout)
                record_step("result_read_ms", result_started)
                duration_ms = int((time.monotonic() - started) * 1000)
                if copy_exit_code not in (None, 0):
                    timing["executor_duration_ms"] = duration_ms
                    logger.info(
                        "invocation executor timing request_id=%s timings=%s",
                        job["request_id"],
                        json.dumps(timing, sort_keys=True),
                    )
                    return ExecutionResult(
                        status="failed",
                        result=result,
                        stdout=stdout,
                        stderr=stderr,
                        exit_code=exit_code,
                        duration_ms=duration_ms,
                        error_message=self._read_export_error(effective_export_dir),
                        timing_ms=timing,
                    )
                try:
                    validation_started = time.monotonic()
                    output_files = self._validate_declared_output_files(
                        job,
                        effective_output_dir,
                    )
                    record_step("output_validation_ms", validation_started)
                except OutputValidationError as exc:
                    timing["executor_duration_ms"] = duration_ms
                    logger.info(
                        "invocation executor timing request_id=%s timings=%s",
                        job["request_id"],
                        json.dumps(timing, sort_keys=True),
                    )
                    return ExecutionResult(
                        status="failed",
                        result=result,
                        stdout=stdout,
                        stderr=stderr,
                        exit_code=exit_code,
                        duration_ms=duration_ms,
                        error_message=str(exc),
                        timing_ms=timing,
                    )

                output_upload_started = time.monotonic()
                output_manifest = self._upload_output_files(job, output_files)
                record_step("output_upload_ms", output_upload_started)
                status = "succeeded" if exit_code == 0 else "failed"
                error_message = (
                    ""
                    if exit_code == 0
                    else "Container exited with a non-zero status."
                )
                timing["executor_duration_ms"] = duration_ms
                logger.info(
                    "invocation executor timing request_id=%s timings=%s",
                    job["request_id"],
                    json.dumps(timing, sort_keys=True),
                )

                return ExecutionResult(
                    status=status,
                    result=result,
                    stdout=stdout,
                    stderr=stderr,
                    exit_code=exit_code,
                    duration_ms=duration_ms,
                    error_message=error_message,
                    timing_ms=timing,
                    output_manifest=output_manifest,
                )
            finally:
                cleanup_started = time.monotonic()
                self._remove_container(container)
                self._remove_volume(sandbox_volume)
                record_step("docker_cleanup_ms", cleanup_started)
                timing["executor_wall_with_cleanup_ms"] = int(
                    (time.monotonic() - started) * 1000
                )
                logger.info(
                    "invocation executor final timing request_id=%s timings=%s",
                    job["request_id"],
                    json.dumps(timing, sort_keys=True),
                )

    def _runner_export_command(self) -> str:
        return (
            "python /runner.py; "
            "code=$?; "
            f"mkdir -p {SANDBOX_EXPORT_OUTPUT_PATH}; "
            f"cp -a /sandbox/output/. {SANDBOX_EXPORT_OUTPUT_PATH}/ "
            f"2>{SANDBOX_EXPORT_PATH}/output_copy_error.txt; "
            "copy_code=$?; "
            f"printf '%s' \"$code\" > {SANDBOX_EXPORT_PATH}/runner_exit_code; "
            f"printf '%s' \"$copy_code\" > {SANDBOX_EXPORT_PATH}/output_copy_exit_code; "
            'exit "$code"'
        )

    def _wait_for_exit(self, container, timeout_seconds: int) -> int | None:
        try:
            wait_result = container.wait(timeout=timeout_seconds)
        except ReadTimeout as exc:
            container.kill()
            raise ExecutionError(
                f"Function execution timed out after {timeout_seconds} seconds."
            ) from exc
        return wait_result.get("StatusCode")

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

    def _read_runner_timings(self, stdout: str) -> dict[str, int]:
        for line in reversed(stdout.splitlines()):
            if not line.startswith("__FUNCTION_TIMING__="):
                continue
            payload = line.split("=", 1)[1]
            try:
                timings = json.loads(payload)
            except json.JSONDecodeError:
                return {}
            if not isinstance(timings, dict):
                return {}
            return {
                key: value
                for key, value in timings.items()
                if key.startswith("runner_")
                and isinstance(value, int)
                and not isinstance(value, bool)
            }
        return {}

    def _effective_output_dir(self, output_dir: Path) -> Path:
        nested = output_dir / "output"
        if nested.is_dir():
            return nested
        return output_dir

    def _effective_export_dir(self, export_dir: Path) -> Path:
        nested = export_dir / "export"
        if nested.is_dir():
            return nested
        return export_dir

    def _read_export_status(self, export_dir: Path, filename: str) -> int | None:
        path = export_dir / filename
        if not path.exists():
            return None
        try:
            return int(path.read_text(encoding="utf-8").strip())
        except ValueError:
            return None

    def _read_export_error(self, export_dir: Path) -> str:
        path = export_dir / "output_copy_error.txt"
        if not path.exists():
            return "Could not export output files from the tmpfs sandbox."
        detail = path.read_text(encoding="utf-8", errors="replace").strip()
        if not detail:
            return "Could not export output files from the tmpfs sandbox."
        return f"Could not export output files from the tmpfs sandbox: {detail}"

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

    def _upload_output_files(
        self,
        job: dict,
        output_files: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        if self.backend_client is None:
            return []

        request_id = job["request_id"]
        manifest = []
        for position, item in enumerate(output_files):
            content_type = (
                mimetypes.guess_type(item["path"].name)[0]
                or "application/octet-stream"
            )
            checksum = file_sha256(item["path"])
            manifest_item = {
                "original_path": item["original_path"],
                "size_bytes": int(item.get("size_bytes", item["path"].stat().st_size)),
                "checksum_sha256": checksum,
            }
            if int(job.get("coordination_version", 1)) == 2:
                self.backend_client.upload_staged_invocation_output(
                    request_id,
                    job_id=job["job_id"],
                    dispatch_attempt=int(job["dispatch_attempt"]),
                    completion_id=job["completion_id"],
                    original_path=item["original_path"],
                    checksum_sha256=checksum,
                    file_path=item["path"],
                    position=position,
                    content_type=content_type,
                )
            else:
                self.backend_client.upload_invocation_output(
                    request_id,
                    original_path=item["original_path"],
                    file_path=item["path"],
                    position=position,
                    content_type=content_type,
                )
            manifest.append(manifest_item)
        return manifest

    def _validate_declared_output_files(
        self,
        job: dict,
        output_dir: Path,
    ) -> list[dict[str, Any]]:
        output_files = self._collect_declared_output_files(job, output_dir)
        max_files = self._positive_int(
            job.get("invocation_output_max_files"),
            default=len(job.get("declared_output_files") or []),
        )
        max_file_size = self._megabytes_to_bytes(
            job.get("invocation_output_max_file_size_mb"),
            default_mb=10,
        )
        max_total_size = self._megabytes_to_bytes(
            job.get("invocation_output_max_total_size_mb"),
            default_mb=25,
        )

        if output_files and max_files <= 0:
            raise OutputValidationError("Function version does not allow output files.")
        if len(output_files) > max_files:
            raise OutputValidationError(
                f"Invocation produced {len(output_files)} declared output file(s), "
                f"but the limit is {max_files}."
            )

        total_size = 0
        for item in output_files:
            size = item["path"].stat().st_size
            item["size_bytes"] = size
            total_size += size
            if size > max_file_size:
                raise OutputValidationError(
                    f"Output file {item['original_path']} is {size} byte(s), "
                    f"but the per-file limit is {max_file_size} byte(s)."
                )

        if total_size > max_total_size:
            raise OutputValidationError(
                f"Invocation produced {total_size} byte(s) of declared output, "
                f"but the total limit is {max_total_size} byte(s)."
            )
        return output_files

    def _collect_declared_output_files(
        self,
        job: dict,
        output_dir: Path,
    ) -> list[dict[str, Any]]:
        declared = job.get("declared_output_files") or []
        if not isinstance(declared, list):
            raise OutputValidationError("Declared output files must be a list.")

        collected: list[dict[str, Any]] = []
        for raw_name in declared:
            name = self._safe_output_name(raw_name)
            if name is None or name == "result.json":
                raise OutputValidationError(
                    f"Declared output file name is unsafe or reserved: {raw_name!r}"
                )
            path = output_dir / name
            if not path.exists():
                continue
            if not path.is_file():
                raise OutputValidationError(
                    f"Declared output path is not a file: {name}"
                )
            collected.append({"original_path": name, "path": path})
        return collected

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

    def _safe_output_name(self, value: str) -> str | None:
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

    def _positive_int(self, value, *, default: int) -> int:
        if value in ("", None):
            return default
        try:
            return int(value)
        except (TypeError, ValueError):
            return default

    def _megabytes_to_bytes(self, value, *, default_mb: int) -> int:
        return self._positive_int(value, default=default_mb) * 1024 * 1024

    def _output_tmpfs_size_bytes(self, job: dict) -> int:
        size = self._megabytes_to_bytes(
            job.get("invocation_output_max_total_size_mb"),
            default_mb=10,
        )
        return max(size, 1024 * 1024)

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
