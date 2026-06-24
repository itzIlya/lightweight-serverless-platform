from __future__ import annotations

from django.conf import settings

from apps.functions.models import BuildStatus
from apps.invocations.models import InvocationStatus
from apps.workers.models import WorkerStatus

from .models import Job, JobStatus, JobType


def create_build_job_record(build_attempt, payload: dict) -> Job:
    job = Job.objects.create(
        type=JobType.BUILD,
        status=JobStatus.QUEUED,
        queue_name=settings.SCHEDULER_QUEUE_NAME,
        payload=payload,
        build_attempt=build_attempt,
        available_at=build_attempt.queued_at,
    )
    payload["job_id"] = str(job.job_id)
    job.payload = payload
    job.save(update_fields=["payload", "updated_at"])
    return job


def create_invocation_job_record(invocation, payload: dict) -> Job:
    job = Job.objects.create(
        type=JobType.INVOCATION,
        status=JobStatus.QUEUED,
        queue_name=settings.SCHEDULER_QUEUE_NAME,
        payload=payload,
        invocation=invocation,
        available_at=invocation.queued_at,
    )
    payload["job_id"] = str(job.job_id)
    job.payload = payload
    job.save(update_fields=["payload", "updated_at"])
    return job


def mark_build_jobs_from_status(build_attempt, build_status: str) -> int:
    return Job.objects.filter(build_attempt=build_attempt).update(
        status=build_status_to_job_status(build_status)
    )


def mark_invocation_jobs_from_status(invocation, invocation_status: str) -> int:
    return Job.objects.filter(invocation=invocation).update(
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


def worker_processing_queue_name(worker_name: str) -> str:
    return f"{settings.WORKER_QUEUE_PREFIX}:{worker_name}:processing"


def available_workers():
    from apps.workers.models import WorkerNode

    return WorkerNode.objects.filter(status=WorkerStatus.ONLINE).order_by(
        "name",
        "id",
    )
