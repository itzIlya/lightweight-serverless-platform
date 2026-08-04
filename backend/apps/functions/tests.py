import io
from unittest.mock import patch
import zipfile

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from apps.invocations.models import Invocation, InvocationInputFile

from .models import (
    BuildAttempt,
    BuildLease,
    BuildPolicy,
    BuildStatus,
    Function,
    FunctionImage,
    FunctionImageStatus,
    FunctionVersion,
)
from .services import cleanup_pending_function_images, create_build_attempt


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


class FunctionSourceReplacementTests(APITestCase):
    def setUp(self):
        self.owner = get_user_model().objects.create_user(username="source-owner")
        self.other = get_user_model().objects.create_user(username="source-other")
        authenticate_with_jwt(self.client, self.owner)
        self.function = Function.objects.create(
            owner=self.owner,
            name="Replaceable",
            slug="replaceable",
        )
        self.active_version = FunctionVersion.objects.create(
            function=self.function,
            version="v1",
            source_bundle=function_bundle(),
            image_ref="localhost:5000/functions/replaceable:v1",
            build_status=BuildStatus.BUILT,
            config={"old": True},
            declared_output_files=["report.txt"],
        )
        self.function.active_version = self.active_version
        self.function.save(update_fields=["active_version"])
        BuildPolicy.objects.update_or_create(
            pk=1,
            defaults={
                "max_retries": 0,
                "max_builds_per_user_per_hour": 20,
                "max_builds_per_function_per_hour": 10,
                "max_queued_builds_per_user": 5,
                "max_queued_builds_per_function": 3,
            },
        )

    @patch("apps.functions.views.enqueue_build_attempt")
    def test_source_replacement_creates_candidate_without_switching_active(self, enqueue):
        response = self.client.post(
            reverse("function-replace-source", args=[self.function.id]),
            data={"source_bundle": function_bundle()},
            format="multipart",
        )

        self.assertEqual(response.status_code, 202, response.content)
        candidate = FunctionVersion.objects.exclude(pk=self.active_version.pk).get()
        attempt = BuildAttempt.objects.get(function_version=candidate)
        self.function.refresh_from_db()
        self.assertEqual(self.function.active_version_id, self.active_version.id)
        self.assertEqual(candidate.build_status, BuildStatus.QUEUED)
        self.assertEqual(candidate.config, {"old": True})
        self.assertEqual(candidate.declared_output_files, ["report.txt"])
        self.assertEqual(attempt.status, BuildStatus.QUEUED)
        enqueue.assert_called_once_with(attempt)

    @patch("apps.functions.views.enqueue_invocation")
    def test_default_invocation_uses_active_version_while_candidate_is_queued(self, enqueue):
        candidate = FunctionVersion.objects.create(
            function=self.function,
            version="r2",
            source_bundle=function_bundle(),
            build_status=BuildStatus.QUEUED,
        )

        response = self.client.post(
            reverse("function-invoke", args=[self.function.id]),
            data={"event": {"name": "Ilya"}},
            format="json",
        )

        self.assertEqual(response.status_code, 202, response.content)
        invocation = response.data["id"]
        from apps.invocations.models import Invocation

        record = Invocation.objects.get(pk=invocation)
        self.assertEqual(record.function_version_id, self.active_version.id)
        self.assertNotEqual(record.function_version_id, candidate.id)
        enqueue.assert_called_once()

    @patch("apps.functions.views.enqueue_build_attempt")
    def test_successful_candidate_build_promotes_active_version(self, enqueue):
        FunctionImage.objects.create(
            function=self.function,
            function_version=self.active_version,
            image_ref=self.active_version.image_ref,
            status=FunctionImageStatus.ACTIVE,
        )
        replacement = self.client.post(
            reverse("function-replace-source", args=[self.function.id]),
            data={"source_bundle": function_bundle()},
            format="multipart",
        )
        candidate = FunctionVersion.objects.get(
            pk=replacement.data["candidate_version"]["id"]
        )
        attempt = BuildAttempt.objects.get(function_version=candidate)

        report = self.client.patch(
            reverse("report-build", args=[attempt.request_id]),
            data={
                "status": BuildStatus.BUILT,
                "image_ref": "localhost:5000/functions/replaceable:r2",
                "build_log": "built",
                "build_finished_at": timezone.now().isoformat(),
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(report.status_code, 200, report.content)
        candidate.refresh_from_db()
        self.function.refresh_from_db()
        self.assertEqual(candidate.build_status, BuildStatus.BUILT)
        self.assertEqual(self.function.active_version_id, candidate.id)
        self.assertEqual(candidate.image_ref, "localhost:5000/functions/replaceable:r2")
        new_image = FunctionImage.objects.get(image_ref=candidate.image_ref)
        old_image = FunctionImage.objects.get(image_ref=self.active_version.image_ref)
        self.assertEqual(new_image.status, FunctionImageStatus.ACTIVE)
        self.assertEqual(old_image.status, FunctionImageStatus.PENDING_DELETE)

    @patch("apps.functions.views.enqueue_build_attempt")
    def test_failed_candidate_build_keeps_previous_active_version(self, enqueue):
        replacement = self.client.post(
            reverse("function-replace-source", args=[self.function.id]),
            data={"source_bundle": function_bundle()},
            format="multipart",
        )
        candidate = FunctionVersion.objects.get(
            pk=replacement.data["candidate_version"]["id"]
        )
        attempt = BuildAttempt.objects.get(function_version=candidate)

        report = self.client.patch(
            reverse("report-build", args=[attempt.request_id]),
            data={
                "status": BuildStatus.FAILED,
                "image_ref": "localhost:5000/functions/replaceable:failed-r2",
                "build_log": "failed",
                "build_finished_at": timezone.now().isoformat(),
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(report.status_code, 200, report.content)
        candidate.refresh_from_db()
        self.function.refresh_from_db()
        self.assertEqual(candidate.build_status, BuildStatus.FAILED)
        self.assertEqual(self.function.active_version_id, self.active_version.id)
        failed_image = FunctionImage.objects.get(image_ref=candidate.image_ref)
        self.assertEqual(failed_image.status, FunctionImageStatus.PENDING_DELETE)

    @patch("apps.functions.views.enqueue_build_attempt")
    def test_other_user_cannot_replace_source(self, enqueue):
        authenticate_with_jwt(self.client, self.other)

        response = self.client.post(
            reverse("function-replace-source", args=[self.function.id]),
            data={"source_bundle": function_bundle()},
            format="multipart",
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(FunctionVersion.objects.count(), 1)
        enqueue.assert_not_called()

    @patch("apps.functions.views.enqueue_build_attempt")
    def test_function_detail_exposes_user_facing_build_summary(self, enqueue):
        replacement = self.client.post(
            reverse("function-replace-source", args=[self.function.id]),
            data={"source_bundle": function_bundle()},
            format="multipart",
        )
        candidate_id = replacement.data["candidate_version"]["id"]

        response = self.client.get(reverse("function-detail", args=[self.function.id]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["active_version"]["id"], self.active_version.id)
        self.assertEqual(response.data["active_image_ref"], self.active_version.image_ref)
        self.assertEqual(response.data["build_status"], BuildStatus.QUEUED)
        self.assertEqual(response.data["pending_build"]["version_id"], candidate_id)
        self.assertEqual(
            response.data["links"]["build_status"],
            f"/api/functions/{self.function.id}/build-status/",
        )
        self.assertEqual(
            response.data["links"]["tokens"],
            f"/api/functions/{self.function.id}/tokens/",
        )

    @patch("apps.functions.views.enqueue_build_attempt")
    def test_build_status_endpoint_exposes_frontend_poll_contract(self, enqueue):
        replacement = self.client.post(
            reverse("function-replace-source", args=[self.function.id]),
            data={"source_bundle": function_bundle()},
            format="multipart",
        )
        candidate_id = replacement.data["candidate_version"]["id"]

        response = self.client.get(reverse("function-build-status", args=[self.function.id]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["resource"], "build")
        self.assertEqual(response.data["function_id"], self.function.id)
        self.assertEqual(response.data["state"], BuildStatus.QUEUED)
        self.assertEqual(response.data["frontend_state"], BuildStatus.QUEUED)
        self.assertFalse(response.data["is_terminal"])
        self.assertEqual(response.data["poll_after_seconds"], 1)
        self.assertTrue(response.data["can_cancel"])
        self.assertTrue(response.data["can_invoke"])
        self.assertEqual(
            response.data["links"]["invoke"],
            f"/api/functions/{self.function.id}/invoke/",
        )
        self.assertEqual(response.data["active_version"]["id"], self.active_version.id)
        self.assertEqual(response.data["pending_version"]["id"], candidate_id)
        self.assertEqual(response.data["latest_attempt"]["status"], BuildStatus.QUEUED)

    def test_function_invocations_action_lists_only_that_function(self):
        other_function = Function.objects.create(
            owner=self.owner,
            name="Other",
            slug="other",
        )
        other_version = FunctionVersion.objects.create(
            function=other_function,
            version="v1",
            source_bundle=function_bundle(),
            image_ref="localhost:5000/functions/other:v1",
            build_status=BuildStatus.BUILT,
        )
        mine = Invocation.objects.create(function_version=self.active_version)
        Invocation.objects.create(function_version=other_version)

        response = self.client.get(reverse("function-invocations", args=[self.function.id]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], mine.id)

    def test_function_invocations_action_filters_status_and_limit(self):
        first = Invocation.objects.create(
            function_version=self.active_version,
            status="succeeded",
        )
        Invocation.objects.create(
            function_version=self.active_version,
            status="failed",
        )
        latest = Invocation.objects.create(
            function_version=self.active_version,
            status="succeeded",
        )

        response = self.client.get(
            reverse("function-invocations", args=[self.function.id]),
            data={"status": "succeeded", "limit": "1"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], latest.id)
        self.assertNotEqual(response.data[0]["id"], first.id)

    def test_pending_image_cleanup_deletes_non_active_image(self):
        image = FunctionImage.objects.create(
            function=self.function,
            function_version=self.active_version,
            image_ref="localhost:5000/functions/replaceable:old",
            status=FunctionImageStatus.PENDING_DELETE,
            delete_after=timezone.now(),
        )

        result = cleanup_pending_function_images(
            delete_image=lambda image_ref, registry_base_url: True,
        )

        image.refresh_from_db()
        self.assertEqual(result["deleted"], 1)
        self.assertEqual(image.status, FunctionImageStatus.DELETED)
        self.assertIsNotNone(image.deleted_at)

    def test_pending_image_cleanup_skips_current_active_image(self):
        image = FunctionImage.objects.create(
            function=self.function,
            function_version=self.active_version,
            image_ref=self.active_version.image_ref,
            status=FunctionImageStatus.PENDING_DELETE,
            delete_after=timezone.now(),
        )
        deleted = []

        result = cleanup_pending_function_images(
            delete_image=lambda image_ref, registry_base_url: deleted.append(image_ref),
        )

        image.refresh_from_db()
        self.assertEqual(result["skipped_active"], 1)
        self.assertEqual(deleted, [])
        self.assertEqual(image.status, FunctionImageStatus.ACTIVE)

    def test_cleanup_command_runs_function_image_cleanup(self):
        with patch(
            "apps.functions.management.commands.cleanup_function_images.cleanup_pending_function_images",
            return_value={"checked": 1, "deleted": 1, "failed": 0, "skipped_active": 0},
        ) as cleanup:
            call_command(
                "cleanup_function_images",
                registry_base_url="http://registry:5000",
                stdout=io.StringIO(),
            )

        cleanup.assert_called_once_with(
            registry_base_url="http://registry:5000",
            batch_size=100,
        )

    def test_delete_function_removes_sources_artifacts_and_schedules_images(self):
        FunctionImage.objects.create(
            function=self.function,
            function_version=self.active_version,
            image_ref=self.active_version.image_ref,
            status=FunctionImageStatus.ACTIVE,
        )
        source_storage = self.active_version.source_bundle.storage
        source_name = self.active_version.source_bundle.name
        invocation = Invocation.objects.create(function_version=self.active_version)
        input_file = InvocationInputFile.objects.create(
            invocation=invocation,
            position=0,
            original_name="payload.txt",
            content_type="text/plain",
            size_bytes=5,
            file=SimpleUploadedFile("payload.txt", b"hello"),
        )
        input_storage = input_file.file.storage
        input_name = input_file.file.name

        response = self.client.delete(reverse("function-detail", args=[self.function.id]))

        self.assertEqual(response.status_code, 204)
        self.assertFalse(Function.objects.filter(pk=self.function.pk).exists())
        self.assertFalse(source_storage.exists(source_name))
        self.assertFalse(input_storage.exists(input_name))
        image = FunctionImage.objects.get(image_ref=self.active_version.image_ref)
        self.assertEqual(image.status, FunctionImageStatus.PENDING_DELETE)
        self.assertIsNone(image.function_id)
        self.assertIsNone(image.function_version_id)
