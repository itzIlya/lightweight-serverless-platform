import io
from unittest.mock import Mock, patch
import zipfile

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from rest_framework.test import APITestCase

from apps.functions.models import BuildStatus, Function, FunctionVersion
from apps.functions.services import create_build_attempt, enqueue_build_attempt
from apps.invocations.models import Invocation
from apps.invocations.services import enqueue_invocation
from apps.workers.models import WorkerNode

from .models import CoordinationVersion, Job, JobStatus, JobType, OutboxEvent
from .outbox import publish_pending_outbox_events
from .services import create_build_job_record


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


class DurableJobRecordTests(APITestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(username="job-owner")
        function = Function.objects.create(owner=user, name="Jobs", slug="jobs")
        self.version = FunctionVersion.objects.create(
            function=function,
            version="v1",
            source_bundle=function_bundle(),
            image_ref="localhost:5000/functions/jobs:v1-v1",
            build_status=BuildStatus.BUILT,
            declared_output_files=["report.txt", "summary.json"],
            invocation_output_max_files=2,
            invocation_output_max_file_size_mb=3,
            invocation_output_max_total_size_mb=10,
        )

    @patch("redis.Redis.from_url")
    def test_build_enqueue_creates_durable_job_record(self, redis_from_url):
        redis_client = Mock()
        redis_from_url.return_value = redis_client
        attempt = create_build_attempt(self.version)

        payload = enqueue_build_attempt(attempt)

        job = Job.objects.get(build_attempt=attempt)
        self.assertEqual(job.type, JobType.BUILD)
        self.assertEqual(job.status, JobStatus.QUEUED)
        self.assertEqual(job.coordination_version, CoordinationVersion.V1)
        self.assertEqual(job.payload["job_id"], str(job.job_id))
        self.assertEqual(payload["job_id"], str(job.job_id))
        event = OutboxEvent.objects.get(aggregate_id=job.job_id)
        self.assertEqual(event.event_type, "job.created")
        self.assertEqual(event.payload["coordination_version"], CoordinationVersion.V1)
        self.assertEqual(event.payload["payload"]["job_id"], str(job.job_id))
        redis_client.rpush.assert_called_once_with(
            "scheduler-pending-builds",
            str(job.job_id),
        )

    @patch("redis.Redis.from_url")
    def test_invocation_enqueue_creates_durable_job_record(self, redis_from_url):
        redis_client = Mock()
        redis_from_url.return_value = redis_client
        invocation = Invocation.objects.create(
            function_version=self.version,
            event={"hello": "world"},
        )

        payload = enqueue_invocation(invocation)

        job = Job.objects.get(invocation=invocation)
        self.assertEqual(job.type, JobType.INVOCATION)
        self.assertEqual(job.status, JobStatus.QUEUED)
        self.assertEqual(job.coordination_version, CoordinationVersion.V2)
        self.assertEqual(job.payload["job_id"], str(job.job_id))
        self.assertEqual(
            job.payload["declared_output_files"],
            ["report.txt", "summary.json"],
        )
        self.assertEqual(job.payload["invocation_output_max_files"], 2)
        self.assertEqual(job.payload["invocation_output_max_file_size_mb"], 3)
        self.assertEqual(job.payload["invocation_output_max_total_size_mb"], 10)
        self.assertEqual(job.payload["invocation_max_retries"], 0)
        self.assertEqual(job.payload["invocation_retry_backoff_seconds"], [])
        self.assertFalse(job.payload["retry_invocation_timeouts"])
        self.assertFalse(job.payload["retry_invocation_function_errors"])
        self.assertEqual(payload["job_id"], str(job.job_id))
        event = OutboxEvent.objects.get(aggregate_id=job.job_id)
        self.assertEqual(event.event_type, "job.created")
        self.assertEqual(event.payload["job_type"], JobType.INVOCATION)
        self.assertEqual(event.payload["coordination_version"], CoordinationVersion.V2)
        redis_client.rpush.assert_not_called()

    @patch("redis.Redis.from_url")
    def test_build_report_updates_durable_job_status(self, redis_from_url):
        redis_from_url.return_value = Mock()
        attempt = create_build_attempt(self.version)
        enqueue_build_attempt(attempt)

        running = self.client.patch(
            reverse("report-build", args=[attempt.request_id]),
            data={
                "status": BuildStatus.BUILDING,
                "build_started_at": timezone.now().isoformat(),
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )
        built = self.client.patch(
            reverse("report-build", args=[attempt.request_id]),
            data={
                "status": BuildStatus.BUILT,
                "image_ref": "localhost:5000/functions/jobs:v1-v1",
                "build_finished_at": timezone.now().isoformat(),
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(running.status_code, 200)
        self.assertEqual(built.status_code, 200)
        job = Job.objects.get(build_attempt=attempt)
        self.assertEqual(job.status, JobStatus.SUCCEEDED)

    @patch("redis.Redis.from_url")
    def test_invocation_report_updates_durable_job_status(self, redis_from_url):
        redis_from_url.return_value = Mock()
        invocation = Invocation.objects.create(
            function_version=self.version,
            event={},
        )
        enqueue_invocation(invocation)

        running = self.client.patch(
            reverse("report-invocation", args=[invocation.request_id]),
            data={
                "status": "running",
                "started_at": timezone.now().isoformat(),
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )
        succeeded = self.client.patch(
            reverse("report-invocation", args=[invocation.request_id]),
            data={
                "status": "succeeded",
                "result": {"ok": True},
                "finished_at": timezone.now().isoformat(),
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(running.status_code, 200)
        self.assertEqual(succeeded.status_code, 200)
        job = Job.objects.get(invocation=invocation)
        self.assertEqual(job.status, JobStatus.SUCCEEDED)

    def test_worker_can_register_for_scheduler_placement(self):
        response = self.client.post(
            reverse("register-worker"),
            data={
                "name": "worker-a",
                "hostname": "worker-a.local",
                "max_concurrency": 2,
                "max_build_concurrency": 1,
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(response.status_code, 200)
        worker = WorkerNode.objects.get(name="worker-a")
        self.assertEqual(worker.hostname, "worker-a.local")
        self.assertEqual(worker.max_concurrency, 2)
        self.assertEqual(worker.max_build_concurrency, 1)

    def test_worker_can_send_heartbeat(self):
        WorkerNode.objects.create(
            name="worker-a",
            hostname="worker-a.local",
            status="offline",
        )

        response = self.client.patch(
            reverse("heartbeat-worker"),
            data={
                "name": "worker-a",
                "active_jobs": 1,
                "active_builds": 0,
                "active_invocations": 1,
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(response.status_code, 200)
        worker = WorkerNode.objects.get(name="worker-a")
        self.assertEqual(worker.status, "online")
        self.assertEqual(worker.metadata["active_jobs"], 1)
        self.assertEqual(worker.metadata["active_builds"], 0)
        self.assertEqual(worker.metadata["active_invocations"], 1)
        self.assertIsNotNone(worker.last_seen_at)

    @patch("redis.Redis.from_url")
    def test_scheduler_can_read_and_dispatch_queued_job(self, redis_from_url):
        redis_from_url.return_value = Mock()
        WorkerNode.objects.create(
            name="worker-a",
            hostname="worker-a.local",
        )
        attempt = create_build_attempt(self.version)
        enqueue_build_attempt(attempt)
        job = Job.objects.get(build_attempt=attempt)

        get_response = self.client.get(
            reverse("get-scheduler-job", args=[job.job_id]),
            HTTP_X_INTERNAL_TOKEN="change-me",
        )
        workers_response = self.client.get(
            reverse("list-scheduler-workers"),
            HTTP_X_INTERNAL_TOKEN="change-me",
        )
        dispatch_response = self.client.post(
            reverse("dispatch-scheduler-job", args=[job.job_id]),
            data={
                "worker_name": "worker-a",
                "queue_name": "worker:worker-a:jobs",
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(get_response.data["status"], JobStatus.QUEUED)
        self.assertEqual(
            get_response.data["coordination_version"],
            CoordinationVersion.V1,
        )
        self.assertEqual(workers_response.status_code, 200)
        self.assertEqual(
            workers_response.data[0]["invocation_queue_name"],
            "worker:worker-a:invocations",
        )
        self.assertEqual(
            workers_response.data[0]["build_queue_name"],
            "worker:worker-a:builds",
        )
        self.assertEqual(dispatch_response.status_code, 200)
        self.assertTrue(dispatch_response.data["dispatched"])
        job.refresh_from_db()
        self.assertEqual(job.status, JobStatus.DISPATCHED)
        self.assertEqual(job.queue_name, "worker:worker-a:jobs")
        self.assertEqual(job.dispatch_attempts, 1)
        self.assertEqual(job.payload["dispatch_attempt"], 1)

    @patch("redis.Redis.from_url")
    def test_scheduler_does_not_dispatch_job_before_available_at(self, redis_from_url):
        redis_from_url.return_value = Mock()
        WorkerNode.objects.create(
            name="worker-a",
            hostname="worker-a.local",
        )
        attempt = create_build_attempt(self.version)
        enqueue_build_attempt(attempt)
        job = Job.objects.get(build_attempt=attempt)
        job.available_at = timezone.now() + timedelta(seconds=30)
        job.save(update_fields=["available_at", "updated_at"])

        dispatch_response = self.client.post(
            reverse("dispatch-scheduler-job", args=[job.job_id]),
            data={
                "worker_name": "worker-a",
                "queue_name": "worker:worker-a:jobs",
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(dispatch_response.status_code, 200)
        self.assertFalse(dispatch_response.data["dispatched"])
        self.assertEqual(dispatch_response.data["status"], JobStatus.QUEUED)
        self.assertIn("not available", dispatch_response.data["detail"])
        job.refresh_from_db()
        self.assertEqual(job.status, JobStatus.QUEUED)
        self.assertEqual(job.dispatch_attempts, 0)

    def test_outbox_failure_rolls_back_job_creation(self):
        attempt = create_build_attempt(self.version)

        with patch.object(OutboxEvent.objects, "create", side_effect=RuntimeError("db error")):
            with self.assertRaisesRegex(RuntimeError, "db error"):
                create_build_job_record(attempt, {"type": "build"})

        self.assertFalse(Job.objects.filter(build_attempt=attempt).exists())

    @patch("redis.Redis.from_url")
    def test_worker_can_claim_dispatched_job(self, redis_from_url):
        redis_from_url.return_value = Mock()
        WorkerNode.objects.create(
            name="worker-a",
            hostname="worker-a.local",
        )
        attempt = create_build_attempt(self.version)
        enqueue_build_attempt(attempt)
        job = Job.objects.get(build_attempt=attempt)
        self.client.post(
            reverse("dispatch-scheduler-job", args=[job.job_id]),
            data={
                "worker_name": "worker-a",
                "queue_name": "worker:worker-a:jobs",
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )
        job.refresh_from_db()

        claim_response = self.client.post(
            reverse("claim-worker-job", args=[job.job_id]),
            data={
                "worker_name": "worker-a",
                "dispatch_attempt": job.payload["dispatch_attempt"],
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(claim_response.status_code, 200)
        self.assertTrue(claim_response.data["claimed"])
        self.assertEqual(
            claim_response.data["job"]["payload"]["assigned_worker"],
            "worker-a",
        )
        job.refresh_from_db()
        self.assertEqual(job.status, JobStatus.RUNNING)

    @patch("redis.Redis.from_url")
    def test_worker_claim_rejects_wrong_worker_or_attempt(self, redis_from_url):
        redis_from_url.return_value = Mock()
        WorkerNode.objects.create(
            name="worker-a",
            hostname="worker-a.local",
        )
        attempt = create_build_attempt(self.version)
        enqueue_build_attempt(attempt)
        job = Job.objects.get(build_attempt=attempt)
        self.client.post(
            reverse("dispatch-scheduler-job", args=[job.job_id]),
            data={
                "worker_name": "worker-a",
                "queue_name": "worker:worker-a:jobs",
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )
        job.refresh_from_db()

        claim_response = self.client.post(
            reverse("claim-worker-job", args=[job.job_id]),
            data={
                "worker_name": "worker-b",
                "dispatch_attempt": job.payload["dispatch_attempt"] + 1,
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(claim_response.status_code, 200)
        self.assertFalse(claim_response.data["claimed"])
        self.assertTrue(claim_response.data["stale"])
        job.refresh_from_db()
        self.assertEqual(job.status, JobStatus.DISPATCHED)

    @patch("redis.Redis.from_url")
    def test_worker_claim_rejects_recovered_delivery_before_execution(self, redis_from_url):
        redis_from_url.return_value = Mock()
        WorkerNode.objects.create(
            name="worker-a",
            hostname="worker-a.local",
        )
        attempt = create_build_attempt(self.version)
        enqueue_build_attempt(attempt)
        job = Job.objects.get(build_attempt=attempt)
        self.client.post(
            reverse("dispatch-scheduler-job", args=[job.job_id]),
            data={
                "worker_name": "worker-a",
                "queue_name": "worker:worker-a:jobs",
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )
        job.refresh_from_db()
        old_attempt = job.payload["dispatch_attempt"]
        self.client.post(
            reverse("requeue-scheduler-job", args=[job.job_id]),
            data={
                "worker_name": "worker-a",
                "reason": "Worker missed heartbeat.",
                "recovery": True,
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        claim_response = self.client.post(
            reverse("claim-worker-job", args=[job.job_id]),
            data={
                "worker_name": "worker-a",
                "dispatch_attempt": old_attempt,
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(claim_response.status_code, 200)
        self.assertFalse(claim_response.data["claimed"])
        self.assertTrue(claim_response.data["stale"])
        self.assertEqual(claim_response.data["status"], JobStatus.QUEUED)
        job.refresh_from_db()
        self.assertEqual(job.status, JobStatus.QUEUED)

    @patch("redis.Redis.from_url")
    def test_scheduler_can_expire_stale_workers_and_requeue_job(self, redis_from_url):
        redis_from_url.return_value = Mock()
        WorkerNode.objects.create(
            name="worker-a",
            hostname="worker-a.local",
            last_seen_at=timezone.now() - timedelta(seconds=120),
        )
        attempt = create_build_attempt(self.version)
        enqueue_build_attempt(attempt)
        job = Job.objects.get(build_attempt=attempt)
        self.client.post(
            reverse("dispatch-scheduler-job", args=[job.job_id]),
            data={
                "worker_name": "worker-a",
                "queue_name": "worker:worker-a:jobs",
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        expired_response = self.client.post(
            reverse("expire-stale-scheduler-workers"),
            data={"stale_after_seconds": 30},
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )
        requeue_response = self.client.post(
            reverse("requeue-scheduler-job", args=[job.job_id]),
            data={
                "worker_name": "worker-a",
                "reason": "Worker missed heartbeat.",
                "recovery": True,
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(expired_response.status_code, 200)
        self.assertEqual(expired_response.data["expired"][0]["name"], "worker-a")
        self.assertEqual(
            expired_response.data["expired"][0]["processing_queue_name"],
            "worker:worker-a:processing",
        )
        self.assertEqual(requeue_response.status_code, 200)
        self.assertTrue(requeue_response.data["requeued"])
        job.refresh_from_db()
        self.assertEqual(job.status, JobStatus.QUEUED)
        self.assertEqual(job.queue_name, "scheduler-pending-builds")
        self.assertEqual(job.recovery_count, 1)
        self.assertNotIn("assigned_worker", job.payload)

    @patch("redis.Redis.from_url")
    def test_invocation_recovery_uses_fast_backoff(self, redis_from_url):
        redis_from_url.return_value = Mock()
        WorkerNode.objects.create(
            name="worker-a",
            hostname="worker-a.local",
        )
        invocation = Invocation.objects.create(
            function_version=self.version,
            event={},
        )
        enqueue_invocation(invocation)
        job = Job.objects.get(invocation=invocation)
        self.client.post(
            reverse("dispatch-scheduler-job", args=[job.job_id]),
            data={
                "worker_name": "worker-a",
                "queue_name": "worker:worker-a:jobs",
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        first = self.client.post(
            reverse("requeue-scheduler-job", args=[job.job_id]),
            data={
                "worker_name": "worker-a",
                "reason": "Worker missed heartbeat.",
                "recovery": True,
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )
        job.refresh_from_db()
        first_available_at = job.available_at
        job.status = JobStatus.DISPATCHED
        job.queue_name = "worker:worker-a:jobs"
        job.payload["assigned_worker"] = "worker-a"
        job.save(update_fields=["status", "queue_name", "payload", "updated_at"])
        second_started_at = timezone.now()
        second = self.client.post(
            reverse("requeue-scheduler-job", args=[job.job_id]),
            data={
                "worker_name": "worker-a",
                "reason": "Worker missed heartbeat again.",
                "recovery": True,
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(first.status_code, 200)
        self.assertEqual(first.data["recovery_delay_seconds"], 0)
        self.assertEqual(second.status_code, 200)
        self.assertEqual(second.data["recovery_delay_seconds"], 2)
        job.refresh_from_db()
        self.assertEqual(job.recovery_count, 2)
        self.assertLessEqual(first_available_at, timezone.now())
        self.assertGreaterEqual(
            job.available_at,
            second_started_at + timedelta(seconds=1),
        )
        self.assertLessEqual(
            job.available_at,
            second_started_at + timedelta(seconds=3),
        )

    @patch("redis.Redis.from_url")
    def test_build_recovery_uses_slower_backoff(self, redis_from_url):
        redis_from_url.return_value = Mock()
        WorkerNode.objects.create(
            name="worker-a",
            hostname="worker-a.local",
        )
        attempt = create_build_attempt(self.version)
        enqueue_build_attempt(attempt)
        job = Job.objects.get(build_attempt=attempt)
        self.client.post(
            reverse("dispatch-scheduler-job", args=[job.job_id]),
            data={
                "worker_name": "worker-a",
                "queue_name": "worker:worker-a:jobs",
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        started_at = timezone.now()
        requeue_response = self.client.post(
            reverse("requeue-scheduler-job", args=[job.job_id]),
            data={
                "worker_name": "worker-a",
                "reason": "Worker missed heartbeat.",
                "recovery": True,
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(requeue_response.status_code, 200)
        self.assertTrue(requeue_response.data["requeued"])
        self.assertEqual(requeue_response.data["recovery_delay_seconds"], 10)
        job.refresh_from_db()
        self.assertEqual(job.recovery_count, 1)
        self.assertGreaterEqual(job.available_at, started_at + timedelta(seconds=9))
        self.assertLessEqual(job.available_at, started_at + timedelta(seconds=11))

    @patch("redis.Redis.from_url")
    def test_recovered_too_many_times_moves_to_dead_letter(self, redis_from_url):
        redis_from_url.return_value = Mock()
        WorkerNode.objects.create(
            name="worker-a",
            hostname="worker-a.local",
        )
        invocation = Invocation.objects.create(
            function_version=self.version,
            event={},
        )
        enqueue_invocation(invocation)
        job = Job.objects.get(invocation=invocation)
        job.status = JobStatus.RUNNING
        job.queue_name = "worker:worker-a:jobs"
        job.recovery_count = 3
        job.max_recovery_attempts = 3
        job.payload["assigned_worker"] = "worker-a"
        job.save(
            update_fields=[
                "status",
                "queue_name",
                "recovery_count",
                "max_recovery_attempts",
                "payload",
                "updated_at",
            ]
        )

        response = self.client.post(
            reverse("requeue-scheduler-job", args=[job.job_id]),
            data={
                "worker_name": "worker-a",
                "reason": "Worker missed heartbeat too many times.",
                "recovery": True,
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.data["requeued"])
        self.assertTrue(response.data["dead_lettered"])
        job.refresh_from_db()
        self.assertEqual(job.status, JobStatus.DEAD_LETTERED)
        self.assertEqual(job.recovery_count, 4)
        self.assertIsNotNone(job.dead_lettered_at)
        self.assertIn("too many", job.dead_letter_reason)
        self.assertNotIn("assigned_worker", job.payload)

    @patch("redis.Redis.from_url")
    def test_old_worker_report_is_ignored_after_recovery(self, redis_from_url):
        redis_from_url.return_value = Mock()
        WorkerNode.objects.create(
            name="worker-a",
            hostname="worker-a.local",
        )
        attempt = create_build_attempt(self.version)
        enqueue_build_attempt(attempt)
        job = Job.objects.get(build_attempt=attempt)
        self.client.post(
            reverse("dispatch-scheduler-job", args=[job.job_id]),
            data={
                "worker_name": "worker-a",
                "queue_name": "worker:worker-a:jobs",
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )
        job.refresh_from_db()
        old_attempt = job.payload["dispatch_attempt"]
        self.client.post(
            reverse("requeue-scheduler-job", args=[job.job_id]),
            data={
                "worker_name": "worker-a",
                "reason": "Worker missed heartbeat.",
                "recovery": True,
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        report_response = self.client.patch(
            reverse("report-build", args=[attempt.request_id]),
            data={
                "job_id": str(job.job_id),
                "dispatch_attempt": old_attempt,
                "worker_name": "worker-a",
                "status": BuildStatus.BUILT,
                "image_ref": "localhost:5000/functions/jobs:v1-v1",
                "build_finished_at": timezone.now().isoformat(),
            },
            format="json",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(report_response.status_code, 200)
        self.assertFalse(report_response.data["accepted"])
        self.assertTrue(report_response.data["stale"])
        attempt.refresh_from_db()
        job.refresh_from_db()
        self.assertEqual(attempt.status, BuildStatus.QUEUED)
        self.assertEqual(job.status, JobStatus.QUEUED)


class OutboxPublisherTests(TestCase):
    def make_event(self) -> OutboxEvent:
        import uuid

        job_id = uuid.uuid4()
        return OutboxEvent.objects.create(
            aggregate_id=job_id,
            event_type="job.created",
            payload={"job_id": str(job_id), "status": "queued"},
        )

    def test_successful_publish_marks_event(self):
        event = self.make_event()
        client = Mock()
        client.eval.return_value = "1710000000000-0"

        result = publish_pending_outbox_events(client, stream_name="test:events")

        self.assertEqual(result, {"published": 1, "failed": 0})
        event.refresh_from_db()
        self.assertEqual(event.publish_attempts, 1)
        self.assertEqual(event.stream_id, "1710000000000-0")
        self.assertIsNotNone(event.published_at)
        self.assertEqual(event.last_error, "")
        args = client.eval.call_args.args
        self.assertEqual(args[2], "test:events")
        self.assertEqual(
            args[3],
            f"orchestrator:outbox:published:{event.event_id}",
        )

    def test_failed_publish_remains_retryable(self):
        event = self.make_event()
        client = Mock()
        client.eval.side_effect = ConnectionError("redis unavailable")

        result = publish_pending_outbox_events(client)

        self.assertEqual(result, {"published": 0, "failed": 1})
        event.refresh_from_db()
        self.assertEqual(event.publish_attempts, 1)
        self.assertIsNone(event.published_at)
        self.assertEqual(event.stream_id, "")
        self.assertIn("redis unavailable", event.last_error)

    def test_already_published_event_is_not_republished(self):
        event = self.make_event()
        event.published_at = timezone.now()
        event.stream_id = "1-0"
        event.save(update_fields=["published_at", "stream_id", "updated_at"])
        client = Mock()

        result = publish_pending_outbox_events(client)

        self.assertEqual(result, {"published": 0, "failed": 0})
        client.eval.assert_not_called()
