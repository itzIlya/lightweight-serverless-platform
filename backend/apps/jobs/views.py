from django.conf import settings
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Job, JobStatus
from .services import available_workers, worker_processing_queue_name, worker_queue_name
from apps.workers.models import WorkerNode, WorkerStatus


def _authorize_internal(request):
    token = request.headers.get("X-Internal-Token", "")
    if token != settings.WORKER_SHARED_SECRET:
        return Response(
            {"detail": "Unauthorized."},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    return None


@api_view(["GET"])
@permission_classes([])
def get_scheduler_job(request, job_id):
    unauthorized = _authorize_internal(request)
    if unauthorized:
        return unauthorized

    job = get_object_or_404(Job, job_id=job_id)
    return Response(_job_payload(job))


@api_view(["GET"])
@permission_classes([])
def list_scheduler_workers(request):
    unauthorized = _authorize_internal(request)
    if unauthorized:
        return unauthorized

    workers = [_scheduler_worker_payload(worker) for worker in available_workers()]
    return Response(workers)


@api_view(["POST"])
@permission_classes([])
def expire_stale_scheduler_workers(request):
    unauthorized = _authorize_internal(request)
    if unauthorized:
        return unauthorized

    stale_after_seconds = int(
        request.data.get("stale_after_seconds")
        or settings.WORKER_STALE_AFTER_SECONDS
    )
    cutoff = timezone.now() - timedelta(seconds=stale_after_seconds)
    stale_workers = list(
        WorkerNode.objects.filter(
            status=WorkerStatus.ONLINE,
            last_seen_at__lt=cutoff,
        ).order_by("name", "id")
    )

    expired = []
    for worker in stale_workers:
        worker.status = WorkerStatus.OFFLINE
        worker.save(update_fields=["status", "updated_at"])
        expired.append(_scheduler_worker_payload(worker))

    return Response(
        {
            "expired": expired,
            "stale_after_seconds": stale_after_seconds,
        }
    )


@api_view(["POST"])
@permission_classes([])
def dispatch_scheduler_job(request, job_id):
    unauthorized = _authorize_internal(request)
    if unauthorized:
        return unauthorized

    job = get_object_or_404(Job, job_id=job_id)
    if job.status != JobStatus.QUEUED:
        return Response(
            {
                "dispatched": False,
                "status": job.status,
                "detail": "Job is no longer queued.",
            }
        )

    queue_name = request.data.get("queue_name", "")
    worker_name = request.data.get("worker_name", "")
    if not queue_name or not worker_name:
        return Response(
            {"detail": "worker_name and queue_name are required."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    with transaction.atomic():
        job = Job.objects.select_for_update().get(pk=job.pk)
        if job.status != JobStatus.QUEUED:
            return Response(
                {
                    "dispatched": False,
                    "status": job.status,
                    "detail": "Job is no longer queued.",
                }
            )

        dispatch_attempt = job.dispatch_attempts + 1
        job.status = JobStatus.DISPATCHED
        job.queue_name = queue_name
        job.dispatch_attempts = dispatch_attempt
        job.payload["assigned_worker"] = worker_name
        job.payload["worker_queue_name"] = queue_name
        job.payload["dispatch_attempt"] = dispatch_attempt
        job.save(
            update_fields=[
                "status",
                "queue_name",
                "dispatch_attempts",
                "payload",
                "updated_at",
            ]
        )
    return Response(
        {
            "dispatched": True,
            "job": _job_payload(job),
        }
    )


@api_view(["POST"])
@permission_classes([])
def claim_worker_job(request, job_id):
    unauthorized = _authorize_internal(request)
    if unauthorized:
        return unauthorized

    worker_name = request.data.get("worker_name", "")
    dispatch_attempt = request.data.get("dispatch_attempt")
    if not worker_name or dispatch_attempt in ("", None):
        return Response(
            {"detail": "worker_name and dispatch_attempt are required."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    dispatch_attempt = int(dispatch_attempt)

    with transaction.atomic():
        job = get_object_or_404(Job.objects.select_for_update(), job_id=job_id)
        expected_worker = job.payload.get("assigned_worker", "")
        expected_attempt = job.payload.get("dispatch_attempt")

        if job.status in {
            JobStatus.SUCCEEDED,
            JobStatus.FAILED,
            JobStatus.CANCELLED,
        }:
            return Response(
                {
                    "claimed": False,
                    "terminal": True,
                    "status": job.status,
                }
            )

        if (
            job.status not in {JobStatus.DISPATCHED, JobStatus.RUNNING}
            or expected_worker != worker_name
            or expected_attempt != dispatch_attempt
        ):
            return Response(
                {
                    "claimed": False,
                    "stale": True,
                    "status": job.status,
                    "expected_worker": expected_worker,
                    "reported_worker": worker_name,
                    "expected_dispatch_attempt": expected_attempt,
                    "reported_dispatch_attempt": dispatch_attempt,
                }
            )

        if job.status == JobStatus.DISPATCHED:
            job.status = JobStatus.RUNNING
            job.save(update_fields=["status", "updated_at"])

    return Response(
        {
            "claimed": True,
            "job": _job_payload(job),
        }
    )


@api_view(["POST"])
@permission_classes([])
def requeue_scheduler_job(request, job_id):
    unauthorized = _authorize_internal(request)
    if unauthorized:
        return unauthorized

    worker_name = request.data.get("worker_name", "")
    reason = request.data.get("reason", "")
    if not worker_name:
        return Response(
            {"detail": "worker_name is required."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    with transaction.atomic():
        job = get_object_or_404(Job.objects.select_for_update(), job_id=job_id)
        if job.status in {
            JobStatus.SUCCEEDED,
            JobStatus.FAILED,
            JobStatus.CANCELLED,
        }:
            return Response(
                {
                    "requeued": False,
                    "terminal": True,
                    "status": job.status,
                }
            )

        assigned_worker = job.payload.get("assigned_worker", "")
        if assigned_worker and assigned_worker != worker_name:
            return Response(
                {
                    "requeued": False,
                    "status": job.status,
                    "detail": "Job belongs to a different worker.",
                },
                status=status.HTTP_409_CONFLICT,
            )

        job.status = JobStatus.QUEUED
        job.queue_name = settings.SCHEDULER_QUEUE_NAME
        job.last_error = reason
        for key in ("assigned_worker", "worker_queue_name"):
            job.payload.pop(key, None)
        job.save(
            update_fields=[
                "status",
                "queue_name",
                "last_error",
                "payload",
                "updated_at",
            ]
        )

    return Response(
        {
            "requeued": True,
            "job": _job_payload(job),
        }
    )


def _job_payload(job):
    return {
        "id": job.id,
        "job_id": str(job.job_id),
        "type": job.type,
        "status": job.status,
        "queue_name": job.queue_name,
        "payload": job.payload,
        "dispatch_attempts": job.dispatch_attempts,
        "available_at": job.available_at,
        "updated_at": job.updated_at,
    }


def _scheduler_worker_payload(worker):
    return {
        "id": worker.id,
        "name": worker.name,
        "hostname": worker.hostname,
        "status": worker.status,
        "max_concurrency": worker.max_concurrency,
        "max_build_concurrency": worker.max_build_concurrency,
        "queue_name": worker_queue_name(worker.name),
        "processing_queue_name": worker_processing_queue_name(worker.name),
        "last_seen_at": worker.last_seen_at,
    }
