import io
import uuid
import zipfile
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from apps.functions.models import Function, FunctionVersion
from apps.jobs.models import CoordinationVersion, Job, JobStatus, JobType

from .models import (
    Invocation,
    InvocationOutputFile,
    InvocationStatus,
    InvocationStagedCompletion,
    StagedCompletionStatus,
)


def function_bundle() -> SimpleUploadedFile:
    data = io.BytesIO()
    with zipfile.ZipFile(data, "w") as archive:
        archive.writestr(
            "handler.py",
            "def main(event, context):\n    return {'echo': event}\n",
        )
        archive.writestr("requirements.txt", "")
        archive.writestr("config.json", "{}")
    return SimpleUploadedFile(
        "function.zip",
        data.getvalue(),
        content_type="application/zip",
    )


def authenticate_with_jwt(client, user) -> None:
    access = RefreshToken.for_user(user).access_token
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")


class V2InvocationReadTests(APITestCase):
    def setUp(self):
        self.owner = get_user_model().objects.create_user(username="owner")
        authenticate_with_jwt(self.client, self.owner)
        function = Function.objects.create(
            owner=self.owner,
            name="V2 Reader",
            slug="v2-reader",
        )
        self.version = FunctionVersion.objects.create(
            function=function,
            version="v1",
            source_bundle=function_bundle(),
            image_ref="localhost:5000/functions/v2-reader:v1-v1",
            build_status="built",
            declared_output_files=["report.txt"],
            invocation_output_max_files=1,
            invocation_output_max_file_size_mb=1,
            invocation_output_max_total_size_mb=1,
        )
        self.invocation = Invocation.objects.create(
            function_version=self.version,
            event={"name": "Ilya"},
            status=InvocationStatus.QUEUED,
        )
        self.job = Job.objects.create(
            type=JobType.INVOCATION,
            status=JobStatus.RUNNING,
            coordination_version=CoordinationVersion.V2,
            queue_name="scheduler-pending-invocations-v2",
            invocation=self.invocation,
            payload={"request_id": str(self.invocation.request_id)},
        )

    def redis_state(self, **overrides):
        state = {
            "job_id": str(self.job.job_id),
            "status": "running",
            "dispatch_attempt": "1",
        }
        state.update(overrides)
        return state

    @patch("apps.invocations.v2_reads._read_v2_job_state")
    def test_active_v2_status_overlays_stale_postgres_status(self, read_state):
        read_state.return_value = self.redis_state(status="dispatched")

        response = self.client.get(
            f"{reverse('invocation-detail', args=[self.invocation.id])}?response_mode=advanced"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], InvocationStatus.RUNNING)
        self.assertEqual(response.data["frontend_state"], InvocationStatus.RUNNING)
        self.assertFalse(response.data["is_terminal"])
        self.assertFalse(response.data["result_available"])
        self.assertFalse(response.data["can_download"])
        self.assertEqual(response.data["result"], {})
        self.assertEqual(response.data["output_files"], [])

    @patch("apps.invocations.v2_reads._read_v2_job_state")
    def test_default_detail_returns_simple_pending_response(self, read_state):
        read_state.return_value = self.redis_state(status="running")

        response = self.client.get(reverse("invocation-detail", args=[self.invocation.id]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.invocation.id)
        self.assertEqual(response.data["status"], InvocationStatus.RUNNING)
        self.assertEqual(response.data["poll_after_seconds"], 1)
        self.assertEqual(
            response.data["links"]["self"],
            f"/api/invocations/{self.invocation.id}/?response_mode=simple",
        )
        self.assertNotIn("stdout", response.data)
        self.assertNotIn("stderr", response.data)
        self.assertNotIn("can_download", response.data)

    @patch("apps.invocations.v2_reads._read_v2_job_state")
    def test_terminal_v2_result_is_returned_after_artifact_commit(self, read_state):
        completion = self.create_committed_completion()
        read_state.return_value = self.redis_state(
            status="succeeded",
            completion_id=completion.completion_id,
            artifact_commit_id=str(completion.artifact_commit_id),
        )

        response = self.client.get(
            f"{reverse('invocation-detail', args=[self.invocation.id])}?response_mode=advanced"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], InvocationStatus.SUCCEEDED)
        self.assertEqual(response.data["frontend_state"], InvocationStatus.SUCCEEDED)
        self.assertTrue(response.data["is_terminal"])
        self.assertTrue(response.data["result_available"])
        self.assertTrue(response.data["can_download"])
        self.assertTrue(response.data["outputs_available"])
        self.assertEqual(response.data["result"], {"ok": True})
        self.assertEqual(response.data["stdout"], "done")
        self.assertEqual(response.data["output_files"][0]["original_path"], "report.txt")

    @patch("apps.invocations.v2_reads._read_v2_job_state")
    def test_default_terminal_v2_response_is_simple(self, read_state):
        completion = self.create_committed_completion()
        output = completion.output_files.get()
        read_state.return_value = self.redis_state(
            status="succeeded",
            completion_id=completion.completion_id,
            artifact_commit_id=str(completion.artifact_commit_id),
        )

        response = self.client.get(reverse("invocation-detail", args=[self.invocation.id]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            {
                "result": {"ok": True},
                "output_files": [
                    {
                        "path": "report.txt",
                        "size_bytes": 5,
                        "content_type": "text/plain",
                        "download_url": f"/api/invocations/{self.invocation.id}/outputs/{output.id}/download/",
                    }
                ],
            },
        )
        self.assertNotIn("stdout", response.data)
        self.assertNotIn("stderr", response.data)
        self.assertNotIn("exit_code", response.data)

    @patch("apps.invocations.v2_reads._read_v2_job_state")
    def test_terminal_v2_state_hides_outputs_until_artifact_commit_matches(self, read_state):
        completion = self.create_staged_completion()
        self.create_output_file(completion, status=StagedCompletionStatus.STAGED)
        read_state.return_value = self.redis_state(
            status="succeeded",
            completion_id=completion.completion_id,
            artifact_commit_id=str(uuid.uuid4()),
        )

        detail_response = self.client.get(
            f"{reverse('invocation-detail', args=[self.invocation.id])}?response_mode=advanced"
        )
        outputs_response = self.client.get(
            reverse("invocation-outputs", args=[self.invocation.id])
        )

        self.assertEqual(detail_response.status_code, 200)
        self.assertEqual(detail_response.data["status"], self.invocation.status)
        self.assertEqual(detail_response.data["result"], {})
        self.assertEqual(detail_response.data["output_files"], [])
        self.assertEqual(outputs_response.status_code, 200)
        self.assertEqual(outputs_response.data, [])

    @patch("apps.invocations.v2_reads._read_v2_job_state")
    def test_committed_v2_outputs_can_be_listed_and_downloaded_with_read_token(
        self,
        read_state,
    ):
        completion = self.create_committed_completion()
        output = completion.output_files.get()
        read_state.return_value = self.redis_state(
            status="succeeded",
            completion_id=completion.completion_id,
            artifact_commit_id=str(completion.artifact_commit_id),
        )
        token = self.invocation.issue_read_token()
        self.client.credentials()

        list_response = self.client.get(
            reverse("invocation-outputs", args=[self.invocation.id]),
            HTTP_X_INVOCATION_READ_TOKEN=token,
        )
        download_response = self.client.get(
            reverse("invocation-download-output", args=[self.invocation.id, output.id]),
            HTTP_X_INVOCATION_READ_TOKEN=token,
        )

        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(list_response.data[0]["original_path"], "report.txt")
        self.assertEqual(download_response.status_code, 200)
        self.assertEqual(b"".join(download_response.streaming_content), b"hello")

    @patch("apps.invocations.v2_reads._read_v2_job_state")
    def test_missing_redis_state_falls_back_to_projected_postgres_result(self, read_state):
        read_state.return_value = {}
        self.invocation.status = InvocationStatus.SUCCEEDED
        self.invocation.result = {"projected": True}
        self.invocation.save()

        response = self.client.get(
            f"{reverse('invocation-detail', args=[self.invocation.id])}?response_mode=advanced"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], InvocationStatus.SUCCEEDED)
        self.assertEqual(response.data["result"], {"projected": True})

    def create_staged_completion(self):
        return InvocationStagedCompletion.objects.create(
            invocation=self.invocation,
            job_id=self.job.job_id,
            dispatch_attempt=1,
            completion_id=f"completion-{uuid.uuid4()}",
            status=StagedCompletionStatus.STAGED,
            terminal_status=InvocationStatus.SUCCEEDED,
            result={"ok": True},
            stdout="done",
            duration_ms=123,
        )

    def create_committed_completion(self):
        completion = self.create_staged_completion()
        completion.status = StagedCompletionStatus.COMMITTED
        completion.artifact_commit_id = uuid.uuid4()
        completion.committed_at = timezone.now()
        completion.save()
        self.create_output_file(completion, status=StagedCompletionStatus.COMMITTED)
        return completion

    def create_output_file(self, completion, *, status):
        output = InvocationOutputFile.objects.create(
            invocation=self.invocation,
            staged_completion=completion,
            status=status,
            checksum_sha256="2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
            original_path="report.txt",
            safe_name="report.txt",
            content_type="text/plain",
            size_bytes=5,
            position=0,
        )
        output.file.save("report.txt", ContentFile(b"hello"), save=True)
        return output
