from datetime import timedelta

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from apps.invocations.models import Invocation, InvocationStatus


TERMINAL_INVOCATION_STATUSES = {
    InvocationStatus.SUCCEEDED,
    InvocationStatus.FAILED,
    InvocationStatus.TIMEOUT,
    InvocationStatus.CANCELLED,
}


class Command(BaseCommand):
    help = "Delete terminal invocations and their artifacts after the retention window."

    def add_arguments(self, parser):
        parser.add_argument(
            "--retention-days",
            type=int,
            default=settings.INVOCATION_RETENTION_DAYS,
        )
        parser.add_argument("--batch-size", type=int, default=100)
        parser.add_argument("--dry-run", action="store_true")

    def handle(self, *args, **options):
        deleted = cleanup_expired_invocations(
            retention_days=options["retention_days"],
            batch_size=options["batch_size"],
            dry_run=options["dry_run"],
        )
        action = "would_delete" if options["dry_run"] else "deleted"
        self.stdout.write(f"{action}_expired_invocations={deleted}")


def cleanup_expired_invocations(
    *,
    retention_days: int | None = None,
    batch_size: int = 100,
    now=None,
    dry_run: bool = False,
) -> int:
    retention_days = (
        settings.INVOCATION_RETENTION_DAYS
        if retention_days is None
        else int(retention_days)
    )
    cutoff = (now or timezone.now()) - timedelta(days=retention_days)
    ids = list(
        Invocation.objects.filter(
            status__in=TERMINAL_INVOCATION_STATUSES,
            queued_at__lte=cutoff,
        )
        .order_by("queued_at")
        .values_list("id", flat=True)[: max(int(batch_size), 1)]
    )
    if dry_run:
        return len(ids)

    deleted = 0
    for invocation_id in ids:
        with transaction.atomic():
            invocation = (
                Invocation.objects.select_for_update()
                .prefetch_related(
                    "input_files",
                    "output_files",
                    "log_artifacts",
                    "staged_completions__output_files",
                    "staged_completions__log_artifacts",
                )
                .filter(pk=invocation_id)
                .first()
            )
            if invocation is None:
                continue
            if (
                invocation.status not in TERMINAL_INVOCATION_STATUSES
                or invocation.queued_at > cutoff
            ):
                continue
            _delete_invocation_artifact_files(invocation)
            invocation.delete()
            deleted += 1
    return deleted


def _delete_invocation_artifact_files(invocation: Invocation) -> None:
    for input_file in invocation.input_files.all():
        if input_file.file:
            input_file.file.delete(save=False)

    seen_output_ids = set()
    for output_file in invocation.output_files.all():
        seen_output_ids.add(output_file.id)
        if output_file.file:
            output_file.file.delete(save=False)

    for log_file in invocation.log_artifacts.all():
        if log_file.file:
            log_file.file.delete(save=False)

    for completion in invocation.staged_completions.all():
        for output_file in completion.output_files.all():
            if output_file.id in seen_output_ids:
                continue
            if output_file.file:
                output_file.file.delete(save=False)
        for log_file in completion.log_artifacts.all():
            if log_file.file:
                log_file.file.delete(save=False)
