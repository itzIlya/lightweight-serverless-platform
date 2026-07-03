from __future__ import annotations

from django.conf import settings
from django.db.models import Count

from apps.workers.models import WorkerNode

from .models import CoordinationVersion, Job, JobStatus
from .services import (
    worker_build_queue_name,
    worker_invocation_queue_name,
    worker_processing_queue_name,
    worker_queue_name,
)


TERMINAL_STATUSES = {
    JobStatus.SUCCEEDED,
    JobStatus.FAILED,
    JobStatus.CANCELLED,
    JobStatus.DEAD_LETTERED,
}


def v1_queue_names() -> list[str]:
    names = {
        settings.JOB_QUEUE_NAME,
        settings.SCHEDULER_QUEUE_NAME,
        settings.SCHEDULER_BUILD_QUEUE_NAME,
        settings.SCHEDULER_INVOCATION_QUEUE_NAME,
    }
    for worker_name in WorkerNode.objects.values_list("name", flat=True):
        names.update(
            {
                worker_queue_name(worker_name),
                worker_build_queue_name(worker_name),
                worker_invocation_queue_name(worker_name),
                worker_processing_queue_name(worker_name),
            }
        )
    return sorted(name for name in names if name)


def v1_retirement_status(redis_client) -> dict:
    active_jobs = Job.objects.filter(
        coordination_version=CoordinationVersion.V1,
    ).exclude(status__in=TERMINAL_STATUSES)
    status_counts = {
        JobStatus.QUEUED: 0,
        JobStatus.DISPATCHED: 0,
        JobStatus.RUNNING: 0,
    }
    status_counts.update(
        {
            row["status"]: row["total"]
            for row in active_jobs.values("status").annotate(total=Count("id"))
        }
    )
    queues = v1_queue_names()
    pipeline = redis_client.pipeline(transaction=False)
    for queue in queues:
        pipeline.llen(queue)
    lengths = pipeline.execute() if queues else []
    queue_depths = dict(zip(queues, (int(value) for value in lengths), strict=True))
    active_total = sum(status_counts.values())
    queued_total = sum(queue_depths.values())
    return {
        "ready": active_total == 0 and queued_total == 0,
        "v1_creation_enabled": settings.V1_JOB_CREATION_ENABLED,
        "v1_coordination_endpoints_enabled": (
            settings.V1_COORDINATION_ENDPOINTS_ENABLED
        ),
        "active_jobs": status_counts,
        "active_job_total": active_total,
        "queue_depths": queue_depths,
        "queued_item_total": queued_total,
    }
