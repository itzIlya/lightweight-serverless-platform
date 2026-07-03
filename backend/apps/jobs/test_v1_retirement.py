import uuid
from unittest.mock import Mock

from django.core.management import CommandError, call_command
from django.test import TestCase, override_settings
from django.urls import reverse
from rest_framework.test import APIClient

from .models import CoordinationVersion, Job, JobStatus, JobType
from .v1_retirement import v1_retirement_status


class V1RetirementTests(TestCase):
    def setUp(self):
        self.redis = Mock()
        self.pipeline = self.redis.pipeline.return_value

    def test_readiness_requires_terminal_jobs_and_empty_known_queues(self):
        job = Job.objects.create(
            type=JobType.INVOCATION,
            status=JobStatus.RUNNING,
            coordination_version=CoordinationVersion.V1,
            queue_name="worker:a:invocations",
        )
        self.pipeline.execute.return_value = [0, 0, 0, 0]

        active = v1_retirement_status(self.redis)
        job.status = JobStatus.SUCCEEDED
        job.save(update_fields=["status", "updated_at"])
        drained = v1_retirement_status(self.redis)

        self.assertFalse(active["ready"])
        self.assertEqual(active["active_job_total"], 1)
        self.assertTrue(drained["ready"])
        self.redis.pipeline.assert_called_with(transaction=False)

    def test_queue_retirement_requires_explicit_confirmation(self):
        with self.assertRaisesRegex(CommandError, "--confirm RETIRE_V1"):
            call_command("retire_v1_queues")

    @override_settings(V1_COORDINATION_ENDPOINTS_ENABLED=False)
    def test_v1_coordination_and_report_endpoints_return_gone(self):
        client = APIClient()
        job = Job.objects.create(
            type=JobType.INVOCATION,
            status=JobStatus.QUEUED,
            coordination_version=CoordinationVersion.V1,
            queue_name="scheduler-pending-invocations",
        )
        headers = {"HTTP_X_INTERNAL_TOKEN": "change-me"}

        dispatch = client.post(
            reverse("dispatch-scheduler-job", args=[job.job_id]),
            data={"worker_name": "a", "queue_name": "worker:a:invocations"},
            format="json",
            **headers,
        )
        claim = client.post(
            reverse("claim-worker-job", args=[job.job_id]),
            data={"worker_name": "a", "dispatch_attempt": 1},
            format="json",
            **headers,
        )
        invocation_report = client.patch(
            reverse("report-invocation", args=[uuid.uuid4()]),
            data={"status": "failed"},
            format="json",
            **headers,
        )
        build_report = client.patch(
            reverse("report-build", args=[uuid.uuid4()]),
            data={"status": "failed"},
            format="json",
            **headers,
        )

        self.assertEqual(dispatch.status_code, 410)
        self.assertEqual(claim.status_code, 410)
        self.assertEqual(invocation_report.status_code, 410)
        self.assertEqual(build_report.status_code, 410)
