from __future__ import annotations

from django.conf import settings

from apps.jobs.models import CoordinationVersion, Job

from .models import (
    Invocation,
    InvocationStatus,
    InvocationStagedCompletion,
    StagedCompletionStatus,
)
from .serializers import (
    InvocationOutputFileSerializer,
    InvocationSerializer,
)


V2_JOB_KEY_PREFIX = "orchestrator:v2:job"

V2_ACTIVE_STATUS_MAP = {
    "queued": InvocationStatus.QUEUED,
    "dispatched": InvocationStatus.RUNNING,
    "running": InvocationStatus.RUNNING,
    "finalizing": InvocationStatus.RUNNING,
}

V2_TERMINAL_STATUS_MAP = {
    "succeeded": InvocationStatus.SUCCEEDED,
    "failed": InvocationStatus.FAILED,
    "cancelled": InvocationStatus.CANCELLED,
    "dead_lettered": InvocationStatus.FAILED,
}


def serialize_invocation_for_read(invocation: Invocation) -> dict:
    data = InvocationSerializer(invocation).data
    snapshot = get_v2_invocation_snapshot(invocation)
    if snapshot is None:
        return data

    if snapshot.committed_completion is not None:
        completion = snapshot.committed_completion
        data.update(
            {
                "status": V2_TERMINAL_STATUS_MAP.get(
                    snapshot.redis_status,
                    InvocationStatus.FAILED,
                ),
                "result": completion.result,
                "stdout": completion.stdout,
                "stderr": completion.stderr,
                "exit_code": completion.exit_code,
                "cold_start": completion.cold_start,
                "error_message": completion.error_message,
                "finished_at": completion.committed_at,
                "duration_ms": completion.duration_ms,
                "output_files": InvocationOutputFileSerializer(
                    completion.output_files.filter(
                        status=StagedCompletionStatus.COMMITTED,
                    ),
                    many=True,
                ).data,
                "frontend_state": V2_TERMINAL_STATUS_MAP.get(
                    snapshot.redis_status,
                    InvocationStatus.FAILED,
                ),
                "is_terminal": True,
                "poll_after_seconds": None,
                "result_available": True,
                "outputs_available": completion.output_files.filter(
                    status=StagedCompletionStatus.COMMITTED,
                ).exists(),
                "can_read_outputs": True,
                "can_download": True,
            }
        )
        return data

    if snapshot.redis_status in V2_ACTIVE_STATUS_MAP:
        data["status"] = V2_ACTIVE_STATUS_MAP[snapshot.redis_status]
        data["frontend_state"] = V2_ACTIVE_STATUS_MAP[snapshot.redis_status]
        data["output_files"] = []
        data["is_terminal"] = False
        data["poll_after_seconds"] = 1
        data["result_available"] = False
        data["outputs_available"] = False
        data["can_read_outputs"] = False
        data["can_download"] = False
    return data


def visible_invocation_outputs(invocation: Invocation):
    snapshot = get_v2_invocation_snapshot(invocation)
    if snapshot is not None:
        if snapshot.committed_completion is None:
            return invocation.output_files.none()
        return snapshot.committed_completion.output_files.filter(
            status=StagedCompletionStatus.COMMITTED,
        )
    if invocation.status not in terminal_invocation_statuses():
        return invocation.output_files.none()
    return invocation.output_files.filter(status=StagedCompletionStatus.COMMITTED)


def visible_invocation_logs(invocation: Invocation):
    snapshot = get_v2_invocation_snapshot(invocation)
    if snapshot is not None:
        if snapshot.committed_completion is None:
            return invocation.log_artifacts.none()
        return snapshot.committed_completion.log_artifacts.filter(
            status=StagedCompletionStatus.COMMITTED,
        )
    if invocation.status not in terminal_invocation_statuses():
        return invocation.log_artifacts.none()
    return invocation.log_artifacts.filter(status=StagedCompletionStatus.COMMITTED)


def invocation_outputs_are_published(invocation: Invocation) -> bool:
    snapshot = get_v2_invocation_snapshot(invocation)
    if snapshot is not None:
        return snapshot.committed_completion is not None
    return invocation.status in terminal_invocation_statuses()


def terminal_invocation_statuses():
    return {
        InvocationStatus.SUCCEEDED,
        InvocationStatus.FAILED,
        InvocationStatus.TIMEOUT,
        InvocationStatus.CANCELLED,
    }


class V2InvocationSnapshot:
    def __init__(self, *, redis_status: str, committed_completion):
        self.redis_status = redis_status
        self.committed_completion = committed_completion


def get_v2_invocation_snapshot(invocation: Invocation) -> V2InvocationSnapshot | None:
    job = (
        Job.objects.filter(
            invocation=invocation,
            coordination_version=CoordinationVersion.V2,
        )
        .order_by("-id")
        .first()
    )
    if job is None:
        return None

    state = _read_v2_job_state(job.job_id)
    if not state:
        return None

    redis_status = str(state.get("status") or "")
    if redis_status not in {*V2_ACTIVE_STATUS_MAP, *V2_TERMINAL_STATUS_MAP}:
        return None

    committed_completion = None
    if redis_status in V2_TERMINAL_STATUS_MAP:
        committed_completion = _committed_completion_for_state(invocation, job, state)

    return V2InvocationSnapshot(
        redis_status=redis_status,
        committed_completion=committed_completion,
    )


def _read_v2_job_state(job_id) -> dict:
    import redis

    try:
        client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)
        return client.hgetall(f"{V2_JOB_KEY_PREFIX}:{job_id}") or {}
    except redis.RedisError:
        return {}


def _committed_completion_for_state(invocation: Invocation, job: Job, state: dict):
    completion_id = str(state.get("completion_id") or "")
    artifact_commit_id = str(state.get("artifact_commit_id") or "")
    if not completion_id or not artifact_commit_id:
        return None

    completion = (
        InvocationStagedCompletion.objects.prefetch_related("output_files")
        .filter(
            invocation=invocation,
            job_id=job.job_id,
            completion_id=completion_id,
            status=StagedCompletionStatus.COMMITTED,
        )
        .first()
    )
    if completion is None:
        return None
    if str(completion.artifact_commit_id) != artifact_commit_id:
        return None
    return completion
