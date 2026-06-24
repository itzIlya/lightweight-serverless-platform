import io
from unittest.mock import patch
import zipfile

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .models import (
    BuildAttempt,
    BuildLease,
    BuildPolicy,
    BuildStatus,
    Function,
    FunctionVersion,
)
from .services import create_build_attempt


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


class AsyncBuildApiTests(APITestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(username="builder")
        authenticate_with_jwt(self.client, user)
        function = Function.objects.create(
            owner=user,
            name="Echo",
            slug="echo",
        )
        self.version = FunctionVersion.objects.create(
            function=function,
            version="v1",
            source_bundle=function_bundle(),
        )
        BuildPolicy.objects.update_or_create(pk=1, defaults={"max_retries": 2})

    def create_attempt(self, **kwargs):
        return create_build_attempt(self.version, **kwargs)

    def create_version(self, version: str) -> FunctionVersion:
        return FunctionVersion.objects.create(
            function=self.version.function,
            version=version,
            source_bundle=function_bundle(),
        )

    @patch("apps.functions.views.enqueue_build_attempt")
    def test_build_endpoint_creates_first_history_record(self, enqueue):
        response = self.client.post(
            reverse("function-version-build", args=[self.version.id]),
        )

        self.assertEqual(response.status_code, 202)
        attempt = BuildAttempt.objects.get(function_version=self.version)
        self.version.refresh_from_db()
        self.assertEqual(attempt.attempt_number, 1)
        self.assertEqual(attempt.status, BuildStatus.QUEUED)
        self.assertEqual(self.version.build_request_id, attempt.request_id)
        self.assertEqual(self.version.build_status, BuildStatus.QUEUED)
        enqueue.assert_called_once_with(attempt)

    @patch("apps.functions.views.enqueue_build_attempt")
    def test_duplicate_request_does_not_create_another_attempt(self, enqueue):
        self.create_attempt()
        enqueue.reset_mock()

        response = self.client.post(
            reverse("function-version-build", args=[self.version.id]),
        )

        self.assertEqual(response.status_code, 202)
        self.assertEqual(BuildAttempt.objects.count(), 1)
        enqueue.assert_not_called()

    @patch(
        "apps.functions.views.enqueue_build_attempt",
        side_effect=RuntimeError("Redis unavailable"),
    )
    def test_queue_failure_rolls_back_attempt_and_version(self, enqueue):
        response = self.client.post(
            reverse("function-version-build", args=[self.version.id]),
        )

        self.assertEqual(response.status_code, 503)
        self.version.refresh_from_db()
        self.assertEqual(BuildAttempt.objects.count(), 0)
        self.assertEqual(self.version.build_status, BuildStatus.PENDING)
        enqueue.assert_called_once()

    @patch("apps.functions.views.enqueue_build_attempt")
    def test_user_hourly_build_rate_limit_rejects_new_build(self, enqueue):
        BuildPolicy.objects.update_or_create(
            pk=1,
            defaults={
                "max_retries": 2,
                "max_builds_per_user_per_hour": 1,
                "max_builds_per_function_per_hour": 10,
                "max_queued_builds_per_user": 10,
                "max_queued_builds_per_function": 10,
            },
        )
        older = create_build_attempt(self.create_version("older"))
        older.status = BuildStatus.FAILED
        older.finished_at = timezone.now()
        older.save()

        response = self.client.post(
            reverse("function-version-build", args=[self.version.id]),
        )

        self.assertEqual(response.status_code, 429)
        self.assertEqual(response.data["detail"], "Build rate limit exceeded for this user.")
        self.assertIn("retry_after_seconds", response.data)
        enqueue.assert_not_called()

    @patch("apps.functions.views.enqueue_build_attempt")
    def test_function_hourly_build_rate_limit_rejects_new_build(self, enqueue):
        BuildPolicy.objects.update_or_create(
            pk=1,
            defaults={
                "max_retries": 2,
                "max_builds_per_user_per_hour": 10,
                "max_builds_per_function_per_hour": 1,
                "max_queued_builds_per_user": 10,
                "max_queued_builds_per_function": 10,
            },
        )
        older = create_build_attempt(self.create_version("older"))
        older.status = BuildStatus.FAILED
        older.finished_at = timezone.now()
        older.save()

        response = self.client.post(
            reverse("function-version-build", args=[self.version.id]),
        )

        self.assertEqual(response.status_code, 429)
        self.assertEqual(response.data["detail"], "Build rate limit exceeded for this function.")
        enqueue.assert_not_called()

    @patch("apps.functions.views.enqueue_build_attempt")
    def test_queued_depth_limit_rejects_new_build(self, enqueue):
        BuildPolicy.objects.update_or_create(
            pk=1,
            defaults={
                "max_retries": 2,
                "max_builds_per_user_per_hour": 10,
                "max_builds_per_function_per_hour": 10,
                "max_queued_builds_per_user": 1,
                "max_queued_builds_per_function": 10,
            },
        )
        create_build_attempt(self.create_version("queued"))

        response = self.client.post(
            reverse("function-version-build", args=[self.version.id]),
        )

        self.assertEqual(response.status_code, 429)
        self.assertEqual(response.data["detail"], "Too many queued builds for this user.")
        enqueue.assert_not_called()

    @patch("apps.functions.views.enqueue_build_attempt")
    def test_failed_attempt_schedules_retries_up_to_policy(self, enqueue):
        attempt = self.create_attempt()
        enqueue.reset_mock()

        first = self.report(
            attempt,
            status="failed",
            build_log="first failure",
        )
        retry_2 = BuildAttempt.objects.get(attempt_number=2)
        second = self.report(
            retry_2,
            status="failed",
            build_log="second failure",
        )
        retry_3 = BuildAttempt.objects.get(attempt_number=3)
        third = self.report(
            retry_3,
            status="failed",
            build_log="third failure",
        )

        self.assertTrue(first.data["retry_scheduled"])
        self.assertTrue(second.data["retry_scheduled"])
        self.assertFalse(third.data["retry_scheduled"])
        self.assertEqual(BuildAttempt.objects.count(), 3)
        self.assertEqual(enqueue.call_count, 2)
        self.version.refresh_from_db()
        self.assertEqual(self.version.build_status, BuildStatus.FAILED)
        self.assertEqual(self.version.build_request_id, retry_3.request_id)

    @patch("apps.functions.views.enqueue_build_attempt")
    def test_admin_policy_can_disable_retries(self, enqueue):
        BuildPolicy.objects.update_or_create(pk=1, defaults={"max_retries": 0})
        attempt = self.create_attempt()
        enqueue.reset_mock()

        response = self.report(
            attempt,
            status="failed",
            build_log="no retry",
        )

        self.assertFalse(response.data["retry_scheduled"])
        self.assertEqual(BuildAttempt.objects.count(), 1)
        enqueue.assert_not_called()

    def test_build_history_lists_every_attempt(self):
        first = self.create_attempt()
        first.status = BuildStatus.FAILED
        first.finished_at = timezone.now()
        first.save()
        second = self.create_attempt(
            build_id=first.build_id,
            attempt_number=2,
        )

        response = self.client.get(
            reverse("function-version-builds", args=[self.version.id]),
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["request_id"], str(second.request_id))
        self.assertEqual(response.data[1]["request_id"], str(first.request_id))

    def test_queued_build_can_be_cancelled_immediately(self):
        attempt = self.create_attempt()

        response = self.client.post(
            reverse("build-attempt-cancel", args=[attempt.id]),
        )

        self.assertEqual(response.status_code, 200)
        attempt.refresh_from_db()
        self.version.refresh_from_db()
        self.assertEqual(attempt.status, BuildStatus.CANCELLED)
        self.assertEqual(self.version.build_status, BuildStatus.CANCELLED)
        self.assertIsNotNone(attempt.cancel_requested_at)
        self.assertIsNotNone(attempt.finished_at)

    def test_running_build_moves_to_cancelling(self):
        attempt = self.create_attempt()
        attempt.status = BuildStatus.BUILDING
        attempt.started_at = timezone.now()
        attempt.save()

        response = self.client.post(
            reverse("function-version-cancel-build", args=[self.version.id]),
        )

        self.assertEqual(response.status_code, 200)
        attempt.refresh_from_db()
        self.assertEqual(attempt.status, BuildStatus.CANCELLING)
        self.assertIsNotNone(attempt.cancel_requested_at)

    @patch("apps.functions.views.enqueue_build_attempt")
    def test_cancelled_failure_does_not_retry(self, enqueue):
        attempt = self.create_attempt()
        attempt.status = BuildStatus.CANCELLING
        attempt.cancel_requested_at = timezone.now()
        attempt.save()
        enqueue.reset_mock()

        response = self.report(
            attempt,
            status="failed",
            build_log="worker stopped",
        )

        attempt.refresh_from_db()
        self.assertEqual(attempt.status, BuildStatus.CANCELLED)
        self.assertFalse(response.data["retry_scheduled"])
        enqueue.assert_not_called()

    def test_worker_state_endpoint_exposes_cancellation(self):
        attempt = self.create_attempt()
        attempt.cancel_requested_at = timezone.now()
        attempt.status = BuildStatus.CANCELLING
        attempt.save()

        response = self.client.get(
            reverse("get-build-state", args=[attempt.request_id]),
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], BuildStatus.CANCELLING)
        self.assertIsNotNone(response.data["cancel_requested_at"])

    def test_worker_can_download_source_bundle(self):
        attempt = self.create_attempt()
        response = self.client.get(
            reverse("download-build-source", args=[attempt.request_id]),
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(response.status_code, 200)
        body = b"".join(response.streaming_content)
        with zipfile.ZipFile(io.BytesIO(body)) as archive:
            self.assertIn("handler.py", archive.namelist())

    def test_worker_endpoints_require_shared_secret(self):
        attempt = self.create_attempt()
        report_response = self.client.patch(
            reverse("report-build", args=[attempt.request_id]),
            data={"status": "building"},
            format="json",
        )
        state_response = self.client.get(
            reverse("get-build-state", args=[attempt.request_id]),
        )

        self.assertEqual(report_response.status_code, 401)
        self.assertEqual(state_response.status_code, 401)

    def test_worker_can_acquire_and_release_build_lease(self):
        attempt = self.create_attempt()

        acquire_response = self.client.post(
            reverse("acquire-build-lease", args=[attempt.request_id]),
            data={
                "worker_name": "worker-a",
                "hostname": "worker-a.local",
                "max_build_concurrency": 1,
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )
        lease = BuildLease.objects.get(build_attempt=attempt)
        release_response = self.client.post(
            reverse("release-build-lease", args=[attempt.request_id]),
            data={
                "lease_id": lease.id,
                "reason": "test complete",
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(acquire_response.status_code, 200)
        self.assertTrue(acquire_response.data["granted"])
        self.assertEqual(acquire_response.data["worker"], "worker-a")
        self.assertEqual(release_response.status_code, 200)
        self.assertEqual(release_response.data["released"], 1)
        lease.refresh_from_db()
        self.assertEqual(lease.status, "released")

    def test_worker_build_lease_respects_global_concurrency_limit(self):
        BuildPolicy.objects.update_or_create(
            pk=1,
            defaults={
                "max_retries": 2,
                "max_concurrent_builds": 1,
            },
        )
        first = self.create_attempt()
        second = create_build_attempt(self.create_version("v2"))
        self.client.post(
            reverse("acquire-build-lease", args=[first.request_id]),
            data={"worker_name": "worker-a"},
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        response = self.client.post(
            reverse("acquire-build-lease", args=[second.request_id]),
            data={"worker_name": "worker-b"},
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.data["granted"])
        self.assertEqual(
            response.data["reason"],
            "Global build concurrency limit reached.",
        )

    def test_unbuilt_version_cannot_be_invoked(self):
        response = self.client.post(
            reverse("function-invoke", args=[self.version.function_id]),
            data={"event": {"name": "Ilya"}},
            format="json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("version", response.data)

    def report(self, attempt, **payload):
        payload.setdefault("build_finished_at", timezone.now().isoformat())
        return self.client.patch(
            reverse("report-build", args=[attempt.request_id]),
            data=payload,
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )
