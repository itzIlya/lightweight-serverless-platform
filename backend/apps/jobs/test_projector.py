import io
import json
from unittest.mock import patch
import zipfile

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings

from apps.functions.models import BuildStatus, Function, FunctionVersion
from apps.functions.services import create_build_attempt, enqueue_build_attempt
from apps.invocations.models import Invocation, InvocationStatus
from apps.invocations.services import enqueue_invocation

from .models import CoordinationVersion, Job, JobStatus
from .projector import apply_orchestrator_projection


def bundle():
    data = io.BytesIO()
    with zipfile.ZipFile(data, "w") as archive:
        archive.writestr("handler.py", "def main(event, context): return event\n")
        archive.writestr("requirements.txt", "")
        archive.writestr("config.json", "{}")
    return SimpleUploadedFile("function.zip", data.getvalue())


class V2ProjectorTests(TestCase):
    def setUp(self):
        owner = get_user_model().objects.create_user(username="v2-owner")
        function = Function.objects.create(owner=owner, name="V2", slug="v2")
        self.version = FunctionVersion.objects.create(
            function=function,
            version="v1",
            source_bundle=bundle(),
        )

    def fields(self, job, event_type, **state):
        payload = {
            "job_id": str(job.job_id),
            "job_type": job.type,
            "status": state.pop("status", event_type.removeprefix("job.")),
            "dispatch_attempt": state.pop("dispatch_attempt", 1),
            "assigned_worker": "worker-a",
            "worker_stream": f"worker:worker-a:v2:{job.type}s",
            "payload": job.payload,
            **state,
        }
        return {"event_type": event_type, "payload": json.dumps(payload)}

    @override_settings(V2_BUILD_PILOT_ENABLED=True)
    @patch("redis.Redis.from_url")
    def test_v2_build_uses_outbox_only_and_hides_image_until_finalized(self, redis_from_url):
        attempt = create_build_attempt(self.version)
        enqueue_build_attempt(attempt)
        job = Job.objects.get(build_attempt=attempt)

        self.assertEqual(job.coordination_version, CoordinationVersion.V2)
        self.assertIn(f"-a1-{attempt.request_id.hex[:12]}", job.payload["image_ref"])
        redis_from_url.assert_not_called()

        applied = apply_orchestrator_projection(
            self.fields(job, "job.running", status="running")
        )
        attempt.refresh_from_db()
        self.version.refresh_from_db()
        self.assertTrue(applied)
        self.assertEqual(attempt.status, BuildStatus.BUILDING)
        self.assertEqual(self.version.image_ref, "")

        final_image = f"{job.payload['image_ref']}-d1"
        apply_orchestrator_projection(
            self.fields(
                job,
                "job.succeeded",
                status="succeeded",
                effective_image_ref=final_image,
                artifact_commit_id=final_image,
                completion_payload={"image_ref": final_image, "build_log": "ok"},
            )
        )
        attempt.refresh_from_db()
        self.version.refresh_from_db()
        job.refresh_from_db()
        self.assertEqual(attempt.status, BuildStatus.BUILT)
        self.assertEqual(self.version.build_status, BuildStatus.BUILT)
        self.assertEqual(self.version.image_ref, final_image)
        self.assertEqual(job.status, JobStatus.SUCCEEDED)

    @override_settings(V2_INVOCATION_PILOT_ENABLED=True)
    @patch("redis.Redis.from_url")
    def test_v2_invocation_running_state_is_projected_asynchronously(self, redis_from_url):
        self.version.build_status = BuildStatus.BUILT
        self.version.image_ref = "localhost:5000/functions/v2:ready"
        self.version.save(update_fields=["build_status", "image_ref", "updated_at"])
        invocation = Invocation.objects.create(function_version=self.version, event={})
        enqueue_invocation(invocation)
        job = Job.objects.get(invocation=invocation)

        self.assertEqual(job.coordination_version, CoordinationVersion.V2)
        redis_from_url.assert_not_called()
        apply_orchestrator_projection(
            self.fields(job, "job.running", status="running")
        )
        invocation.refresh_from_db()
        job.refresh_from_db()
        self.assertEqual(invocation.status, InvocationStatus.RUNNING)
        self.assertEqual(job.status, JobStatus.RUNNING)

    @override_settings(V2_BUILD_PILOT_ENABLED=True)
    def test_stale_projection_cannot_overwrite_newer_attempt(self):
        attempt = create_build_attempt(self.version)
        enqueue_build_attempt(attempt)
        job = Job.objects.get(build_attempt=attempt)
        apply_orchestrator_projection(
            self.fields(job, "job.dispatched", dispatch_attempt=2, status="dispatched")
        )

        stale = apply_orchestrator_projection(
            self.fields(job, "job.running", dispatch_attempt=1, status="running")
        )

        job.refresh_from_db()
        attempt.refresh_from_db()
        self.assertFalse(stale)
        self.assertEqual(job.dispatch_attempts, 2)
        self.assertEqual(attempt.status, BuildStatus.QUEUED)
