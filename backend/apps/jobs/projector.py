from __future__ import annotations

import json

import redis
from django.db import transaction
from django.utils import timezone

from apps.functions.models import BuildStatus
from apps.functions.services import sync_version_from_attempt
from apps.invocations.models import InvocationStatus

from .models import CoordinationVersion, Job, JobStatus


def apply_orchestrator_projection(fields: dict) -> bool:
    event_type = fields.get("event_type", "")
    state = json.loads(fields["payload"])
    job_id = str(state["job_id"])
    incoming_attempt = int(state.get("dispatch_attempt", 0))

    with transaction.atomic():
        job = (
            Job.objects.select_for_update()
            .filter(job_id=job_id, coordination_version=CoordinationVersion.V2)
            .first()
        )
        if job is None or incoming_attempt < job.dispatch_attempts:
            return False

        payload = dict(job.payload)
        if state.get("assigned_worker"):
            payload["assigned_worker"] = state["assigned_worker"]
        if state.get("worker_stream"):
            payload["worker_queue_name"] = state["worker_stream"]
        payload["dispatch_attempt"] = incoming_attempt
        if state.get("effective_image_ref"):
            payload["effective_image_ref"] = state["effective_image_ref"]

        job.dispatch_attempts = incoming_attempt
        job.payload = payload
        job.queue_name = state.get("worker_stream") or job.queue_name
        job.status = projected_job_status(event_type, state.get("status"))
        job.last_error = state.get("last_error", "")
        job.save(
            update_fields=[
                "dispatch_attempts",
                "payload",
                "queue_name",
                "status",
                "last_error",
                "updated_at",
            ]
        )

        if job.build_attempt_id:
            project_build(job, event_type, state)
        elif job.invocation_id:
            project_invocation(job, event_type)
    return True


def projected_job_status(event_type: str, state_status: str | None) -> str:
    mapping = {
        "job.dispatched": JobStatus.DISPATCHED,
        "job.running": JobStatus.RUNNING,
        "job.requeued": JobStatus.QUEUED,
        "job.succeeded": JobStatus.SUCCEEDED,
        "job.failed": JobStatus.FAILED,
        "job.cancelled": JobStatus.CANCELLED,
        "job.dead_lettered": JobStatus.DEAD_LETTERED,
    }
    return mapping.get(event_type, state_status or JobStatus.QUEUED)


def project_build(job: Job, event_type: str, state: dict) -> None:
    attempt = job.build_attempt
    completion = state.get("completion_payload") or {}
    if event_type == "job.running":
        attempt.status = BuildStatus.BUILDING
        attempt.started_at = attempt.started_at or timezone.now()
        attempt.log = "V2 orchestrator granted the worker lease."
    elif event_type == "job.requeued":
        attempt.status = BuildStatus.QUEUED
        attempt.log = state.get("last_error", "V2 build requeued.")
    elif event_type == "job.succeeded":
        attempt.status = BuildStatus.BUILT
        attempt.image_ref = completion.get("image_ref") or state.get(
            "artifact_commit_id",
            "",
        )
        attempt.log = completion.get("build_log", "Build completed.")
        attempt.finished_at = timezone.now()
    elif event_type in {"job.failed", "job.dead_lettered"}:
        attempt.status = BuildStatus.FAILED
        attempt.log = completion.get("build_log", state.get("last_error", "Build failed."))
        attempt.finished_at = timezone.now()
    else:
        return
    attempt.save()

    version = attempt.function_version
    if version.build_request_id == attempt.request_id:
        sync_version_from_attempt(version, attempt)


def project_invocation(job: Job, event_type: str) -> None:
    invocation = job.invocation
    if event_type == "job.running":
        invocation.status = InvocationStatus.RUNNING
        invocation.started_at = invocation.started_at or timezone.now()
        invocation.save(update_fields=["status", "started_at"])
    elif event_type == "job.requeued":
        invocation.status = InvocationStatus.QUEUED
        invocation.started_at = None
        invocation.save(update_fields=["status", "started_at"])
    elif event_type == "job.dead_lettered":
        invocation.status = InvocationStatus.FAILED
        invocation.finished_at = timezone.now()
        invocation.error_message = "Invocation exceeded V2 recovery attempts."
        invocation.save(update_fields=["status", "finished_at", "error_message"])


class OrchestratorProjector:
    def __init__(
        self,
        redis_client,
        *,
        stream: str = "orchestrator:v2:projections",
        group: str = "postgres-projector-v2",
        consumer: str = "projector",
    ):
        self.redis = redis_client
        self.stream = stream
        self.group = group
        self.consumer = consumer

    def ensure_group(self):
        try:
            self.redis.xgroup_create(self.stream, self.group, id="0-0", mkstream=True)
        except redis.ResponseError as exc:
            if "BUSYGROUP" not in str(exc):
                raise

    def process_once(self, *, block_ms: int = 1000, count: int = 20) -> int:
        batches = self.redis.xreadgroup(
            self.group,
            self.consumer,
            {self.stream: ">"},
            count=count,
            block=block_ms,
        )
        return self._apply_batches(batches)

    def reclaim_once(self, *, min_idle_ms: int = 30_000, count: int = 20) -> int:
        response = self.redis.xautoclaim(
            self.stream,
            self.group,
            self.consumer,
            min_idle_ms,
            "0-0",
            count=count,
        )
        messages = response[1] if len(response) > 1 else []
        return self._apply_batches([(self.stream, messages)])

    def _apply_batches(self, batches) -> int:
        processed = 0
        for _, messages in batches:
            for stream_id, fields in messages:
                apply_orchestrator_projection(fields)
                self.redis.xack(self.stream, self.group, stream_id)
                processed += 1
        return processed
