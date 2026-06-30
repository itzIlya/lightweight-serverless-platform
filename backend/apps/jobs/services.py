from __future__ import annotations

from django.conf import settings
from django.db import transaction

from apps.functions.models import BuildStatus
from apps.invocations.models import InvocationStatus
from apps.workers.models import WorkerStatus

from .models import CoordinationVersion, Job, JobStatus, JobType, OutboxEvent


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


def create_build_job_record(build_attempt, payload: dict) -> Job:
    with transaction.atomic():
        job = Job.objects.create(
            type=JobType.BUILD,
            status=JobStatus.QUEUED,
            queue_name=scheduler_queue_name_for_type(JobType.BUILD),
            payload=payload,
            build_attempt=build_attempt,
            available_at=build_attempt.queued_at,
            max_recovery_attempts=max_recovery_attempts_for_type(JobType.BUILD),
            coordination_version=(
                CoordinationVersion.V2
                if settings.V2_BUILD_PILOT_ENABLED
                else CoordinationVersion.V1
            ),
        )
        return _finish_job_creation(job, payload)


def create_invocation_job_record(invocation, payload: dict) -> Job:
    with transaction.atomic():
        job = Job.objects.create(
            type=JobType.INVOCATION,
            status=JobStatus.QUEUED,
            queue_name=scheduler_queue_name_for_type(JobType.INVOCATION),
            payload=payload,
            invocation=invocation,
            available_at=invocation.queued_at,
            max_recovery_attempts=max_recovery_attempts_for_type(JobType.INVOCATION),
            coordination_version=(
                CoordinationVersion.V2
                if settings.V2_INVOCATION_PILOT_ENABLED
                else CoordinationVersion.V1
            ),
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
