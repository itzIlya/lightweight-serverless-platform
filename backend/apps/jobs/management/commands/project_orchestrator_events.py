import socket
import time

import redis
from django.conf import settings
from django.core.management.base import BaseCommand

from apps.jobs.projector import OrchestratorProjector


class Command(BaseCommand):
    help = "Project V2 orchestrator events into PostgreSQL read models."

    def handle(self, *args, **options):
        client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)
        projector = OrchestratorProjector(client, consumer=socket.gethostname())
        projector.ensure_group()
        while True:
            try:
                projector.reclaim_once()
                projector.process_once()
            except Exception as exc:
                self.stderr.write(f"orchestrator projection failed: {exc}")
                time.sleep(1)
