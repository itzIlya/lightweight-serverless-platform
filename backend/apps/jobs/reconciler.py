from __future__ import annotations

import json
from urllib import error, request

from apps.invocations.models import (
    InvocationStagedCompletion,
    InvocationStatus,
    StagedCompletionStatus,
)

from .models import CoordinationVersion, Job, JobStatus


POSTGRES_TERMINAL = {
    JobStatus.SUCCEEDED,
    JobStatus.FAILED,
    JobStatus.CANCELLED,
    JobStatus.DEAD_LETTERED,
}
INVOCATION_TERMINAL = {
    InvocationStatus.SUCCEEDED,
    InvocationStatus.FAILED,
    InvocationStatus.TIMEOUT,
    InvocationStatus.CANCELLED,
}
REDIS_TERMINAL = {"succeeded", "failed", "cancelled", "dead_lettered"}


class OrchestratorRepairClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.token = token

    def post(self, path: str, payload: dict | None = None) -> dict:
        http_request = request.Request(
            f"{self.base_url}{path}",
            data=json.dumps(payload or {}).encode("utf-8"),
            method="POST",
            headers={
                "Content-Type": "application/json",
                "X-Internal-Token": self.token,
            },
        )
        try:
            with request.urlopen(http_request, timeout=10) as response:
                return json.loads(response.read().decode("utf-8") or "{}")
        except (error.HTTPError, error.URLError, OSError) as exc:
            raise RuntimeError(f"orchestrator repair failed: {exc}") from exc


class CrossStoreReconciler:
    def __init__(
        self,
        redis_client,
        orchestrator_client,
        *,
        state_prefix: str = "orchestrator:v2:job",
    ):
        self.redis = redis_client
        self.orchestrator = orchestrator_client
        self.state_prefix = state_prefix.rstrip(":")

    def reconcile_once(self, *, limit: int = 100) -> dict[str, int]:
        jobs = list(
            Job.objects.filter(coordination_version=CoordinationVersion.V2)
            .exclude(status__in=POSTGRES_TERMINAL)
            .order_by("updated_at")[:limit]
        )
        completions = list(
            InvocationStagedCompletion.objects.filter(
                status=StagedCompletionStatus.COMMITTED,
                invocation__jobs__coordination_version=CoordinationVersion.V2,
            )
            .exclude(invocation__status__in=INVOCATION_TERMINAL)
            .select_related("invocation")
            .distinct()
            .order_by("committed_at")[:limit]
        )
        job_ids = {str(job.job_id) for job in jobs}
        job_ids.update(str(completion.job_id) for completion in completions)
        states = self._load_states(job_ids)

        repaired_projections = 0
        resumed_commits = 0
        anomalies = 0
        for job in jobs:
            state = states.get(str(job.job_id), {})
            if state.get("status") not in REDIS_TERMINAL:
                continue
            response = self.orchestrator.post(
                f"/v2/jobs/{job.job_id}/repair-projection"
            )
            repaired_projections += int(bool(response.get("published")))

        for completion in completions:
            state = states.get(str(completion.job_id), {})
            if (
                state.get("status") == "finalizing"
                and state.get("completion_id") == completion.completion_id
            ):
                response = self.orchestrator.post(
                    f"/v2/jobs/{completion.job_id}/finalize",
                    {
                        "completion_id": completion.completion_id,
                        "status": completion.terminal_status,
                        "artifact_commit_id": str(completion.artifact_commit_id),
                    },
                )
                resumed_commits += int(bool(response.get("finalized")))
            elif state.get("status") not in REDIS_TERMINAL:
                anomalies += 1

        return {
            "checked_jobs": len(jobs),
            "checked_commits": len(completions),
            "repaired_projections": repaired_projections,
            "resumed_commits": resumed_commits,
            "anomalies": anomalies,
        }

    def _load_states(self, job_ids: set[str]) -> dict[str, dict]:
        if not job_ids:
            return {}
        ordered = sorted(job_ids)
        pipeline = self.redis.pipeline(transaction=False)
        for job_id in ordered:
            pipeline.hgetall(f"{self.state_prefix}:{job_id}")
        return dict(zip(ordered, pipeline.execute(), strict=True))
