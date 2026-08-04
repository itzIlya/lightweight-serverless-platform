import json
import logging
import os
from pathlib import Path
import signal
import socket
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import UTC, datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from backend_client import BackendClient, BackendReportError
from builder import BuildCancelled, BuildError, DockerBuilder
from executor import DockerExecutor, ExecutionError, ExecutionResult
from orchestrator_client import OrchestratorClient, OrchestratorError
from scheduler.orchestrator_workers import WorkerOperationalStateStore


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("worker")

TERMINAL_JOB_STATUSES = {"succeeded", "failed", "cancelled"}
V2_WORKER_GROUP = "v2-workers"


class WorkerActivity:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._active_jobs = 0
        self._active_builds = 0
        self._active_invocations = 0

    def start(self, job_type: str) -> None:
        with self._lock:
            self._active_jobs += 1
            if job_type == "function.build":
                self._active_builds += 1
            elif job_type == "function.invoke":
                self._active_invocations += 1

    def finish(self, job_type: str) -> None:
        with self._lock:
            self._active_jobs = max(self._active_jobs - 1, 0)
            if job_type == "function.build":
                self._active_builds = max(self._active_builds - 1, 0)
            elif job_type == "function.invoke":
                self._active_invocations = max(self._active_invocations - 1, 0)

    def can_start_invocation(
        self,
        *,
        max_concurrency: int,
        max_invocation_concurrency: int,
    ) -> bool:
        with self._lock:
            return (
                self._active_jobs < max_concurrency
                and self._active_invocations < max_invocation_concurrency
            )

    def can_start_build(
        self,
        *,
        max_concurrency: int,
        max_build_concurrency: int,
    ) -> bool:
        with self._lock:
            return (
                self._active_jobs < max_concurrency
                and self._active_builds < max_build_concurrency
            )

    def snapshot(self) -> dict:
        with self._lock:
            return {
                "active_jobs": self._active_jobs,
                "active_builds": self._active_builds,
                "active_invocations": self._active_invocations,
            }

    def has_active_jobs(self) -> bool:
        with self._lock:
            return self._active_jobs > 0


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
    operational_store: WorkerOperationalStateStore | None = None,
    operational_payload: dict | None = None,
    warm_inventory_provider=None,
    status_provider=None,
) -> None:
    stop_event = stop_event or threading.Event()
    while not stop_event.wait(interval_seconds):
        state = activity.snapshot() if activity is not None else {}
        worker_status = status_provider() if status_provider is not None else "online"
        payload = dict(operational_payload or {})
        payload["status"] = worker_status
        metadata = dict(payload.get("metadata") or {})
        backend_metadata = {}
        if warm_inventory_provider is not None:
            try:
                warm_pool = warm_inventory_provider()
                metadata["warm_pool"] = warm_pool
                backend_metadata["warm_pool"] = warm_pool
            except Exception:
                logger.exception(
                    "failed to read warm container inventory name=%s",
                    worker_name,
                )
        if metadata:
            payload["metadata"] = metadata
        if operational_store is not None:
            try:
                operational_store.record_heartbeat(
                    {
                        **payload,
                        "name": worker_name,
                        "status": worker_status,
                        "active_jobs": state.get("active_jobs", 0),
                        "active_builds": state.get("active_builds", 0),
                        "active_invocations": state.get("active_invocations", 0),
                    }
                )
            except Exception:
                logger.exception(
                    "failed to record orchestrator heartbeat name=%s",
                    worker_name,
                )
        try:
            backend.heartbeat_worker(
                {
                    "name": worker_name,
                    "status": worker_status,
                    "active_jobs": state.get("active_jobs", 0),
                    "active_builds": state.get("active_builds", 0),
                    "active_invocations": state.get("active_invocations", 0),
                    "metadata": backend_metadata,
                }
            )
        except Exception:
            logger.exception("failed to send worker heartbeat name=%s", worker_name)


def warm_pool_heartbeat_metadata(executor: DockerExecutor) -> dict:
    if not executor.warm_enabled or executor.warm_pool is None:
        return {
            "enabled": False,
            "containers": [],
        }
    return {
        "enabled": True,
        "containers": executor.warm_pool.inventory(),
    }


