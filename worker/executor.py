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
import uuid
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from typing import Any
from urllib import error as urlerror
from urllib import request as urlrequest

from requests.exceptions import ReadTimeout

from warm_pool import WarmContainerKey, WarmContainerPool


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
    def __init__(
        self,
        docker_client=None,
        backend_client=None,
        *,
        warm_enabled: bool | None = None,
        warm_pool: WarmContainerPool | None = None,
    ) -> None:
        self.docker_client = docker_client or get_docker_client()
        self.backend_client = backend_client
        self.warm_enabled = (
            self._env_bool("WORKER_WARM_CONTAINERS_ENABLED", default=False)
            if warm_enabled is None
            else warm_enabled
        )
        self.runner_direct_output_upload_enabled = self._env_bool(
            "WORKER_RUNNER_DIRECT_OUTPUT_UPLOAD_ENABLED",
            default=False,
        )
        self.warm_resident_runner_enabled = self._env_bool(
            "WORKER_WARM_RESIDENT_RUNNER_ENABLED",
            default=False,
        )
        self.warm_resident_runner_port = self._positive_int(
            os.getenv("WORKER_WARM_RESIDENT_RUNNER_PORT"),
            default=8765,
        )
        self.warm_resident_runner_startup_timeout_seconds = self._positive_int(
            os.getenv("WORKER_WARM_RESIDENT_RUNNER_STARTUP_TIMEOUT_SECONDS"),
            default=5,
        )
        self.runner_backend_base_url = os.getenv("BACKEND_BASE_URL", "")
        self.function_container_network = os.getenv("FUNCTION_CONTAINER_NETWORK", "")
        self.runner_output_upload_timeout_seconds = self._positive_int(
            os.getenv("WORKER_RUNNER_OUTPUT_UPLOAD_TIMEOUT_SECONDS"),
            default=10,
        )
        self.runner_output_upload_token_ttl_seconds = self._positive_int(
            os.getenv("WORKER_RUNNER_OUTPUT_UPLOAD_TOKEN_TTL_SECONDS"),
            default=300,
        )
        self.warm_pool = warm_pool or (
            WarmContainerPool(
                max_containers=int(os.getenv("WORKER_WARM_MAX_CONTAINERS", "2")),
                max_per_key=int(
                    os.getenv("WORKER_WARM_MAX_PER_FUNCTION_VERSION", "1")
                ),
                idle_ttl_seconds=float(
                    os.getenv("WORKER_WARM_IDLE_TTL_SECONDS", "60")
                ),
                max_age_seconds=float(
                    os.getenv("WORKER_WARM_MAX_AGE_SECONDS", "900")
                ),
                max_uses=int(os.getenv("WORKER_WARM_MAX_USES", "100")),
                max_memory_mb=int(os.getenv("WORKER_WARM_MAX_MEMORY_MB", "0")),
            )
            if self.warm_enabled
            else None
        )

    def run(self, job: dict) -> ExecutionResult:
        if self.warm_enabled and self.warm_pool is not None:
            return self._run_warm(job)
        return self._run_cold(job)

    def _run_cold(self, job: dict) -> ExecutionResult:
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
        direct_output_upload = self._runner_direct_output_upload_enabled(job)

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
                    self._runner_command(
                        job,
                        direct_output_upload=direct_output_upload,
                    ),
                ],
                detach=True,
                entrypoint=["sh"],
                environment=self._runner_environment(
                    job,
                    event,
                    input_files,
                    direct_output_upload=direct_output_upload,
                ),
                mem_limit=f"{memory_mb}m",
                **self._container_network_kwargs(
                    direct_output_upload=direct_output_upload
                ),
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

                duration_ms = int((time.monotonic() - started) * 1000)
                declares_outputs = self._declares_output_files(job)
                if direct_output_upload:
                    result_started = time.monotonic()
                    result = self._read_result(None, stdout)
                    record_step("result_read_ms", result_started)
                    output_manifest = self._read_runner_output_manifest(stdout)
                    if (
                        output_manifest is None
                        and (job.get("declared_output_files") or [])
                    ):
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
                            error_message="Runner did not report direct output uploads.",
                            timing_ms=timing,
                        )
                    output_manifest = output_manifest or []
                    timing["docker_export_copy_ms"] = 0
                    timing["output_validation_ms"] = 0
                    timing["output_upload_ms"] = 0
                elif not declares_outputs:
                    result_started = time.monotonic()
                    result = self._read_result(None, stdout)
                    record_step("result_read_ms", result_started)
                    output_manifest = []
                    timing["docker_export_copy_ms"] = 0
                    timing["output_validation_ms"] = 0
                    timing["output_upload_ms"] = 0
                else:
                    export_started = time.monotonic()
                    self._copy_directory_from_container(
                        container,
                        SANDBOX_EXPORT_PATH,
                        export_dir,
                    )
                    record_step("docker_export_copy_ms", export_started)

                    effective_export_dir = self._effective_export_dir(export_dir)
                    copy_exit_code = self._read_export_status(
                        effective_export_dir,
                        "output_copy_exit_code",
                    )
                    effective_output_dir = self._effective_output_dir(effective_export_dir)
                    result_started = time.monotonic()
                    result = self._read_result(effective_output_dir, stdout)
                    record_step("result_read_ms", result_started)
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

    def _run_warm(self, job: dict) -> ExecutionResult:
        image_ref = job.get("image_ref")
        if not image_ref:
            raise ExecutionError(
                "Function version has no image_ref yet. Build service must create an image before execution."
            )
        if self.warm_pool is None or self.warm_pool.max_containers <= 0:
            return self._run_cold(job)

        config = job.get("config") or {}
        timeout_seconds = int(config.get("timeout_seconds", 60))
        memory_mb = int(config.get("memory_mb", 256))
        output_tmpfs_size_bytes = self._output_tmpfs_size_bytes(job)
        event = job.get("event") or {}
        direct_output_upload = self._runner_direct_output_upload_enabled(job)
        use_resident_runner = self.warm_resident_runner_enabled
        key = self._warm_container_key(
            job,
            memory_mb,
            output_tmpfs_size_bytes,
            direct_output_upload=direct_output_upload,
        )
        runtime_root = Path(os.getenv("FUNCTION_RUNTIME_ROOT", "/runtime-sandboxes"))
        runtime_root.mkdir(parents=True, exist_ok=True)

        started = time.monotonic()
        timing: dict[str, int] = {}

        def record_step(name: str, step_started: float) -> None:
            timing[name] = int((time.monotonic() - step_started) * 1000)

        record = self.warm_pool.acquire(key)
        cold_start = record is None
        if record is None:
            create_started = time.monotonic()
            record = self._create_warm_container(
                key=key,
                image_ref=image_ref,
                memory_mb=memory_mb,
                output_tmpfs_size_bytes=output_tmpfs_size_bytes,
                request_id=job["request_id"],
                direct_output_upload=direct_output_upload,
            )
            if record is None:
                return self._run_cold(job)
            record_step("warm_container_create_ms", create_started)
        else:
            timing["warm_container_reused"] = 1

        reusable = False
        with tempfile.TemporaryDirectory(
            prefix=f"invocation-{job['request_id']}-",
            dir=runtime_root,
        ) as root:
            try:
                setup_started = time.monotonic()
                root_path = Path(root)
                input_dir = root_path / "input"
                input_files_dir = input_dir / "files"
                output_dir = root_path / "output"
                input_dir.mkdir()
                input_files_dir.mkdir()

                (input_dir / "event.json").write_text(
                    json.dumps(event),
                    encoding="utf-8",
                )
                input_files = self._prepare_input_files(job, input_files_dir)
                record_step("sandbox_prepare_ms", setup_started)

                if use_resident_runner:
                    prepare_started = time.monotonic()
                    self._prepare_resident_warm_runner(
                        record,
                        timeout_seconds=timeout_seconds,
                    )
                    record_step("warm_runner_prepare_ms", prepare_started)
                else:
                    cleanup_before_started = time.monotonic()
                    self._cleanup_warm_sandbox(record.container)
                    record_step(
                        "warm_sandbox_cleanup_before_ms",
                        cleanup_before_started,
                    )

                input_copy_started = time.monotonic()
                self._copy_directory_into_container(
                    record.container,
                    input_dir,
                    "/sandbox",
                )
                record_step("docker_input_copy_ms", input_copy_started)

                exec_started = time.monotonic()
                if use_resident_runner:
                    exit_code, stdout, stderr = self._invoke_resident_warm_runner(
                        record,
                        job=job,
                        event=event,
                        input_files=input_files,
                        timeout_seconds=timeout_seconds,
                        direct_output_upload=direct_output_upload,
                    )
                else:
                    exit_code, stdout, stderr = self._exec_runner_in_warm_container(
                        record.container,
                        job=job,
                        event=event,
                        input_files=input_files,
                        timeout_seconds=timeout_seconds,
                    )
                record_step("warm_runner_exec_ms", exec_started)
                timing.update(self._read_runner_timings(stdout))

                duration_ms = int((time.monotonic() - started) * 1000)
                declares_outputs = self._declares_output_files(job)
                if direct_output_upload:
                    result_started = time.monotonic()
                    result = self._read_result(None, stdout)
                    record_step("result_read_ms", result_started)
                    output_manifest = self._read_runner_output_manifest(stdout)
                    if (
                        output_manifest is None
                        and (job.get("declared_output_files") or [])
                    ):
                        timing["executor_duration_ms"] = duration_ms
                        self._log_invocation_timing(job, timing)
                        return ExecutionResult(
                            status="failed",
                            result=result,
                            stdout=stdout,
                            stderr=stderr,
                            exit_code=exit_code,
                            duration_ms=duration_ms,
                            error_message="Runner did not report direct output uploads.",
                            cold_start=cold_start,
                            timing_ms=timing,
                        )
                    output_manifest = output_manifest or []
                    timing["docker_export_copy_ms"] = 0
                    timing["output_validation_ms"] = 0
                    timing["output_upload_ms"] = 0
                else:
                    if not declares_outputs:
                        result_started = time.monotonic()
                        result = self._read_result(None, stdout)
                        record_step("result_read_ms", result_started)
                        output_manifest = []
                        timing["docker_export_copy_ms"] = 0
                        timing["output_validation_ms"] = 0
                        timing["output_upload_ms"] = 0
                    else:
                        export_started = time.monotonic()
                        self._copy_tmpfs_directory_from_container(
                            record.container,
                            "/sandbox/output",
                            output_dir,
                        )
                        record_step("docker_export_copy_ms", export_started)

                        effective_output_dir = self._effective_output_dir(output_dir)
                        result_started = time.monotonic()
                        result = self._read_result(effective_output_dir, stdout)
                        record_step("result_read_ms", result_started)
                        try:
                            validation_started = time.monotonic()
                            output_files = self._validate_declared_output_files(
                                job,
                                effective_output_dir,
                            )
                            record_step("output_validation_ms", validation_started)
                        except OutputValidationError as exc:
                            timing["executor_duration_ms"] = duration_ms
                            self._log_invocation_timing(job, timing)
                            return ExecutionResult(
                                status="failed",
                                result=result,
                                stdout=stdout,
                                stderr=stderr,
                                exit_code=exit_code,
                                duration_ms=duration_ms,
                                error_message=str(exc),
                                cold_start=cold_start,
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
                if not use_resident_runner:
                    cleanup_after_started = time.monotonic()
                    self._cleanup_warm_sandbox(record.container)
                    record_step(
                        "warm_sandbox_cleanup_after_ms",
                        cleanup_after_started,
                    )
                reusable = exit_code == 0
                timing["executor_duration_ms"] = duration_ms
                self._log_invocation_timing(job, timing)

                return ExecutionResult(
                    status=status,
                    result=result,
                    stdout=stdout,
                    stderr=stderr,
                    exit_code=exit_code,
                    duration_ms=duration_ms,
                    error_message=error_message,
                    cold_start=cold_start,
                    timing_ms=timing,
                    output_manifest=output_manifest,
                )
            finally:
                cleanup_started = time.monotonic()
                self.warm_pool.release(record, reusable=reusable)
                record_step("warm_pool_release_ms", cleanup_started)
                timing["executor_wall_with_cleanup_ms"] = int(
                    (time.monotonic() - started) * 1000
                )
                logger.info(
                    "invocation executor final timing request_id=%s timings=%s",
                    job["request_id"],
                    json.dumps(timing, sort_keys=True),
                )

    def _warm_container_key(
        self,
        job: dict,
        memory_mb: int,
        output_tmpfs_size_bytes: int,
        *,
        direct_output_upload: bool,
    ) -> WarmContainerKey:
        return WarmContainerKey(
            function_version_id=str(
                job.get("function_version_id")
                or job.get("version_id")
                or job.get("image_ref")
            ),
            image_ref=str(job["image_ref"]),
            handler=str(job.get("handler", "handler.main")),
            memory_mb=memory_mb,
            output_tmpfs_size_bytes=output_tmpfs_size_bytes,
            direct_output_upload_enabled=direct_output_upload,
        )

    def _create_warm_container(
        self,
        *,
        key: WarmContainerKey,
        image_ref: str,
        memory_mb: int,
        output_tmpfs_size_bytes: int,
        request_id: str,
        direct_output_upload: bool,
    ):
        if self.warm_pool is None:
            return None

        volume = self.docker_client.volumes.create(
            name=f"warm-{uuid.uuid4().hex[:24]}"
        )
        container = None
        try:
            resident = self.warm_resident_runner_enabled
            command = (
                ["/runner.py", "--serve"]
                if resident
                else [
                    "-c",
                    "import time; time.sleep(1000000000)",
                ]
            )
            entrypoint = ["python"]
            environment = {
                "FUNCTION_HANDLER": key.handler,
                "FUNCTION_OUTPUT_DIR": "/sandbox/output",
            }
            ports = None
            network_kwargs = self._container_network_kwargs(
                direct_output_upload=direct_output_upload
            )
            if resident:
                environment.update(
                    {
                        "FUNCTION_RESIDENT_RUNNER_HOST": "0.0.0.0",
                        "FUNCTION_RESIDENT_RUNNER_PORT": str(
                            self.warm_resident_runner_port
                        ),
                    }
                )
                ports = {
                    f"{self.warm_resident_runner_port}/tcp": ("127.0.0.1", None),
                }
                network_kwargs = self._resident_runner_network_kwargs()

            create_kwargs = {
                "detach": True,
                "entrypoint": entrypoint,
                "environment": environment,
                "labels": {
                    "serverless.worker.warm": "true",
                    "serverless.function_version_id": key.function_version_id,
                    "serverless.image_ref": key.image_ref,
                },
                "mem_limit": f"{memory_mb}m",
                "tmpfs": {
                    "/sandbox/output": f"size={output_tmpfs_size_bytes}",
                },
                "volumes": {volume.name: {"bind": "/sandbox", "mode": "rw"}},
                **network_kwargs,
            }
            if ports is not None:
                create_kwargs["ports"] = ports
            container = self.docker_client.containers.create(
                image_ref,
                command=command,
                **create_kwargs,
            )
            container.start()
            metadata = {}
            if resident:
                metadata["control_url"] = self._resident_runner_control_url(container)
                self._wait_for_resident_warm_runner(
                    metadata["control_url"],
                    timeout_seconds=self.warm_resident_runner_startup_timeout_seconds,
                )
            record = self.warm_pool.add_busy(
                key=key,
                container=container,
                volume=volume,
                metadata=metadata,
            )
            if record is None:
                return None
            return record
        except Exception:
            if container is not None:
                self._remove_container(container)
            self._remove_volume(volume)
            logger.exception(
                "failed to create warm container request_id=%s",
                request_id,
            )
            raise

    def _exec_runner_in_warm_container(
        self,
        container,
        *,
        job: dict,
        event: dict,
        input_files: list[dict[str, Any]],
        timeout_seconds: int,
    ) -> tuple[int | None, str, str]:
        environment = self._runner_environment(
            job,
            event,
            input_files,
            direct_output_upload=self._runner_direct_output_upload_enabled(job),
        )
        return self._exec_run_with_timeout(
            container,
            ["python", "/runner.py"],
            timeout_seconds=timeout_seconds,
            environment=environment,
        )

    def _prepare_resident_warm_runner(
        self,
        record,
        *,
        timeout_seconds: int,
    ) -> None:
        self._resident_runner_request(
            record,
            "/prepare",
            {},
            timeout_seconds=min(max(timeout_seconds, 1), 5),
        )

    def _invoke_resident_warm_runner(
        self,
        record,
        *,
        job: dict,
        event: dict,
        input_files: list[dict[str, Any]],
        timeout_seconds: int,
        direct_output_upload: bool,
    ) -> tuple[int | None, str, str]:
        environment = self._runner_environment(
            job,
            event,
            input_files,
            direct_output_upload=direct_output_upload,
        )
        try:
            payload = self._resident_runner_request(
                record,
                "/invoke",
                {
                    "request_id": job["request_id"],
                    "event": event,
                    "input_files": input_files,
                    "environment": environment,
                },
                timeout_seconds=timeout_seconds,
            )
        except Exception:
            try:
                record.container.kill()
            except Exception:
                pass
            raise

        stdout = self._resident_runner_stdout(payload)
        stderr = str(payload.get("stderr") or "")
        return payload.get("exit_code"), stdout, stderr

    def _resident_runner_stdout(self, payload: dict) -> str:
        stdout = str(payload.get("stdout") or "")
        result = payload.get("result", {})
        manifest = payload.get("output_manifest")
        timings = payload.get("timings", {})
        markers = [
            f"__FUNCTION_RESULT__={json.dumps(result)}",
        ]
        if manifest is not None:
            markers.append(
                f"__FUNCTION_OUTPUT_MANIFEST__={json.dumps(manifest, sort_keys=True)}"
            )
        markers.append(f"__FUNCTION_TIMING__={json.dumps(timings, sort_keys=True)}")
        return "\n".join([stdout.rstrip("\n"), *markers]).lstrip("\n") + "\n"

    def _resident_runner_request(
        self,
        record,
        path: str,
        payload: dict,
        *,
        timeout_seconds: int,
    ) -> dict:
        control_url = str(record.metadata.get("control_url") or "").rstrip("/")
        if not control_url:
            raise ExecutionError("Warm container has no resident runner control URL.")
        body = json.dumps(payload).encode("utf-8")
        request = urlrequest.Request(
            f"{control_url}{path}",
            data=body,
            method="POST",
            headers={"Content-Type": "application/json"},
        )
        try:
            with urlrequest.urlopen(request, timeout=timeout_seconds) as response:
                response_body = response.read().decode("utf-8")
        except urlerror.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise ExecutionError(
                f"Resident warm runner returned HTTP {exc.code}: {detail}"
            ) from exc
        except urlerror.URLError as exc:
            raise ExecutionError(f"Resident warm runner request failed: {exc}") from exc
        try:
            parsed = json.loads(response_body) if response_body else {}
        except json.JSONDecodeError as exc:
            raise ExecutionError("Resident warm runner returned invalid JSON.") from exc
        if not isinstance(parsed, dict):
            raise ExecutionError("Resident warm runner returned invalid response.")
        return parsed

    def _wait_for_resident_warm_runner(
        self,
        control_url: str,
        *,
        timeout_seconds: int,
    ) -> None:
        deadline = time.monotonic() + timeout_seconds
        health_url = f"{control_url.rstrip('/')}/health"
        last_error = None
        while time.monotonic() < deadline:
            try:
                with urlrequest.urlopen(health_url, timeout=0.25) as response:
                    if response.status == 200:
                        return
            except Exception as exc:
                last_error = exc
                time.sleep(0.05)
        raise ExecutionError(f"Resident warm runner did not become healthy: {last_error}")

    def _resident_runner_control_url(self, container) -> str:
        try:
            container.reload()
        except Exception:
            pass
        ip_address = self._container_network_ip(container)
        if ip_address:
            return f"http://{ip_address}:{self.warm_resident_runner_port}"
        return (
            "http://127.0.0.1:"
            f"{self._container_host_port(container, self.warm_resident_runner_port)}"
        )

    def _container_network_ip(self, container) -> str:
        networks = (
            getattr(container, "attrs", {})
            .get("NetworkSettings", {})
            .get("Networks", {})
        )
        if self.function_container_network:
            configured = networks.get(self.function_container_network) or {}
            if configured.get("IPAddress"):
                return configured["IPAddress"]
        for network in networks.values():
            if network.get("IPAddress"):
                return network["IPAddress"]
        return ""

    def _container_host_port(self, container, internal_port: int) -> int:
        try:
            container.reload()
        except Exception:
            pass
        ports = (
            getattr(container, "attrs", {})
            .get("NetworkSettings", {})
            .get("Ports", {})
        )
        bindings = ports.get(f"{internal_port}/tcp") or []
        if not bindings:
            raise ExecutionError("Warm container did not publish its control port.")
        return int(bindings[0]["HostPort"])

    def _exec_run_with_timeout(
        self,
        container,
        command: list[str],
        *,
        timeout_seconds: int,
        environment: dict[str, str] | None = None,
    ) -> tuple[int | None, str, str]:
        exec_instance = self.docker_client.api.exec_create(
            container.id,
            command,
            environment=environment,
        )
        exec_id = exec_instance["Id"]
        pool = ThreadPoolExecutor(max_workers=1)
        future = pool.submit(
            self.docker_client.api.exec_start,
            exec_id,
            demux=True,
        )
        try:
            output = future.result(timeout=timeout_seconds)
        except TimeoutError as exc:
            container.kill()
            future.cancel()
            raise ExecutionError(
                f"Function execution timed out after {timeout_seconds} seconds."
            ) from exc
        finally:
            pool.shutdown(wait=False, cancel_futures=True)
        stdout, stderr = self._decode_exec_output(output)
        inspect_result = self.docker_client.api.exec_inspect(exec_id)
        return inspect_result.get("ExitCode"), stdout, stderr

    def _decode_exec_output(self, output) -> tuple[str, str]:
        if isinstance(output, tuple):
            stdout, stderr = output
        else:
            stdout, stderr = output, b""
        return (
            self._decode_bytes(stdout),
            self._decode_bytes(stderr),
        )

    def _decode_bytes(self, value) -> str:
        if value is None:
            return ""
        if isinstance(value, str):
            return value
        return value.decode("utf-8", errors="replace")

    def _cleanup_warm_sandbox(self, container) -> None:
        result = container.exec_run(
            [
                "sh",
                "-c",
                (
                    "rm -rf /sandbox/input /sandbox/export; "
                    "mkdir -p /sandbox/input/files /sandbox/output; "
                    "find /sandbox/output -mindepth 1 -maxdepth 1 "
                    "-exec rm -rf -- {} +"
                ),
            ],
            demux=True,
        )
        if result.exit_code != 0:
            _, stderr = self._decode_exec_output(result.output)
            raise ExecutionError(
                f"Could not clean warm container sandbox: {stderr.strip()}"
            )

    def _log_invocation_timing(self, job: dict, timing: dict[str, int]) -> None:
        logger.info(
            "invocation executor timing request_id=%s timings=%s",
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

    def _read_result(self, output_dir: Path | None, stdout: str) -> dict:
        if output_dir is None:
            return self._read_result_from_stdout(stdout)
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
        for nested in (
            output_dir / "output",
            output_dir / "sandbox" / "output",
        ):
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

    def _runner_direct_output_upload_enabled(self, job: dict) -> bool:
        if not self.runner_direct_output_upload_enabled:
            return False
        if int(job.get("coordination_version", 1)) != 2:
            return False
        if self.backend_client is None:
            return False
        if not job.get("completion_id"):
            return False
        return True

    def _runner_command(self, job: dict, *, direct_output_upload: bool) -> str:
        if direct_output_upload or not self._declares_output_files(job):
            return "python /runner.py"
        return self._runner_export_command()

    def _declares_output_files(self, job: dict) -> bool:
        return bool(job.get("declared_output_files"))

    def _runner_environment(
        self,
        job: dict,
        event: dict,
        input_files: list[dict[str, Any]],
        *,
        direct_output_upload: bool,
    ) -> dict[str, str]:
        environment = {
            "FUNCTION_EVENT_PATH": "/sandbox/input/event.json",
            "FUNCTION_EVENT_JSON": json.dumps(event),
            "FUNCTION_INPUT_FILES_DIR": "/sandbox/input/files",
            "FUNCTION_INPUT_FILES_JSON": json.dumps(input_files),
            "FUNCTION_OUTPUT_DIR": "/sandbox/output",
            "FUNCTION_HANDLER": job.get("handler", "handler.main"),
            "FUNCTION_REQUEST_ID": job["request_id"],
        }
        if direct_output_upload:
            environment.update(self._runner_upload_environment(job))
        return environment

    def _runner_upload_environment(self, job: dict) -> dict[str, str]:
        declared = job.get("declared_output_files") or []
        max_files = self._positive_int(
            job.get("invocation_output_max_files"),
            default=len(declared),
        )
        return {
            "FUNCTION_OUTPUT_DIRECT_UPLOAD_ENABLED": "1",
            "FUNCTION_OUTPUT_UPLOAD_URL": (
                f"{self.runner_backend_base_url}/api/internal/invocations/"
                f"{job['request_id']}/runner-staged-outputs/"
            ),
            "FUNCTION_OUTPUT_UPLOAD_TOKEN": self._sign_runner_output_token(job),
            "FUNCTION_OUTPUT_UPLOAD_JOB_ID": str(job["job_id"]),
            "FUNCTION_OUTPUT_UPLOAD_DISPATCH_ATTEMPT": str(
                int(job.get("dispatch_attempt", 0))
            ),
            "FUNCTION_OUTPUT_UPLOAD_COMPLETION_ID": str(job["completion_id"]),
            "FUNCTION_DECLARED_OUTPUT_FILES": json.dumps(declared),
            "FUNCTION_OUTPUT_MAX_FILES": str(max_files),
            "FUNCTION_OUTPUT_MAX_FILE_SIZE_BYTES": str(
                self._megabytes_to_bytes(
                    job.get("invocation_output_max_file_size_mb"),
                    default_mb=10,
                )
            ),
            "FUNCTION_OUTPUT_MAX_TOTAL_SIZE_BYTES": str(
                self._output_tmpfs_size_bytes(job)
            ),
            "FUNCTION_OUTPUT_UPLOAD_TIMEOUT_SECONDS": str(
                self.runner_output_upload_timeout_seconds
            ),
        }

    def _sign_runner_output_token(self, job: dict) -> str:
        import base64
        import hashlib
        import hmac

        payload = {
            "request_id": str(job["request_id"]),
            "job_id": str(job["job_id"]),
            "dispatch_attempt": int(job.get("dispatch_attempt", 0)),
            "completion_id": str(job["completion_id"]),
            "exp": int(time.time()) + self.runner_output_upload_token_ttl_seconds,
        }
        payload_json = json.dumps(payload, separators=(",", ":"), sort_keys=True)
        payload_b64 = base64.urlsafe_b64encode(payload_json.encode("utf-8")).decode(
            "ascii"
        ).rstrip("=")
        signature = hmac.new(
            self.backend_client.token.encode("utf-8"),
            payload_b64.encode("ascii"),
            hashlib.sha256,
        ).hexdigest()
        return f"{payload_b64}.{signature}"

    def _container_network_kwargs(self, *, direct_output_upload: bool) -> dict[str, Any]:
        if not direct_output_upload:
            return {"network_disabled": True}
        kwargs: dict[str, Any] = {"network_disabled": False}
        if self.function_container_network:
            kwargs["network"] = self.function_container_network
        return kwargs

    def _resident_runner_network_kwargs(self) -> dict[str, Any]:
        kwargs: dict[str, Any] = {"network_disabled": False}
        if self.function_container_network:
            kwargs["network"] = self.function_container_network
        return kwargs

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

    def _read_runner_output_manifest(self, stdout: str) -> list[dict[str, Any]] | None:
        for line in reversed(stdout.splitlines()):
            if not line.startswith("__FUNCTION_OUTPUT_MANIFEST__="):
                continue
            payload = line.split("=", 1)[1]
            try:
                manifest = json.loads(payload)
            except json.JSONDecodeError:
                return None
            if isinstance(manifest, list):
                return manifest
            return None
        return None

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

    def _copy_tmpfs_directory_from_container(
        self,
        container,
        source_path: str,
        destination_dir: Path,
    ) -> None:
        script = (
            "import pathlib, sys, tarfile\n"
            "root = pathlib.Path(sys.argv[1])\n"
            "with tarfile.open(fileobj=sys.stdout.buffer, mode='w|') as archive:\n"
            "    if root.exists():\n"
            "        for path in sorted(root.rglob('*')):\n"
            "            archive.add(path, arcname=str(path.relative_to(root)))\n"
        )
        result = container.exec_run(
            ["python", "-c", script, source_path],
            demux=True,
        )
        stdout, stderr = result.output if isinstance(result.output, tuple) else (
            result.output,
            b"",
        )
        if result.exit_code != 0:
            detail = self._decode_bytes(stderr).strip()
            detail = detail or "could not export tmpfs output files"
            raise ExecutionError(detail)
        if not stdout:
            destination_dir.mkdir(parents=True, exist_ok=True)
            return
        self._extract_tar_archive(stdout or b"", destination_dir)

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

    def _env_bool(self, name: str, *, default: bool) -> bool:
        value = os.getenv(name)
        if value is None:
            return default
        return value.strip().lower() in {"1", "true", "yes", "on"}

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
