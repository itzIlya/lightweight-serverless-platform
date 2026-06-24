from __future__ import annotations

import json
from pathlib import PurePosixPath
import re
import uuid
import zipfile

from django.conf import settings
from django.db import transaction
from django.utils import timezone

from apps.workers.models import WorkerNode, WorkerStatus

from .models import (
    BuildAttempt,
    BuildLease,
    BuildLeaseStatus,
    BuildPolicy,
    BuildStatus,
    FunctionVersion,
)


REQUIRED_BUNDLE_FILES = {
    "handler.py",
    "requirements.txt",
    "config.json",
}


class BuildAdmissionError(ValueError):
    def __init__(self, message: str, *, retry_after_seconds: int | None = None):
        super().__init__(message)
        self.retry_after_seconds = retry_after_seconds


def validate_function_bundle(uploaded_file) -> None:
    name = getattr(uploaded_file, "name", "")
    if not name.lower().endswith(".zip"):
        raise ValueError("Function bundle must be a .zip archive.")

    try:
        uploaded_file.seek(0)
        with zipfile.ZipFile(uploaded_file) as archive:
            paths = []
            for info in archive.infolist():
                if "\\" in info.filename:
                    raise ValueError(
                        f"Bundle contains unsafe path: {info.filename}"
                    )
                entry = PurePosixPath(info.filename)
                if entry.is_absolute() or ".." in entry.parts:
                    raise ValueError(
                        f"Bundle contains unsafe path: {info.filename}"
                    )
                if info.is_dir():
                    continue
                paths.append(entry)

            top_level = {path.name for path in paths if len(path.parts) == 1}
            missing = sorted(REQUIRED_BUNDLE_FILES - top_level)
            if missing:
                raise ValueError(
                    "Bundle is missing required files: " + ", ".join(missing)
                )
    except zipfile.BadZipFile as exc:
        raise ValueError("Function bundle is not a valid zip archive.") from exc
    finally:
        try:
            uploaded_file.seek(0)
        except Exception:
            pass


def make_image_ref(version: FunctionVersion, registry: str | None = None) -> str:
    registry = registry or settings.LOCAL_REGISTRY
    slug = sanitize_tag_part(version.function.slug)
    version_part = sanitize_tag_part(version.version)
    return f"{registry}/functions/{slug}:v{version.id}-{version_part}"


def sanitize_tag_part(value: str) -> str:
    normalized = re.sub(r"[^a-zA-Z0-9_.-]+", "-", value).strip(".-")
    return normalized.lower() or "function"


def create_build_attempt(
    version: FunctionVersion,
    *,
    build_id=None,
    attempt_number: int = 1,
) -> BuildAttempt:
    attempt = BuildAttempt.objects.create(
        build_id=build_id or uuid.uuid4(),
        function_version=version,
        attempt_number=attempt_number,
        status=BuildStatus.QUEUED,
        log="Build queued.",
        queued_at=timezone.now(),
    )
    sync_version_from_attempt(version, attempt)
    return attempt


def sync_version_from_attempt(
    version: FunctionVersion,
    attempt: BuildAttempt,
) -> None:
    version.build_request_id = attempt.request_id
    version.build_status = attempt.status
    version.build_log = attempt.log
    version.build_queued_at = attempt.queued_at
    version.build_started_at = attempt.started_at
    version.build_finished_at = attempt.finished_at
    if attempt.image_ref:
        version.image_ref = attempt.image_ref
    version.save(
        update_fields=[
            "build_request_id",
            "build_status",
            "build_log",
            "build_queued_at",
            "build_started_at",
            "build_finished_at",
            "image_ref",
            "updated_at",
        ]
    )


def get_build_policy() -> BuildPolicy:
    policy, _ = BuildPolicy.objects.get_or_create(
        pk=1,
        defaults={"max_retries": 2},
    )
    return policy


def get_locked_build_policy() -> BuildPolicy:
    policy, _ = BuildPolicy.objects.select_for_update().get_or_create(
        pk=1,
        defaults={"max_retries": 2},
    )
    return policy


def enforce_build_submission_limits(
    *,
    version: FunctionVersion,
    policy: BuildPolicy,
    now=None,
) -> None:
    now = now or timezone.now()
    owner = version.function.owner
    since = now - timezone.timedelta(hours=1)

    user_builds_last_hour = BuildAttempt.objects.filter(
        attempt_number=1,
        queued_at__gte=since,
        function_version__function__owner=owner,
    ).count()
    if user_builds_last_hour >= policy.max_builds_per_user_per_hour:
        raise BuildAdmissionError(
            "Build rate limit exceeded for this user.",
            retry_after_seconds=_retry_after_seconds(
                BuildAttempt.objects.filter(
                    attempt_number=1,
                    queued_at__gte=since,
                    function_version__function__owner=owner,
                ).order_by("queued_at").first(),
                now,
            ),
        )

    function_builds_last_hour = BuildAttempt.objects.filter(
        attempt_number=1,
        queued_at__gte=since,
        function_version__function=version.function,
    ).count()
    if function_builds_last_hour >= policy.max_builds_per_function_per_hour:
        raise BuildAdmissionError(
            "Build rate limit exceeded for this function.",
            retry_after_seconds=_retry_after_seconds(
                BuildAttempt.objects.filter(
                    attempt_number=1,
                    queued_at__gte=since,
                    function_version__function=version.function,
                ).order_by("queued_at").first(),
                now,
            ),
        )

    queued_statuses = [BuildStatus.QUEUED]
    user_queued = BuildAttempt.objects.filter(
        status__in=queued_statuses,
        function_version__function__owner=owner,
    ).count()
    if user_queued >= policy.max_queued_builds_per_user:
        raise BuildAdmissionError("Too many queued builds for this user.")

    function_queued = BuildAttempt.objects.filter(
        status__in=queued_statuses,
        function_version__function=version.function,
    ).count()
    if function_queued >= policy.max_queued_builds_per_function:
        raise BuildAdmissionError("Too many queued builds for this function.")


