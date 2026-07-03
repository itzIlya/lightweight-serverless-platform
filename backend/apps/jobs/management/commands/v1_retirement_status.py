import json

import redis
from django.conf import settings
from django.core.management.base import BaseCommand

from apps.jobs.v1_retirement import v1_retirement_status


class Command(BaseCommand):
    help = "Report whether all V1 jobs and known V1 Redis queues are drained."

    def handle(self, *args, **options):
        client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)
        self.stdout.write(json.dumps(v1_retirement_status(client), indent=2))
