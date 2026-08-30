import hashlib
import io
import json
import tempfile
from datetime import timedelta
import zipfile

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from apps.functions.models import BuildStatus, Function, FunctionVersion
from apps.jobs.models import CoordinationVersion, Job, JobStatus, JobType
from apps.jobs.projector import apply_orchestrator_projection

from .services import issue_runner_output_upload_token
from .management.commands.cleanup_staged_invocations import (
    cleanup_expired_staged_completions,
)
from .models import (
    Invocation,
    InvocationLogArtifact,
    InvocationOutputFile,
    InvocationStagedCompletion,
    InvocationStatus,
    StagedCompletionStatus,
)


def bundle():
    data = io.BytesIO()
    with zipfile.ZipFile(data, "w") as archive:
        archive.writestr("handler.py", "def main(event, context): return event\n")
        archive.writestr("requirements.txt", "")
        archive.writestr("config.json", "{}")
    return SimpleUploadedFile("function.zip", data.getvalue())


class StagedInvocationArtifactTests(APITestCase):
    def setUp(self):
        self.media = tempfile.TemporaryDirectory()
        self.media_override = override_settings(MEDIA_ROOT=self.media.name)
        self.media_override.enable()
        owner = get_user_model().objects.create_user(username="stage-owner")
        token = RefreshToken.for_user(owner).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        function = Function.objects.create(owner=owner, name="Stage", slug="stage")
        version = FunctionVersion.objects.create(
            function=function,
            version="v1",
            source_bundle=bundle(),
            image_ref="localhost:5000/functions/stage:v1",
            build_status=BuildStatus.BUILT,
            declared_output_files=["report.txt"],
            invocation_output_max_files=1,
            invocation_output_max_file_size_mb=1,
            invocation_output_max_total_size_mb=1,
        )
        self.invocation = Invocation.objects.create(
            function_version=version,
            event={},
            status=InvocationStatus.RUNNING,
            started_at=timezone.now(),
        )
        self.job = Job.objects.create(
            type=JobType.INVOCATION,
            status=JobStatus.RUNNING,
            coordination_version=CoordinationVersion.V2,
            queue_name="worker:worker-a:v2:invocations",
            payload={"dispatch_attempt": 1, "assigned_worker": "worker-a"},
            invocation=self.invocation,
            dispatch_attempts=1,
        )
        self.completion_id = f"{self.job.job_id}:1:invocation"
        self.body = b"staged but hidden"
        self.checksum = hashlib.sha256(self.body).hexdigest()

    def tearDown(self):
        self.media_override.disable()
        self.media.cleanup()

    def stage(self, checksum=None):
        return self.client.post(
            reverse("stage-invocation-output", args=[self.invocation.request_id]),
            data={
                "job_id": str(self.job.job_id),
                "dispatch_attempt": "1",
                "completion_id": self.completion_id,
                "original_path": "report.txt",
                "checksum_sha256": checksum or self.checksum,
                "position": "0",
                "file": SimpleUploadedFile("report.txt", self.body, content_type="text/plain"),
            },
            format="multipart",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

    def commit(self):
        return self.client.post(
            reverse(
                "commit-staged-invocation",
                args=[self.invocation.request_id, self.completion_id],
            ),
            data={
                "job_id": str(self.job.job_id),
                "dispatch_attempt": 1,
                "terminal_status": "succeeded",
                "completion_payload": {
                    "result": {"ok": True},
                    "stdout": "done",
                    "stderr": "",
                    "exit_code": 0,
                    "cold_start": True,
                    "duration_ms": 12,
                },
                "output_manifest": [
                    {
                        "original_path": "report.txt",
                        "size_bytes": len(self.body),
                        "checksum_sha256": self.checksum,
                    }
                ],
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

    def direct_upload_token(self, *, completion_id=None):
        return issue_runner_output_upload_token(
            request_id=self.invocation.request_id,
            job_id=self.job.job_id,
            dispatch_attempt=1,
            completion_id=completion_id or self.completion_id,
        )

    def direct_stage(self, *, token=None, original_path="report.txt", body=None):
        return self.client.post(
            reverse(
                "stage-invocation-output-direct",
                args=[self.invocation.request_id],
            ),
            data=self.body if body is None else body,
            content_type="text/plain",
            HTTP_X_RUNNER_UPLOAD_TOKEN=token or self.direct_upload_token(),
            HTTP_X_JOB_ID=str(self.job.job_id),
            HTTP_X_DISPATCH_ATTEMPT="1",
            HTTP_X_COMPLETION_ID=self.completion_id,
            HTTP_X_ORIGINAL_PATH=original_path,
            HTTP_X_POSITION="0",
        )

    def test_worker_dies_after_upload_staged_data_stays_hidden(self):
        staged = self.stage()
        self.assertEqual(staged.status_code, 201, staged.content)
        output = InvocationOutputFile.objects.get()

        detail = self.client.get(
            f"{reverse('invocation-detail', args=[self.invocation.id])}?response_mode=advanced"
        )
        outputs = self.client.get(reverse("invocation-outputs", args=[self.invocation.id]))
        download = self.client.get(
            reverse("invocation-download-output", args=[self.invocation.id, output.id])
        )

        self.assertEqual(staged.status_code, 201)
        self.assertEqual(output.status, StagedCompletionStatus.STAGED)
        self.assertTrue(output.file.storage.exists(output.file.name))
        self.assertEqual(detail.data["status"], InvocationStatus.RUNNING)
        self.assertEqual(detail.data["result"], {})
        self.assertEqual(detail.data["output_files"], [])
        self.assertEqual(outputs.data, [])
        self.assertEqual(download.status_code, 404)

    def test_commit_is_idempotent_but_hidden_until_terminal_projection(self):
        staged = self.stage()
        self.assertEqual(staged.status_code, 201, staged.content)
        first = self.commit()
        second = self.commit()
        completion = InvocationStagedCompletion.objects.get()

        before = self.client.get(
            f"{reverse('invocation-detail', args=[self.invocation.id])}?response_mode=advanced"
        )
        self.assertEqual(first.status_code, 200)
        self.assertEqual(second.data["artifact_commit_id"], first.data["artifact_commit_id"])
        self.assertEqual(before.data["result"], {})
        self.assertEqual(before.data["output_files"], [])
        self.assertNotIn("log_files", before.data)
        self.assertEqual(InvocationLogArtifact.objects.count(), 1)

        applied = apply_orchestrator_projection(
            {
                "event_type": "job.succeeded",
                "payload": json.dumps(
                    {
                        "job_id": str(self.job.job_id),
                        "job_type": "invocation",
                        "status": "succeeded",
                        "dispatch_attempt": 1,
                        "completion_id": self.completion_id,
                        "artifact_commit_id": str(completion.artifact_commit_id),
                        "payload": {},
                    }
                ),
            }
        )
        after = self.client.get(
            f"{reverse('invocation-detail', args=[self.invocation.id])}?response_mode=advanced"
        )
        outputs = self.client.get(reverse("invocation-outputs", args=[self.invocation.id]))
        logs = self.client.get(f"/api/invocations/{self.invocation.id}/logs/")

        self.assertTrue(applied)
        self.assertEqual(after.data["status"], InvocationStatus.SUCCEEDED)
        self.assertEqual(after.data["result"], {"ok": True})
        self.assertEqual(after.data["stdout"], "done")
        self.assertNotIn("log_files", after.data)
        self.assertEqual(len(outputs.data), 1)
        self.assertEqual(logs.status_code, 404)

    def test_checksum_or_manifest_mismatch_cannot_commit(self):
        bad_upload = self.stage(checksum="0" * 64)
        self.assertEqual(bad_upload.status_code, 400)
        self.assertEqual(InvocationOutputFile.objects.count(), 0)

        staged = self.stage()
        self.assertEqual(staged.status_code, 201, staged.content)
        response = self.client.post(
            reverse(
                "commit-staged-invocation",
                args=[self.invocation.request_id, self.completion_id],
            ),
            data={
                "job_id": str(self.job.job_id),
                "dispatch_attempt": 1,
                "terminal_status": "succeeded",
                "completion_payload": {"result": {"ok": True}},
                "output_manifest": [],
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )
        self.assertEqual(response.status_code, 400)

    def test_direct_runner_upload_stages_without_checksum_and_commits(self):
        staged = self.direct_stage()
        self.assertEqual(staged.status_code, 201, staged.content)
        output = InvocationOutputFile.objects.get()

        response = self.client.post(
            reverse(
                "commit-staged-invocation",
                args=[self.invocation.request_id, self.completion_id],
            ),
            data={
                "job_id": str(self.job.job_id),
                "dispatch_attempt": 1,
                "terminal_status": "succeeded",
                "completion_payload": {"result": {"ok": True}},
                "output_manifest": [
                    {
                        "original_path": "report.txt",
                        "size_bytes": len(self.body),
                    }
                ],
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        output.refresh_from_db()
        self.assertEqual(response.status_code, 200, response.content)
        self.assertEqual(output.checksum_sha256, "")
        self.assertEqual(output.status, StagedCompletionStatus.COMMITTED)

    def test_direct_runner_upload_rejects_invalid_token(self):
        response = self.direct_stage(token="bad-token")

        self.assertEqual(response.status_code, 400)
        self.assertIn("token", str(response.data["output"]).lower())
        self.assertEqual(InvocationOutputFile.objects.count(), 0)

    def test_direct_runner_upload_rejects_undeclared_output(self):
        response = self.direct_stage(original_path="extra.txt")

        self.assertEqual(response.status_code, 400)
        self.assertIn("not declared", str(response.data["output"]))
        self.assertEqual(InvocationOutputFile.objects.count(), 0)

    def test_expired_staged_files_are_deleted(self):
        staged = self.stage()
        self.assertEqual(staged.status_code, 201, staged.content)
        completion = InvocationStagedCompletion.objects.get()
        path = completion.output_files.get().file.path
        completion.expires_at = timezone.now() - timedelta(seconds=1)
        completion.save(update_fields=["expires_at", "updated_at"])

        cleaned = cleanup_expired_staged_completions()

        completion.refresh_from_db()
        self.assertEqual(cleaned, 1)
        self.assertEqual(completion.status, StagedCompletionStatus.EXPIRED)
        self.assertEqual(completion.output_files.count(), 0)
        self.assertFalse(__import__("pathlib").Path(path).exists())
