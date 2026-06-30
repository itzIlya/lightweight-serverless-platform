import time

import redis
from django.conf import settings
from django.core.management.base import BaseCommand

from apps.jobs.outbox import publish_pending_outbox_events


class Command(BaseCommand):
    help = "Publish pending transactional outbox events to the orchestrator stream."

    def add_arguments(self, parser):
        parser.add_argument("--once", action="store_true")
        parser.add_argument("--batch-size", type=int, default=100)
        parser.add_argument("--poll-seconds", type=float, default=0.2)

    def handle(self, *args, **options):
        client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)
        while True:
            result = publish_pending_outbox_events(
                client,
                batch_size=max(options["batch_size"], 1),
            )
            if result["published"] or result["failed"]:
                self.stdout.write(
                    f"outbox published={result['published']} failed={result['failed']}"
                )
            if options["once"]:
                return
            if not result["published"]:
                time.sleep(max(options["poll_seconds"], 0.01))
