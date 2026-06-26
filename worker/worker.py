import json
import logging
import os
from pathlib import Path
import socket
import tempfile
import threading
import time
from datetime import UTC, datetime

from backend_client import BackendClient, BackendReportError
from builder import BuildCancelled, BuildError, DockerBuilder
from executor import DockerExecutor, ExecutionError, ExecutionResult


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("worker")

TERMINAL_JOB_STATUSES = {"succeeded", "failed", "cancelled"}


class WorkerActivity:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._active_jobs = 0
        self._active_builds = 0

    def start(self, job_type: str) -> None:
        with self._lock:
            self._active_jobs += 1
            if job_type == "function.build":
                self._active_builds += 1

    def finish(self, job_type: str) -> None:
        with self._lock:
            self._active_jobs = max(self._active_jobs - 1, 0)
            if job_type == "function.build":
                self._active_builds = max(self._active_builds - 1, 0)

    def snapshot(self) -> dict:
        with self._lock:
            return {
                "active_jobs": self._active_jobs,
                "active_builds": self._active_builds,
            }


def utc_now() -> str:
    return datetime.now(UTC).isoformat()


def report_invocation_safely(
    backend: BackendClient,
    request_id: str,
    payload: dict,
) -> None:
    try:
        backend.report_invocation(request_id, payload)
    except BackendReportError:
        logger.exception("failed to report invocation status request_id=%s", request_id)


def report_build_safely(
    backend: BackendClient,
    build_request_id: str,
    payload: dict,
) -> None:
    try:
        backend.report_build(build_request_id, payload)
    except BackendReportError:
        logger.exception(
            "failed to report build status build_request_id=%s",
            build_request_id,
        )


def heartbeat_loop(
    backend: BackendClient,
    *,
    worker_name: str,
    interval_seconds: float,
    activity: WorkerActivity | None = None,
    stop_event: threading.Event | None = None,
) -> None:
    stop_event = stop_event or threading.Event()
    while not stop_event.wait(interval_seconds):
        try:
            state = activity.snapshot() if activity is not None else {}
            backend.heartbeat_worker(
                {
                    "name": worker_name,
                    "active_jobs": state.get("active_jobs", 0),
                    "active_builds": state.get("active_builds", 0),
                }
            )
        except BackendReportError:
            logger.exception("failed to send worker heartbeat name=%s", worker_name)


def worker_processing_queue_name(worker_queue_name: str) -> str:
    parts = worker_queue_name.split(":")
    if len(parts) >= 3 and parts[-1] in {"invocations", "builds", "jobs"}:
        return ":".join(parts[:-1] + ["processing"])
    if worker_queue_name.endswith(":jobs"):
        return f"{worker_queue_name[:-5]}:processing"
    return f"{worker_queue_name}:processing"


def move_job_to_processing(client, queue_name: str, processing_queue_name: str):
    return client.execute_command(
        "BLMOVE",
        queue_name,
        processing_queue_name,
        "LEFT",
        "RIGHT",
        5,
    )


def move_job_to_processing_nowait(client, queue_name: str, processing_queue_name: str):
    return client.execute_command(
        "LMOVE",
        queue_name,
        processing_queue_name,
        "LEFT",
        "RIGHT",
    )


def move_next_job_to_processing(
    client,
    invocation_queue_name: str,
    build_queue_name: str,
    processing_queue_name: str,
):
    delivery = move_job_to_processing_nowait(
        client,
        invocation_queue_name,
        processing_queue_name,
    )
    if delivery is not None:
        return delivery, invocation_queue_name

    delivery = move_job_to_processing_nowait(
        client,
        build_queue_name,
        processing_queue_name,
    )
    if delivery is not None:
        return delivery, build_queue_name

    delivery = move_job_to_processing(
        client,
        invocation_queue_name,
        processing_queue_name,
    )
    if delivery is not None:
        return delivery, invocation_queue_name
    return None, None


def acknowledge_processing_job(client, processing_queue_name: str, job_id: str) -> None:
    client.lrem(processing_queue_name, 1, job_id)


def parse_delivery_message(message: str) -> dict:
    try:
        payload = json.loads(message)
    except json.JSONDecodeError:
        return {"job_id": message, "dispatch_attempt": None}
    if isinstance(payload, dict) and payload.get("job_id"):
        return {
            "job_id": str(payload["job_id"]),
            "dispatch_attempt": payload.get("dispatch_attempt"),
        }
    return {"job_id": message, "dispatch_attempt": None}


def claim_job_for_execution(
    backend: BackendClient,
    *,
    job_id: str,
    worker_name: str,
    dispatch_attempt,
) -> dict | None:
    if dispatch_attempt in ("", None):
        logger.info("rejecting delivery without dispatch attempt job_id=%s", job_id)
        return None

    claim = backend.claim_job(
        job_id,
        {
            "worker_name": worker_name,
            "dispatch_attempt": dispatch_attempt,
        },
    )
    if not claim.get("claimed"):
        logger.info(
            "skipping unclaimed job job_id=%s status=%s stale=%s terminal=%s",
            job_id,
            claim.get("status"),
            claim.get("stale"),
            claim.get("terminal"),
        )
        return None
    job = claim["job"]
    if job.get("status") in TERMINAL_JOB_STATUSES:
        logger.info(
            "acknowledging terminal job without execution job_id=%s status=%s",
            job_id,
            job.get("status"),
        )
        return None
    return dict(job.get("payload") or {})


