from __future__ import annotations

import hashlib

from django.conf import settings
from django.db import transaction

from apps.functions.models import BuildStatus
from apps.invocations.models import InvocationStatus
from apps.workers.models import WorkerStatus

from .models import CoordinationVersion, Job, JobStatus, JobType, OutboxEvent


CUTOVER_STAGES = {
    "internal": 1,
    "builds": 2,
    "private": 3,
    "token": 4,
    "public": 5,
    "all": 6,
}


def max_recovery_attempts_for_type(job_type: str) -> int:
    if job_type == JobType.INVOCATION:
        return int(settings.JOB_RECOVERY_MAX_ATTEMPTS_INVOCATION)
    return int(settings.JOB_RECOVERY_MAX_ATTEMPTS_BUILD)


def recovery_backoff_seconds(job_type: str, recovery_count: int) -> int:
    values = _recovery_backoff_values(job_type)
    if not values:
        return 0
    index = max(int(recovery_count), 1) - 1
    if index >= len(values):
        return values[-1]
    return values[index]


def _recovery_backoff_values(job_type: str) -> list[int]:
    raw = (
        settings.JOB_RECOVERY_BACKOFF_SECONDS_INVOCATION
        if job_type == JobType.INVOCATION
        else settings.JOB_RECOVERY_BACKOFF_SECONDS_BUILD
    )
    values: list[int] = []
    for item in str(raw).split(","):
        item = item.strip()
        if not item:
            continue
        values.append(max(int(item), 0))
    return values


def create_build_job_record(
    build_attempt,
    payload: dict,
    *,
    coordination_version: int | None = None,
) -> Job:
    coordination_version = coordination_version or coordination_version_for_job(
        JobType.BUILD,
        build_attempt.request_id,
        function_id=build_attempt.function_version.function_id,
    )
    with transaction.atomic():
        job = Job.objects.create(
            type=JobType.BUILD,
            status=JobStatus.QUEUED,
            queue_name=scheduler_queue_name_for_type(JobType.BUILD),
            payload=payload,
            build_attempt=build_attempt,
            available_at=build_attempt.queued_at,
            max_recovery_attempts=max_recovery_attempts_for_type(JobType.BUILD),
            coordination_version=coordination_version,
        )
        return _finish_job_creation(job, payload)


def create_invocation_job_record(
    invocation,
    payload: dict,
    *,
    coordination_version: int | None = None,
) -> Job:
    coordination_version = coordination_version or coordination_version_for_job(
        JobType.INVOCATION,
        invocation.request_id,
        function_id=invocation.function_version.function_id,
        invoke_access=invocation.function_version.function.invoke_access,
    )
    with transaction.atomic():
        job = Job.objects.create(
            type=JobType.INVOCATION,
            status=JobStatus.QUEUED,
            queue_name=scheduler_queue_name_for_type(JobType.INVOCATION),
            payload=payload,
            invocation=invocation,
            available_at=invocation.queued_at,
            max_recovery_attempts=max_recovery_attempts_for_type(JobType.INVOCATION),
            coordination_version=coordination_version,
        )
        return _finish_job_creation(job, payload)


def _finish_job_creation(job: Job, payload: dict) -> Job:
    payload["job_id"] = str(job.job_id)
    job.payload = payload
    job.save(update_fields=["payload", "updated_at"])
    OutboxEvent.objects.create(
        aggregate_id=job.job_id,
        event_type="job.created",
        payload={
            "job_id": str(job.job_id),
            "job_type": job.type,
            "coordination_version": job.coordination_version,
            "status": job.status,
            "queue_name": job.queue_name,
            "available_at": job.available_at.isoformat(),
            "dispatch_attempts": job.dispatch_attempts,
            "recovery_count": job.recovery_count,
            "max_recovery_attempts": job.max_recovery_attempts,
            "payload": job.payload,
        },
    )
    return job


