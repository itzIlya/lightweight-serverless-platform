import time

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from apps.invocations.models import InvocationStagedCompletion, StagedCompletionStatus


class Command(BaseCommand):
    help = "Delete expired staged invocation files that were never committed."

    def add_arguments(self, parser):
        parser.add_argument("--once", action="store_true")
        parser.add_argument("--interval-seconds", type=float, default=60)

    def handle(self, *args, **options):
        while True:
            cleaned = cleanup_expired_staged_completions()
            if cleaned:
                self.stdout.write(f"expired staged completions={cleaned}")
            if options["once"]:
                return
            time.sleep(max(options["interval_seconds"], 1))


def cleanup_expired_staged_completions() -> int:
    ids = list(
        InvocationStagedCompletion.objects.filter(
            status=StagedCompletionStatus.STAGED,
            expires_at__lte=timezone.now(),
        ).values_list("id", flat=True)[:100]
    )
    cleaned = 0
    for completion_id in ids:
        with transaction.atomic():
            completion = InvocationStagedCompletion.objects.select_for_update().get(
                pk=completion_id
            )
            if completion.status != StagedCompletionStatus.STAGED:
                continue
            for output in completion.output_files.all():
                if output.file:
                    output.file.delete(save=False)
            for log_file in completion.log_artifacts.all():
                if log_file.file:
                    log_file.file.delete(save=False)
            completion.output_files.all().delete()
            completion.log_artifacts.all().delete()
            completion.status = StagedCompletionStatus.EXPIRED
            completion.save(update_fields=["status", "updated_at"])
            cleaned += 1
    return cleaned