def job_report_metadata(job: dict) -> dict:
    metadata = {
        "job_id": job.get("job_id"),
        "dispatch_attempt": job.get("dispatch_attempt"),
        "worker_name": job.get("assigned_worker"),
    }
    return {key: value for key, value in metadata.items() if value not in ("", None)}


def process_invocation_job(
    job: dict,
    backend: BackendClient,
    executor: DockerExecutor,
) -> None:
    request_id = job["request_id"]
    started_at = utc_now()
    report_metadata = job_report_metadata(job)
    report_invocation_safely(
        backend,
        request_id,
        {
            **report_metadata,
            "status": "running",
            "started_at": started_at,
            "cold_start": True,
        },
    )

    try:
        result = executor.run(job)
    except ExecutionError as exc:
        result = ExecutionResult(
            status="failed",
            result={},
            stdout="",
            stderr="",
            exit_code=None,
            duration_ms=0,
            error_message=str(exc),
            cold_start=True,
        )
    except Exception as exc:
        logger.exception("unexpected worker failure request_id=%s", request_id)
        result = ExecutionResult(
            status="failed",
            result={},
            stdout="",
            stderr="",
            exit_code=None,
            duration_ms=0,
            error_message=f"Unexpected worker failure: {exc}",
            cold_start=True,
        )

    report_invocation_safely(
        backend,
        request_id,
        {
            **report_metadata,
            "status": result.status,
            "result": result.result,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.exit_code,
            "cold_start": result.cold_start,
            "error_message": result.error_message,
            "duration_ms": result.duration_ms,
            "finished_at": utc_now(),
        },
    )


def process_build_job(
    job: dict,
    backend: BackendClient,
    builder: DockerBuilder,
    *,
    worker_name: str = "",
    hostname: str = "",
    max_build_concurrency: int = 1,
    requeue=None,
) -> None:
    build_request_id = job["build_request_id"]
    report_metadata = job_report_metadata(job)
    try:
        if backend.is_build_cancel_requested(build_request_id):
            report_build_safely(
                backend,
                build_request_id,
                {
                    **report_metadata,
                    "status": "cancelled",
                    "build_log": "Build cancelled before execution.",
                    "build_finished_at": utc_now(),
                },
            )
            return
    except BackendReportError:
        logger.exception(
            "could not read build state build_request_id=%s",
            build_request_id,
        )
        return

    lease_id = None
    try:
        lease = backend.acquire_build_lease(
            build_request_id,
            {
                "worker_name": worker_name or hostname or "worker",
                "hostname": hostname or worker_name or "worker",
                "max_build_concurrency": max_build_concurrency,
            },
        )
    except BackendReportError:
        logger.exception(
            "could not acquire build lease build_request_id=%s",
            build_request_id,
        )
        if requeue is not None:
            requeue()
        return

    if not lease.get("granted"):
        logger.info(
            "build lease denied build_request_id=%s reason=%s",
            build_request_id,
            lease.get("reason", ""),
        )
        if requeue is not None:
            requeue()
        return

    lease_id = lease.get("lease_id")
    report_build_safely(
        backend,
        build_request_id,
        {
            **report_metadata,
            "status": "building",
            "build_log": "Worker started build.",
            "build_started_at": utc_now(),
        },
    )

    try:
        with tempfile.TemporaryDirectory(prefix="build-source-") as root:
            source_bundle = Path(root) / "function.zip"
            backend.download_build_source(build_request_id, source_bundle)
            result = builder.build(
                job,
                source_bundle,
                should_cancel=lambda: backend.is_build_cancel_requested(
                    build_request_id
                ),
            )
    except BuildCancelled as exc:
        logger.info("build cancelled build_request_id=%s", build_request_id)
        report_build_safely(
            backend,
            build_request_id,
            {
                **report_metadata,
                "status": "cancelled",
                "build_log": str(exc),
                "build_finished_at": utc_now(),
            },
        )
        return
    except (BuildError, BackendReportError) as exc:
        logger.exception("build failed build_request_id=%s", build_request_id)
        report_build_safely(
            backend,
            build_request_id,
            {
                **report_metadata,
                "status": "failed",
                "build_log": str(exc),
                "build_finished_at": utc_now(),
            },
        )
        return
    except Exception as exc:
        logger.exception(
            "unexpected build failure build_request_id=%s",
            build_request_id,
        )
        report_build_safely(
            backend,
            build_request_id,
            {
                **report_metadata,
                "status": "failed",
                "build_log": f"Unexpected worker failure: {exc}",
                "build_finished_at": utc_now(),
            },
        )
        return
    finally:
        if lease_id is not None:
            try:
                backend.release_build_lease(
                    build_request_id,
                    {
                        "lease_id": lease_id,
                        "reason": "Worker finished build processing.",
                    },
                )
            except BackendReportError:
                logger.exception(
                    "failed to release build lease build_request_id=%s lease_id=%s",
                    build_request_id,
                    lease_id,
                )

    report_build_safely(
        backend,
        build_request_id,
        {
            **report_metadata,
            "status": "built",
            "image_ref": result.image_ref,
            "build_log": result.build_log,
            "build_finished_at": utc_now(),
        },
    )