def start_metrics_server(
    *,
    worker_name: str,
    activity: WorkerActivity,
    status_provider,
    warm_inventory_provider,
    port: int,
):
    if port <= 0:
        return None

    class WorkerMetricsHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == "/health/":
                return self.respond_text("worker_metrics_up 1\n", content_type="text/plain")
            if self.path != "/metrics/":
                self.send_response(404)
                self.end_headers()
                return
            body = worker_prometheus_metrics(
                worker_name=worker_name,
                status=status_provider(),
                activity=activity.snapshot(),
                warm_pool=warm_inventory_provider() or {},
            )
            return self.respond_text(body)

        def respond_text(self, body_text: str, *, content_type: str | None = None):
            body = body_text.encode("utf-8")
            self.send_response(200)
            self.send_header(
                "Content-Type",
                content_type or "text/plain; version=0.0.4; charset=utf-8",
            )
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, format, *args):
            logger.debug("worker metrics " + format, *args)

    server = ThreadingHTTPServer(("0.0.0.0", port), WorkerMetricsHandler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    logger.info("worker metrics server started worker=%s port=%s", worker_name, port)
    return server


def worker_prometheus_metrics(
    *,
    worker_name: str,
    status: str,
    activity: dict,
    warm_pool: dict,
) -> str:
    labels = {"worker": worker_name, "status": status}
    lines = [
        "# HELP serverless_worker_metrics_up Worker metrics endpoint availability.",
        "# TYPE serverless_worker_metrics_up gauge",
    ]
    emit_worker_metric(lines, "serverless_worker_metrics_up", 1, labels)
    emit_worker_metric(lines, "serverless_worker_active_jobs", activity.get("active_jobs", 0), labels)
    emit_worker_metric(
        lines,
        "serverless_worker_active_invocations",
        activity.get("active_invocations", 0),
        labels,
    )
    emit_worker_metric(
        lines,
        "serverless_worker_active_builds",
        activity.get("active_builds", 0),
        labels,
    )
    emit_worker_metric(
        lines,
        "serverless_worker_warm_pool_enabled",
        1 if warm_pool.get("enabled") else 0,
        labels,
    )
    for item in warm_pool.get("containers") or []:
        item_labels = {
            **labels,
            "function_version_id": item.get("function_version_id", ""),
            "handler": item.get("handler", ""),
        }
        emit_worker_metric(
            lines,
            "serverless_worker_warm_containers_idle",
            item.get("idle_count", 0),
            item_labels,
        )
        emit_worker_metric(
            lines,
            "serverless_worker_warm_containers_busy",
            item.get("busy_count", 0),
            item_labels,
        )
    return "\n".join(lines) + "\n"


def emit_worker_metric(
    lines: list[str],
    name: str,
    value,
    labels: dict[str, object],
) -> None:
    label_text = "{" + ",".join(
        f'{key}="{escape_metric_label(value)}"' for key, value in sorted(labels.items())
    ) + "}"
    lines.append(f"{name}{label_text} {float(value)}")


def escape_metric_label(value) -> str:
    return str(value).replace("\\", "\\\\").replace("\n", "\\n").replace('"', '\\"')


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


def ensure_v2_stream_group(client, stream_name: str) -> None:
    import redis

    try:
        client.xgroup_create(stream_name, V2_WORKER_GROUP, id="0-0", mkstream=True)
    except redis.ResponseError as exc:
        if "BUSYGROUP" not in str(exc):
            raise


def read_v2_stream_delivery(client, stream_name: str, consumer_name: str):
    messages = client.xreadgroup(
        V2_WORKER_GROUP,
        consumer_name,
        {stream_name: ">"},
        count=1,
        block=1,
    )
    if not messages:
        return None
    _, entries = messages[0]
    return entries[0] if entries else None


class LeaseRenewer:
    def __init__(
        self,
        orchestrator: OrchestratorClient,
        *,
        job_id: str,
        worker_name: str,
        dispatch_attempt: int,
        interval_seconds: float = 5,
    ):
        self.orchestrator = orchestrator
        self.job_id = job_id
        self.worker_name = worker_name
        self.dispatch_attempt = dispatch_attempt
        self.interval_seconds = interval_seconds
        self.stop_event = threading.Event()
        self.lost = threading.Event()
        self.thread = threading.Thread(target=self._run, daemon=True)

    def __enter__(self):
        self.thread.start()
        return self

    def __exit__(self, exc_type, exc, traceback):
        self.stop_event.set()
        self.thread.join(timeout=self.interval_seconds + 1)

    def _run(self):
        while not self.stop_event.wait(self.interval_seconds):
            try:
                response = self.orchestrator.renew_lease(
                    self.job_id,
                    {
                        "worker_name": self.worker_name,
                        "dispatch_attempt": self.dispatch_attempt,
                    },
                )
                if not response.get("accepted"):
                    self.lost.set()
                    return
            except OrchestratorError:
                logger.exception("could not renew V2 lease job_id=%s", self.job_id)
                self.lost.set()
                return


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


def move_next_job_to_processing_for_capacity(
    client,
    invocation_queue_name: str,
    build_queue_name: str,
    processing_queue_name: str,
    *,
    can_run_invocation: bool,
    can_run_build: bool,
):
    if can_run_invocation:
        delivery = move_job_to_processing_nowait(
            client,
            invocation_queue_name,
            processing_queue_name,
        )
        if delivery is not None:
            return delivery, invocation_queue_name

    if can_run_build:
        delivery = move_job_to_processing_nowait(
            client,
            build_queue_name,
            processing_queue_name,
        )
        if delivery is not None:
            return delivery, build_queue_name

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
    worker_started = time.monotonic()
    report_metadata = job_report_metadata(job)
    running_report_started = time.monotonic()
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
    running_report_ms = int((time.monotonic() - running_report_started) * 1000)

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

    final_report_started = time.monotonic()
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
    final_report_ms = int((time.monotonic() - final_report_started) * 1000)
    worker_total_ms = int((time.monotonic() - worker_started) * 1000)
    timing = dict(getattr(result, "timing_ms", {}) or {})
    timing.update(
        {
            "backend_running_report_ms": running_report_ms,
            "backend_final_report_ms": final_report_ms,
            "worker_process_total_ms": worker_total_ms,
        }
    )
    logger.info(
        "invocation worker timing request_id=%s timings=%s",
        request_id,
        json.dumps(timing, sort_keys=True),
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


def process_v2_build_job(
    job: dict,
    backend: BackendClient,
    builder: DockerBuilder,
    orchestrator: OrchestratorClient,
    *,
    worker_name: str,
) -> bool:
    job_id = job["job_id"]
    dispatch_attempt = int(job["dispatch_attempt"])
    build_request_id = job["build_request_id"]
    status = "failed"
    artifact_commit_id = ""
    completion_payload = {}

    try:
        if backend.is_build_cancel_requested(build_request_id):
            raise BuildCancelled("Build cancelled before execution.")
        with LeaseRenewer(
            orchestrator,
            job_id=job_id,
            worker_name=worker_name,
            dispatch_attempt=dispatch_attempt,
        ) as lease:
            with tempfile.TemporaryDirectory(prefix="build-source-") as root:
                source_bundle = Path(root) / "function.zip"
                backend.download_build_source(build_request_id, source_bundle)
                result = builder.build(
                    job,
                    source_bundle,
                    should_cancel=lambda: lease.lost.is_set()
                    or backend.is_build_cancel_requested(build_request_id),
                )
            if lease.lost.is_set():
                raise BuildError("V2 build lease was lost before completion.")
        status = "succeeded"
        artifact_commit_id = result.image_ref
        completion_payload = {
            "image_ref": result.image_ref,
            "build_log": result.build_log,
            "build_finished_at": utc_now(),
        }
    except (BuildCancelled, BuildError, BackendReportError) as exc:
        logger.exception("V2 build failed job_id=%s", job_id)
        completion_payload = {
            "build_log": str(exc),
            "build_finished_at": utc_now(),
        }

    response = orchestrator.complete_job(
        job_id,
        {
            "worker_name": worker_name,
            "dispatch_attempt": dispatch_attempt,
            "completion_id": f"{job_id}:{dispatch_attempt}:build",
            "status": status,
            "completion_payload": completion_payload,
            "artifact_commit_id": artifact_commit_id,
        },
    )
    return bool(response.get("completed"))


def process_v2_invocation_job(
    job: dict,
    backend: BackendClient,
    executor: DockerExecutor,
    orchestrator: OrchestratorClient,
    *,
    worker_name: str,
) -> bool:
    worker_started_ns = int(job.get("_v2_worker_started_ns") or time.monotonic_ns())
    job_id = job["job_id"]
    dispatch_attempt = int(job["dispatch_attempt"])
    request_id = job["request_id"]
    completion_id = f"{job_id}:{dispatch_attempt}:invocation"
    job["completion_id"] = completion_id
    failure_kind = ""
    try:
        with LeaseRenewer(
            orchestrator,
            job_id=job_id,
            worker_name=worker_name,
            dispatch_attempt=dispatch_attempt,
        ) as lease:
            result = executor.run(job)
            if lease.lost.is_set():
                return False
            failure_kind = classify_invocation_failure(result)
    except BackendReportError:
        logger.exception(
            "V2 invocation staged-output upload failed; leaving job recoverable job_id=%s",
            job_id,
        )
        return False
    except Exception as exc:
        if not isinstance(exc, ExecutionError):
            logger.exception("unexpected V2 invocation failure job_id=%s", job_id)
        failure_kind = "platform"
        if "timed out" in str(exc).lower():
            failure_kind = "timeout"
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

    terminal_status = "succeeded" if result.status == "succeeded" else "failed"
    completion_started = time.monotonic()
    response = orchestrator.complete_job(
        job_id,
        {
            "worker_name": worker_name,
            "dispatch_attempt": dispatch_attempt,
            "completion_id": completion_id,
            "status": terminal_status,
            "completion_payload": {
                "request_id": request_id,
                "status": result.status,
                "result": result.result,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "exit_code": result.exit_code,
                "cold_start": result.cold_start,
                "error_message": result.error_message,
                "failure_kind": failure_kind,
                "duration_ms": result.duration_ms,
                "finished_at": utc_now(),
                "output_manifest": result.output_manifest,
            },
            "artifact_commit_id": "",
        },
    )
    completion_ms = int((time.monotonic() - completion_started) * 1000)
    timing = dict(getattr(result, "timing_ms", {}) or {})
    timing.update(
        {
            "orchestrator_claim_ms": int(job.get("_v2_orchestrator_claim_ms", 0)),
            "orchestrator_completion_ms": completion_ms,
            "backend_running_report_ms": 0,
            "backend_final_report_ms": 0,
            "worker_process_total_ms": int(
                (time.monotonic_ns() - worker_started_ns) / 1_000_000
            ),
        }
    )
    logger.info(
        "invocation worker timing request_id=%s timings=%s",
        request_id,
        json.dumps(timing, sort_keys=True),
    )
    return bool(response.get("completed"))


def classify_invocation_failure(result: ExecutionResult) -> str:
    if result.status == "succeeded":
        return ""
    message = str(result.error_message or "").lower()
    if "timed out" in message:
        return "timeout"
    if "output" in message:
        return "output"
    if result.exit_code is not None:
        return "function"
    return "platform"


def run_claimed_job(
    *,
    job: dict,
    backend: BackendClient,
    redis_client,
    processing_queue_name: str,
    delivery_message: str,
    source_queue_name: str,
    worker_name: str,
    hostname: str,
    max_build_concurrency: int,
    activity: WorkerActivity,
    executor_factory=DockerExecutor,
    builder_factory=DockerBuilder,
) -> None:
    job_type = job.get("type")
    try:
        if job_type == "function.invoke":
            logger.info(
                "received invocation job request_id=%s function=%s version=%s",
                job.get("request_id"),
                job.get("function_slug"),
                job.get("version"),
            )
            process_invocation_job(
                job,
                backend,
                executor_factory(backend_client=backend),
            )
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
                builder_factory(),
                worker_name=worker_name,
                hostname=hostname,
                max_build_concurrency=max_build_concurrency,
                requeue=lambda: redis_client.rpush(source_queue_name, delivery_message),
            )
        else:
            logger.error("discarding unknown job type: %s", job_type)
    except Exception:
        logger.exception("unexpected threaded job failure type=%s", job_type)
    finally:
        acknowledge_processing_job(redis_client, processing_queue_name, delivery_message)
        activity.finish(job_type)
        logger.info("job complete type=%s", job_type)


def run_v2_claimed_job(
    *,
    job: dict,
    backend: BackendClient,
    orchestrator: OrchestratorClient,
    worker_name: str,
    activity: WorkerActivity,
    executor_factory=DockerExecutor,
    builder_factory=DockerBuilder,
) -> None:
    job_type = job.get("type")
    try:
        if job_type == "function.build":
            process_v2_build_job(
                job,
                backend,
                builder_factory(),
                orchestrator,
                worker_name=worker_name,
            )
        elif job_type == "function.invoke":
            process_v2_invocation_job(
                job,
                backend,
                executor_factory(backend_client=backend),
                orchestrator,
                worker_name=worker_name,
            )
        else:
            logger.error("discarding unknown V2 job type: %s", job_type)
    except Exception:
        logger.exception("unexpected V2 threaded job failure type=%s", job_type)
    finally:
        activity.finish(job_type)
        logger.info("V2 job processing ended type=%s job_id=%s", job_type, job.get("job_id"))


def main() -> None:
    import redis

    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    backend_base_url = os.getenv("BACKEND_BASE_URL", "http://backend:8000")
    orchestrator_base_url = os.getenv(
        "ORCHESTRATOR_BASE_URL",
        "http://orchestrator:8010",
    )
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
    v2_invocation_stream = f"worker:{worker_name}:v2:invocations"
    v2_build_stream = f"worker:{worker_name}:v2:builds"
    max_concurrency = int(os.getenv("WORKER_MAX_CONCURRENCY", "1"))
    max_invocation_concurrency = int(
        os.getenv("WORKER_MAX_INVOCATION_CONCURRENCY", str(max_concurrency))
    )
    max_build_concurrency = int(os.getenv("WORKER_MAX_BUILD_CONCURRENCY", "1"))
    heartbeat_interval_seconds = float(os.getenv("WORKER_HEARTBEAT_SECONDS", "10"))
    worker_stale_after_seconds = float(
        os.getenv(
            "ORCHESTRATOR_WORKER_STALE_AFTER_SECONDS",
            str(heartbeat_interval_seconds * 3),
        )
    )
    idle_sleep_seconds = float(os.getenv("WORKER_IDLE_SLEEP_SECONDS", "0.2"))
    metrics_port = int(os.getenv("WORKER_METRICS_PORT", "9102"))

    client = redis.Redis.from_url(redis_url, decode_responses=True)
    backend = BackendClient(backend_base_url, worker_token)
    orchestrator = OrchestratorClient(orchestrator_base_url, worker_token)
    invocation_executor = DockerExecutor(backend_client=backend)
    invocation_executor_factory = lambda backend_client=None: invocation_executor
    activity = WorkerActivity()
    shutdown_event = threading.Event()
    heartbeat_stop_event = threading.Event()
    hostname = socket.gethostname()
    operational_payload = {
        "name": worker_name,
        "hostname": hostname,
        "max_concurrency": max_concurrency,
        "max_build_concurrency": max_build_concurrency,
        "max_invocation_concurrency": max_invocation_concurrency,
        "queue_name": legacy_queue_name,
        "invocation_queue_name": invocation_queue_name,
        "build_queue_name": build_queue_name,
        "processing_queue_name": processing_queue_name,
        "metadata": {"legacy_queue_name": legacy_queue_name},
    }
    worker_state = WorkerOperationalStateStore(
        client,
        lease_ttl_ms=max(int(worker_stale_after_seconds * 1000), 1000),
    )

    def worker_status() -> str:
        return "draining" if shutdown_event.is_set() else "online"

    def request_shutdown(signum, _frame) -> None:
        if not shutdown_event.is_set():
            logger.info(
                "worker shutdown requested signal=%s; entering drain mode worker=%s",
                signum,
                worker_name,
            )
        shutdown_event.set()

    for signum in (signal.SIGTERM, signal.SIGINT):
        try:
            signal.signal(signum, request_shutdown)
        except (ValueError, OSError):
            logger.debug("could not install signal handler signum=%s", signum)

    ensure_v2_stream_group(client, v2_invocation_stream)
    ensure_v2_stream_group(client, v2_build_stream)

    try:
        worker_state.record_heartbeat(operational_payload)
    except Exception:
        logger.exception(
            "failed to register worker with orchestrator state name=%s",
            worker_name,
        )

    try:
        backend.register_worker(
            {
                "name": worker_name,
                "hostname": hostname,
                "max_concurrency": max_concurrency,
                "max_build_concurrency": max_build_concurrency,
                "metadata": {
                    "legacy_queue_name": legacy_queue_name,
                    "max_invocation_concurrency": max_invocation_concurrency,
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
            "stop_event": heartbeat_stop_event,
            "operational_store": worker_state,
            "operational_payload": operational_payload,
            "warm_inventory_provider": (
                lambda: warm_pool_heartbeat_metadata(invocation_executor)
            ),
            "status_provider": worker_status,
        },
        daemon=True,
    ).start()
    start_metrics_server(
        worker_name=worker_name,
        activity=activity,
        status_provider=worker_status,
        warm_inventory_provider=lambda: warm_pool_heartbeat_metadata(invocation_executor),
        port=metrics_port,
    )

    logger.info(
        (
            "worker started; worker=%s invocation_queue=%s build_queue=%s "
            "processing_queue=%s max_concurrency=%s max_invocation_concurrency=%s "
            "max_build_concurrency=%s warm_containers=%s"
        ),
        worker_name,
        invocation_queue_name,
        build_queue_name,
        processing_queue_name,
        max_concurrency,
        max_invocation_concurrency,
        max_build_concurrency,
        invocation_executor.warm_enabled,
    )

    with ThreadPoolExecutor(max_workers=max_concurrency) as pool:
        while not shutdown_event.is_set() or activity.has_active_jobs():
            if shutdown_event.is_set():
                time.sleep(idle_sleep_seconds)
                continue
            can_run_invocation = activity.can_start_invocation(
                max_concurrency=max_concurrency,
                max_invocation_concurrency=max_invocation_concurrency,
            )
            can_run_build = activity.can_start_build(
                max_concurrency=max_concurrency,
                max_build_concurrency=max_build_concurrency,
            )
            v2_delivery = None
            delivery_message = None
            source_queue_name = None
            if can_run_invocation:
                v2_delivery = read_v2_stream_delivery(
                    client,
                    v2_invocation_stream,
                    worker_name,
                )
                if v2_delivery is None:
                    delivery_message = move_job_to_processing_nowait(
                        client,
                        invocation_queue_name,
                        processing_queue_name,
                    )
                    if delivery_message is not None:
                        source_queue_name = invocation_queue_name
            if v2_delivery is None and delivery_message is None and can_run_build:
                v2_delivery = read_v2_stream_delivery(
                    client,
                    v2_build_stream,
                    worker_name,
                )
                if v2_delivery is None:
                    delivery_message = move_job_to_processing_nowait(
                        client,
                        build_queue_name,
                        processing_queue_name,
                    )
                    if delivery_message is not None:
                        source_queue_name = build_queue_name

            if v2_delivery is not None:
                stream_id, delivery = v2_delivery
                job_id = delivery.get("job_id", "")
                v2_worker_started_ns = time.monotonic_ns()
                claim_started = time.monotonic()
                try:
                    claim = orchestrator.claim_job(
                        job_id,
                        {
                            "worker_name": worker_name,
                            "dispatch_attempt": int(delivery.get("dispatch_attempt", 0)),
                        },
                    )
                except OrchestratorError:
                    logger.exception("could not claim V2 job job_id=%s", job_id)
                    time.sleep(idle_sleep_seconds)
                    continue
                claim_ms = int((time.monotonic() - claim_started) * 1000)
                if not claim.get("claimed"):
                    client.xack(
                        v2_invocation_stream
                        if delivery.get("job_type") == "invocation"
                        else v2_build_stream,
                        V2_WORKER_GROUP,
                        stream_id,
                    )
                    continue
                job = dict(claim.get("payload") or {})
                job["_v2_worker_started_ns"] = v2_worker_started_ns
                job["_v2_orchestrator_claim_ms"] = claim_ms
                job_type = job.get("type")
                if job_type not in {"function.invoke", "function.build"}:
                    logger.error("discarding unknown claimed V2 job type=%s", job_type)
                    continue
                activity.start(job_type)
                pool.submit(
                    run_v2_claimed_job,
                    job=job,
                    backend=backend,
                    orchestrator=orchestrator,
                    worker_name=worker_name,
                    activity=activity,
                    executor_factory=invocation_executor_factory,
                )
                continue

            if delivery_message is None:
                time.sleep(idle_sleep_seconds)
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
            if job_type not in {"function.invoke", "function.build"}:
                logger.error("discarding unknown job type: %s", job_type)
                acknowledge_processing_job(
                    client,
                    processing_queue_name,
                    delivery_message,
                )
                continue

            activity.start(job_type)
            pool.submit(
                run_claimed_job,
                job=job,
                backend=backend,
                redis_client=client,
                processing_queue_name=processing_queue_name,
                delivery_message=delivery_message,
                source_queue_name=source_queue_name,
                worker_name=worker_name,
                hostname=hostname,
                max_build_concurrency=max_build_concurrency,
                activity=activity,
                executor_factory=invocation_executor_factory,
            )

    heartbeat_stop_event.set()
    try:
        worker_state.record_heartbeat(
            {
                **operational_payload,
                "status": "offline",
                "active_jobs": 0,
                "active_builds": 0,
                "active_invocations": 0,
            }
        )
    except Exception:
        logger.exception("failed to mark worker offline in orchestrator state")
    try:
        backend.heartbeat_worker(
            {
                "name": worker_name,
                "status": "offline",
                "active_jobs": 0,
                "active_builds": 0,
                "active_invocations": 0,
                "metadata": {},
            }
        )
    except Exception:
        logger.exception("failed to mark worker offline in backend projection")


if __name__ == "__main__":
    main()