def coordination_version_for_job(
    job_type: str,
    routing_key,
    *,
    function_id: int | None = None,
    invoke_access: str | None = None,
) -> int:
    if job_type == JobType.BUILD:
        enabled = settings.V2_BUILD_PILOT_ENABLED
        percentage = settings.V2_BUILD_ROLLOUT_PERCENT
        canaries = settings.V2_BUILD_CANARY_FUNCTION_IDS
    else:
        enabled = settings.V2_INVOCATION_PILOT_ENABLED
        percentage = settings.V2_INVOCATION_ROLLOUT_PERCENT
        canaries = settings.V2_INVOCATION_CANARY_FUNCTION_IDS
    selected = CoordinationVersion.V1
    stage = CUTOVER_STAGES.get(settings.V2_CUTOVER_STAGE, 0)
    is_canary = (
        function_id is not None and int(function_id) in parse_integer_set(canaries)
    )
    if enabled and is_canary and stage >= CUTOVER_STAGES["internal"]:
        selected = CoordinationVersion.V2
    elif enabled and cutover_stage_allows(stage, job_type, invoke_access):
        digest = hashlib.sha256(
            f"{job_type}:{routing_key}".encode("utf-8")
        ).digest()
        bucket = int.from_bytes(digest[:8], "big") % 100
        if bucket < max(0, min(100, int(percentage))):
            selected = CoordinationVersion.V2
    if selected == CoordinationVersion.V1 and not settings.V1_JOB_CREATION_ENABLED:
        raise RuntimeError(
            "V1 job creation is disabled and this job is not eligible for V2."
        )
    return selected


def cutover_stage_allows(stage: int, job_type: str, invoke_access: str | None) -> bool:
    if job_type == JobType.BUILD:
        return stage >= CUTOVER_STAGES["builds"]
    required = {
        "private": CUTOVER_STAGES["private"],
        "token": CUTOVER_STAGES["token"],
        "public": CUTOVER_STAGES["public"],
    }.get(str(invoke_access or "private"), CUTOVER_STAGES["all"])
    return stage >= required


def parse_integer_set(value) -> set[int]:
    parsed = set()
    for item in str(value or "").split(","):
        try:
            parsed.add(int(item.strip()))
        except (TypeError, ValueError):
            continue
    return parsed


def mark_build_jobs_from_status(build_attempt, build_status: str) -> int:
    return Job.objects.filter(build_attempt=build_attempt).exclude(
        status=JobStatus.DEAD_LETTERED,
    ).update(
        status=build_status_to_job_status(build_status)
    )


def mark_invocation_jobs_from_status(invocation, invocation_status: str) -> int:
    return Job.objects.filter(invocation=invocation).exclude(
        status=JobStatus.DEAD_LETTERED,
    ).update(
        status=invocation_status_to_job_status(invocation_status)
    )


def build_status_to_job_status(build_status: str) -> str:
    if build_status == BuildStatus.BUILDING:
        return JobStatus.RUNNING
    if build_status == BuildStatus.BUILT:
        return JobStatus.SUCCEEDED
    if build_status == BuildStatus.CANCELLED:
        return JobStatus.CANCELLED
    if build_status == BuildStatus.FAILED:
        return JobStatus.FAILED
    return JobStatus.QUEUED


def invocation_status_to_job_status(invocation_status: str) -> str:
    if invocation_status == InvocationStatus.RUNNING:
        return JobStatus.RUNNING
    if invocation_status == InvocationStatus.SUCCEEDED:
        return JobStatus.SUCCEEDED
    if invocation_status == InvocationStatus.CANCELLED:
        return JobStatus.CANCELLED
    if invocation_status in {InvocationStatus.FAILED, InvocationStatus.TIMEOUT}:
        return JobStatus.FAILED
    return JobStatus.QUEUED


def worker_queue_name(worker_name: str) -> str:
    return f"{settings.WORKER_QUEUE_PREFIX}:{worker_name}:jobs"


def worker_invocation_queue_name(worker_name: str) -> str:
    return f"{settings.WORKER_QUEUE_PREFIX}:{worker_name}:invocations"


def worker_build_queue_name(worker_name: str) -> str:
    return f"{settings.WORKER_QUEUE_PREFIX}:{worker_name}:builds"


def worker_processing_queue_name(worker_name: str) -> str:
    return f"{settings.WORKER_QUEUE_PREFIX}:{worker_name}:processing"


def scheduler_queue_name_for_type(job_type: str) -> str:
    if job_type == JobType.INVOCATION:
        return settings.SCHEDULER_INVOCATION_QUEUE_NAME
    if job_type == JobType.BUILD:
        return settings.SCHEDULER_BUILD_QUEUE_NAME
    return settings.SCHEDULER_QUEUE_NAME


def available_workers():
    from apps.workers.models import WorkerNode

    return WorkerNode.objects.filter(status=WorkerStatus.ONLINE).order_by(
        "name",
        "id",
    )