def main() -> None:
    import redis

    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    backend_base_url = os.getenv("BACKEND_BASE_URL", "http://backend:8000")
    worker_token = os.getenv("WORKER_SHARED_SECRET", "change-me")
    worker_name = os.getenv("WORKER_NAME", socket.gethostname())
    worker_queue_prefix = os.getenv("WORKER_QUEUE_PREFIX", "worker")
    invocation_queue_name = os.getenv(
        "WORKER_INVOCATION_QUEUE_NAME",
        f"{worker_queue_prefix}:{worker_name}:invocations",
    )
    build_queue_name = os.getenv(
        "WORKER_BUILD_QUEUE_NAME",
        f"{worker_queue_prefix}:{worker_name}:builds",
    )
    legacy_queue_name = os.getenv(
        "WORKER_QUEUE_NAME",
        f"{worker_queue_prefix}:{worker_name}:jobs",
    )
    processing_queue_name = os.getenv(
        "WORKER_PROCESSING_QUEUE_NAME",
        worker_processing_queue_name(invocation_queue_name),
    )
    max_concurrency = int(os.getenv("WORKER_MAX_CONCURRENCY", "1"))
    max_build_concurrency = int(os.getenv("WORKER_MAX_BUILD_CONCURRENCY", "1"))
    heartbeat_interval_seconds = float(os.getenv("WORKER_HEARTBEAT_SECONDS", "10"))

    client = redis.Redis.from_url(redis_url, decode_responses=True)
    backend = BackendClient(backend_base_url, worker_token)
    executor = DockerExecutor(backend_client=backend)
    builder = DockerBuilder()
    activity = WorkerActivity()

    try:
        backend.register_worker(
            {
                "name": worker_name,
                "hostname": socket.gethostname(),
            "max_concurrency": max_concurrency,
            "max_build_concurrency": max_build_concurrency,
            "metadata": {
                "legacy_queue_name": legacy_queue_name,
            },
        }
    )
    except BackendReportError:
        logger.exception("failed to register worker name=%s", worker_name)

    threading.Thread(
        target=heartbeat_loop,
        kwargs={
            "backend": backend,
            "worker_name": worker_name,
            "interval_seconds": heartbeat_interval_seconds,
            "activity": activity,
        },
        daemon=True,
    ).start()

    logger.info(
        "worker started; worker=%s invocation_queue=%s build_queue=%s processing_queue=%s",
        worker_name,
        invocation_queue_name,
        build_queue_name,
        processing_queue_name,
    )

    while True:
        delivery_message, source_queue_name = move_next_job_to_processing(
            client,
            invocation_queue_name,
            build_queue_name,
            processing_queue_name,
        )
        if delivery_message is None:
            continue

        delivery = parse_delivery_message(delivery_message)
        job_id = delivery["job_id"]
        try:
            job = claim_job_for_execution(
                backend,
                job_id=job_id,
                worker_name=worker_name,
                dispatch_attempt=delivery.get("dispatch_attempt"),
            )
        except BackendReportError:
            logger.exception("could not claim job job_id=%s", job_id)
            continue

        if job is None:
            acknowledge_processing_job(
                client,
                processing_queue_name,
                delivery_message,
            )
            continue

        job_type = job.get("type")
        activity.start(job_type)
        try:
            if job_type == "function.invoke":
                logger.info(
                    "received invocation job request_id=%s function=%s version=%s",
                    job.get("request_id"),
                    job.get("function_slug"),
                    job.get("version"),
                )
                process_invocation_job(job, backend, executor)
            elif job_type == "function.build":
                logger.info(
                    "received build job build_request_id=%s function=%s version=%s",
                    job.get("build_request_id"),
                    job.get("function_slug"),
                    job.get("version"),
                )
                process_build_job(
                    job,
                    backend,
                    builder,
                    worker_name=worker_name,
                    hostname=socket.gethostname(),
                    max_build_concurrency=max_build_concurrency,
                    requeue=lambda: client.rpush(source_queue_name, delivery_message),
                )
            else:
                logger.error("discarding unknown job type: %s", job_type)
                acknowledge_processing_job(
                    client,
                    processing_queue_name,
                    delivery_message,
                )
                continue
        finally:
            activity.finish(job_type)

        acknowledge_processing_job(client, processing_queue_name, delivery_message)
        logger.info("job complete type=%s", job_type)


if __name__ == "__main__":
    main()
