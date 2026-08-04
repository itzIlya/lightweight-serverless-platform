from datetime import timedelta

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.jobs.models import Job, JobStatus


class Command(BaseCommand):
    help = "Delete dead-lettered jobs after the dead-letter retention window."

    def add_arguments(self, parser):
        parser.add_argument(
            "--retention-days",
            type=int,
            default=settings.DEAD_LETTER_RETENTION_DAYS,
        )
        parser.add_argument("--batch-size", type=int, default=100)
        parser.add_argument("--dry-run", action="store_true")

    def handle(self, *args, **options):
        deleted = cleanup_dead_letter_jobs(
            retention_days=options["retention_days"],
            batch_size=options["batch_size"],
            dry_run=options["dry_run"],
        )
        action = "would_delete" if options["dry_run"] else "deleted"
        self.stdout.write(f"{action}_dead_letter_jobs={deleted}")


def cleanup_dead_letter_jobs(
    *,
    retention_days: int | None = None,
    batch_size: int = 100,
    now=None,
    dry_run: bool = False,
) -> int:
    retention_days = (
        settings.DEAD_LETTER_RETENTION_DAYS
        if retention_days is None
        else int(retention_days)
    )
    cutoff = (now or timezone.now()) - timedelta(days=retention_days)
    queryset = Job.objects.filter(
        status=JobStatus.DEAD_LETTERED,
        dead_lettered_at__lte=cutoff,
    ).order_by("dead_lettered_at")
    ids = list(queryset.values_list("id", flat=True)[: max(int(batch_size), 1)])
    if dry_run:
        return len(ids)
    deleted, _ = Job.objects.filter(id__in=ids).delete()
    return deleted
