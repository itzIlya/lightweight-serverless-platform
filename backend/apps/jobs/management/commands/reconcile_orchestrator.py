import time

import redis
from django.conf import settings
from django.core.management.base import BaseCommand

from apps.jobs.reconciler import (
    CrossStoreReconciler,
    OrchestratorRepairClient,
)


class Command(BaseCommand):
    help = "Audit bounded V2 Redis/PostgreSQL state and repair safe mismatches."

    def add_arguments(self, parser):
        parser.add_argument("--once", action="store_true")
        parser.add_argument("--interval-seconds", type=float, default=300)
        parser.add_argument("--batch-size", type=int, default=100)

    def handle(self, *args, **options):
        reconciler = CrossStoreReconciler(
            redis.Redis.from_url(settings.REDIS_URL, decode_responses=True),
            OrchestratorRepairClient(
                settings.ORCHESTRATOR_BASE_URL,
                settings.WORKER_SHARED_SECRET,
            ),
        )
        while True:
            result = reconciler.reconcile_once(limit=max(options["batch_size"], 1))
            if any(
                result[key]
                for key in ("repaired_projections", "resumed_commits", "anomalies")
            ):
                self.stdout.write(f"orchestrator reconciliation={result}")
            if options["once"]:
                return
            time.sleep(max(options["interval_seconds"], 30))
