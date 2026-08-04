from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from .management.commands.cleanup_dead_letter_jobs import cleanup_dead_letter_jobs
from .models import Job, JobStatus, JobType


class DeadLetterRetentionTests(TestCase):
    def create_dead_letter(self, *, age_days: int) -> Job:
        return Job.objects.create(
            type=JobType.INVOCATION,
            status=JobStatus.DEAD_LETTERED,
            queue_name="worker:worker-a:invocations",
            dead_lettered_at=timezone.now() - timedelta(days=age_days),
            dead_letter_reason="Recovered too many times.",
        )

    def test_cleanup_deletes_old_dead_letter_jobs(self):
        old_job = self.create_dead_letter(age_days=61)
        recent_job = self.create_dead_letter(age_days=30)

        deleted = cleanup_dead_letter_jobs(retention_days=60)

        self.assertEqual(deleted, 1)
        self.assertFalse(Job.objects.filter(pk=old_job.pk).exists())
        self.assertTrue(Job.objects.filter(pk=recent_job.pk).exists())

    def test_cleanup_ignores_non_dead_letter_jobs(self):
        job = Job.objects.create(
            type=JobType.INVOCATION,
            status=JobStatus.FAILED,
            queue_name="worker:worker-a:invocations",
            dead_lettered_at=timezone.now() - timedelta(days=90),
        )

        deleted = cleanup_dead_letter_jobs(retention_days=60)

        self.assertEqual(deleted, 0)
        self.assertTrue(Job.objects.filter(pk=job.pk).exists())

    def test_cleanup_dry_run_counts_without_deleting(self):
        job = self.create_dead_letter(age_days=61)

        deleted = cleanup_dead_letter_jobs(retention_days=60, dry_run=True)

        self.assertEqual(deleted, 1)
        self.assertTrue(Job.objects.filter(pk=job.pk).exists())