def _retry_after_seconds(first_attempt: BuildAttempt | None, now) -> int | None:
    if first_attempt is None:
        return None
    retry_at = first_attempt.queued_at + timezone.timedelta(hours=1)
    return max(1, int((retry_at - now).total_seconds()))


def expire_stale_build_leases(now=None) -> int:
    now = now or timezone.now()
    return BuildLease.objects.filter(
        status=BuildLeaseStatus.ACTIVE,
        expires_at__lte=now,
    ).update(
        status=BuildLeaseStatus.EXPIRED,
        released_at=now,
        release_reason="Lease expired.",
    )


def acquire_build_lease(
    *,
    attempt: BuildAttempt,
    worker_name: str,
    hostname: str = "",
    max_build_concurrency: int | None = None,
    now=None,
) -> tuple[BuildLease | None, str]:
    now = now or timezone.now()
    worker_name = worker_name.strip()
    if not worker_name:
        return None, "worker_name is required"

    with transaction.atomic():
        policy = get_locked_build_policy()
        expire_stale_build_leases(now)
        attempt = BuildAttempt.objects.select_for_update().select_related(
            "function_version",
            "function_version__function",
        ).get(pk=attempt.pk)

        if attempt.status in {
            BuildStatus.BUILT,
            BuildStatus.FAILED,
            BuildStatus.CANCELLED,
            BuildStatus.CANCELLING,
        }:
            return None, f"Build attempt is {attempt.status}."

        worker, _ = WorkerNode.objects.select_for_update().get_or_create(
            name=worker_name,
            defaults={
                "hostname": hostname or worker_name,
                "status": WorkerStatus.ONLINE,
                "max_build_concurrency": max_build_concurrency or 1,
                "last_seen_at": now,
            },
        )
        worker.hostname = hostname or worker.hostname or worker_name
        worker.status = WorkerStatus.ONLINE
        worker.last_seen_at = now
        if max_build_concurrency is not None:
            worker.max_build_concurrency = max(1, int(max_build_concurrency))
        worker.save(
            update_fields=[
                "hostname",
                "status",
                "last_seen_at",
                "max_build_concurrency",
                "updated_at",
            ]
        )

        active_for_attempt = BuildLease.objects.select_for_update().filter(
            build_attempt=attempt,
            status=BuildLeaseStatus.ACTIVE,
        ).first()
        if active_for_attempt is not None:
            if active_for_attempt.worker_id == worker.id:
                active_for_attempt.expires_at = now + timezone.timedelta(
                    seconds=policy.build_lease_seconds
                )
                active_for_attempt.save(update_fields=["expires_at", "updated_at"])
                return active_for_attempt, "lease refreshed"
            return None, "Build attempt already has an active lease."

        active_global = BuildLease.objects.filter(
            status=BuildLeaseStatus.ACTIVE,
        ).count()
        if active_global >= policy.max_concurrent_builds:
            return None, "Global build concurrency limit reached."

        active_for_worker = BuildLease.objects.filter(
            status=BuildLeaseStatus.ACTIVE,
            worker=worker,
        ).count()
        if active_for_worker >= worker.max_build_concurrency:
            return None, "Worker build concurrency limit reached."

        lease = BuildLease.objects.create(
            build_attempt=attempt,
            worker=worker,
            status=BuildLeaseStatus.ACTIVE,
            acquired_at=now,
            expires_at=now + timezone.timedelta(seconds=policy.build_lease_seconds),
        )
        return lease, "lease acquired"


def release_build_lease(
    *,
    attempt: BuildAttempt,
    lease_id: int | None = None,
    reason: str = "",
    now=None,
) -> int:
    now = now or timezone.now()
    queryset = BuildLease.objects.filter(
        build_attempt=attempt,
        status=BuildLeaseStatus.ACTIVE,
    )
    if lease_id is not None:
        queryset = queryset.filter(id=lease_id)
    return queryset.update(
        status=BuildLeaseStatus.RELEASED,
        released_at=now,
        release_reason=reason,
    )


def build_function_job(attempt: BuildAttempt) -> dict:
    version = attempt.function_version
    return {
        "type": "function.build",
        "build_request_id": str(attempt.request_id),
        "build_id": str(attempt.build_id),
        "attempt_number": attempt.attempt_number,
        "function_id": version.function_id,
        "function_slug": version.function.slug,
        "function_version_id": version.id,
        "version": version.version,
        "runtime": version.runtime,
        "handler": version.handler,
        "image_ref": make_image_ref(version),
        "queued_at": attempt.queued_at.isoformat(),
    }


def enqueue_build_attempt(attempt: BuildAttempt) -> dict:
    import redis
    from apps.jobs.services import create_build_job_record

    payload = build_function_job(attempt)
    job = create_build_job_record(attempt, payload)
    client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)
    client.rpush(settings.SCHEDULER_QUEUE_NAME, str(job.job_id))
    return payload
