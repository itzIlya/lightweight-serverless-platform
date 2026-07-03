from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
import redis

from apps.jobs.v1_retirement import v1_retirement_status


class Command(BaseCommand):
    help = "Delete drained V1 Redis Lists after explicit retirement confirmation."

    def add_arguments(self, parser):
        parser.add_argument("--confirm", default="")

    def handle(self, *args, **options):
        if options["confirm"] != "RETIRE_V1":
            raise CommandError("Pass --confirm RETIRE_V1 after the soak period.")
        client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)
        state = v1_retirement_status(client)
        if not state["ready"]:
            raise CommandError(
                "V1 is not drained: "
                f"active_jobs={state['active_job_total']} "
                f"queued_items={state['queued_item_total']}"
            )
        queues = list(state["queue_depths"])
        deleted = client.delete(*queues) if queues else 0
        self.stdout.write(f"retired V1 queues={len(queues)} deleted_keys={deleted}")
