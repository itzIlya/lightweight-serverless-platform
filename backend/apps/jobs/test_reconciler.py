import io
import uuid
import zipfile
from unittest.mock import Mock

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from apps.functions.models import Function, FunctionVersion
from apps.invocations.models import (
    Invocation,
    InvocationStagedCompletion,
    InvocationStatus,
    StagedCompletionStatus,
)

from .models import CoordinationVersion, Job, JobStatus, JobType
from .reconciler import CrossStoreReconciler


def bundle():
    data = io.BytesIO()
    with zipfile.ZipFile(data, "w") as archive:
        archive.writestr("handler.py", "def main(event, context): return event\n")
        archive.writestr("requirements.txt", "")
        archive.writestr("config.json", "{}")
    return SimpleUploadedFile("function.zip", data.getvalue())


class CrossStoreReconcilerTests(TestCase):
    def setUp(self):
        owner = get_user_model().objects.create_user(username="reconcile-owner")
        function = Function.objects.create(
            owner=owner,
            name="Reconcile",
            slug="reconcile",
        )
        self.version = FunctionVersion.objects.create(
            function=function,
            version="v1",
            source_bundle=bundle(),
        )
        self.redis = Mock()
        self.pipeline = self.redis.pipeline.return_value
        self.orchestrator = Mock()
        self.reconciler = CrossStoreReconciler(self.redis, self.orchestrator)

    def test_empty_audit_uses_two_queries_and_no_redis_roundtrip(self):
        with self.assertNumQueries(2):
            result = self.reconciler.reconcile_once()

        self.assertEqual(result["checked_jobs"], 0)
        self.assertEqual(result["checked_commits"], 0)
        self.redis.pipeline.assert_not_called()
        self.orchestrator.post.assert_not_called()

    def test_terminal_redis_job_republishes_missing_postgres_projection(self):
        invocation = Invocation.objects.create(function_version=self.version, event={})
        job = Job.objects.create(
            type=JobType.INVOCATION,
            status=JobStatus.RUNNING,
            coordination_version=CoordinationVersion.V2,
            queue_name="worker:a:v2:invocations",
            invocation=invocation,
        )
        self.pipeline.execute.return_value = [{"status": "succeeded"}]
        self.orchestrator.post.return_value = {"published": True}

        result = self.reconciler.reconcile_once()

        self.assertEqual(result["repaired_projections"], 1)
        self.orchestrator.post.assert_called_once_with(
            f"/v2/jobs/{job.job_id}/repair-projection"
        )
        self.redis.pipeline.assert_called_once_with(transaction=False)

    def test_committed_artifact_resumes_matching_finalization(self):
        invocation = Invocation.objects.create(
            function_version=self.version,
            event={},
            status=InvocationStatus.RUNNING,
        )
        job = Job.objects.create(
            type=JobType.INVOCATION,
            status=JobStatus.RUNNING,
            coordination_version=CoordinationVersion.V2,
            queue_name="worker:a:v2:invocations",
            invocation=invocation,
        )
        completion_id = f"{job.job_id}:1:invocation"
        artifact_commit_id = uuid.uuid4()
        InvocationStagedCompletion.objects.create(
            invocation=invocation,
            job_id=job.job_id,
            dispatch_attempt=1,
            completion_id=completion_id,
            status=StagedCompletionStatus.COMMITTED,
            terminal_status="succeeded",
            artifact_commit_id=artifact_commit_id,
        )
        self.pipeline.execute.return_value = [
            {"status": "finalizing", "completion_id": completion_id}
        ]
        self.orchestrator.post.return_value = {"finalized": True}

        result = self.reconciler.reconcile_once()

        self.assertEqual(result["resumed_commits"], 1)
        self.orchestrator.post.assert_called_once_with(
            f"/v2/jobs/{job.job_id}/finalize",
            {
                "completion_id": completion_id,
                "status": "succeeded",
                "artifact_commit_id": str(artifact_commit_id),
            },
        )

    def test_committed_artifact_with_missing_redis_state_is_detected_only(self):
        invocation = Invocation.objects.create(
            function_version=self.version,
            event={},
            status=InvocationStatus.RUNNING,
        )
        job = Job.objects.create(
            type=JobType.INVOCATION,
            status=JobStatus.RUNNING,
            coordination_version=CoordinationVersion.V2,
            queue_name="worker:a:v2:invocations",
            invocation=invocation,
        )
        InvocationStagedCompletion.objects.create(
            invocation=invocation,
            job_id=job.job_id,
            dispatch_attempt=1,
            completion_id=f"{job.job_id}:1:invocation",
            status=StagedCompletionStatus.COMMITTED,
            terminal_status="succeeded",
            artifact_commit_id=uuid.uuid4(),
        )
        self.pipeline.execute.return_value = [{}]

        result = self.reconciler.reconcile_once()

        self.assertEqual(result["anomalies"], 1)
        self.orchestrator.post.assert_not_called()
