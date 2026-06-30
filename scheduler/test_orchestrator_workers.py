import os
import sys
import unittest
import uuid
from pathlib import Path

import redis

sys.path.insert(0, str(Path(__file__).resolve().parent))

from orchestrator_workers import WorkerOperationalStateStore


class WorkerOperationalStateStoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.redis = redis.Redis.from_url(
            os.getenv("REDIS_URL", "redis://localhost:6379/0"),
            decode_responses=True,
        )
        try:
            cls.redis.ping()
        except redis.RedisError as exc:
            raise unittest.SkipTest(f"Redis integration tests unavailable: {exc}")

    def setUp(self):
        unique = uuid.uuid4()
        self.prefix = f"test:orchestrator:worker:{unique}"
        self.lease_key = f"test:orchestrator:worker-leases:{unique}"
        self.store = WorkerOperationalStateStore(
            self.redis,
            key_prefix=self.prefix,
            lease_key=self.lease_key,
            lease_ttl_ms=300,
        )

    def tearDown(self):
        keys = list(self.redis.scan_iter(f"{self.prefix}:*"))
        if keys:
            self.redis.delete(*keys)
        self.redis.delete(self.lease_key)

    def payload(self, name="worker-a"):
        return {
            "name": name,
            "hostname": f"{name}.local",
            "max_concurrency": 4,
            "max_build_concurrency": 1,
            "max_invocation_concurrency": 4,
            "active_jobs": 2,
            "active_builds": 1,
            "active_invocations": 1,
            "queue_name": f"worker:{name}:jobs",
            "invocation_queue_name": f"worker:{name}:invocations",
            "build_queue_name": f"worker:{name}:builds",
            "processing_queue_name": f"worker:{name}:processing",
        }

    def test_heartbeat_records_capacity_and_activity(self):
        lease = self.store.record_heartbeat(self.payload(), now_ms=1000)
        worker = self.store.get_worker("worker-a")

        self.assertEqual(lease, 1300)
        self.assertEqual(worker["status"], "online")
        self.assertEqual(worker["max_concurrency"], 4)
        self.assertEqual(worker["metadata"]["active_jobs"], 2)
        self.assertEqual(worker["metadata"]["active_builds"], 1)

    def test_heartbeat_refreshes_lease_and_capacity_idempotently(self):
        self.store.record_heartbeat(self.payload(), now_ms=1000)
        updated = self.payload()
        updated["active_jobs"] = 0
        lease = self.store.record_heartbeat(updated, now_ms=1200)

        self.assertEqual(lease, 1500)
        self.assertEqual(self.store.get_worker("worker-a")["metadata"]["active_jobs"], 0)
        self.assertEqual(self.redis.zcard(self.lease_key), 1)

    def test_list_returns_only_live_workers(self):
        self.store.record_heartbeat(self.payload("worker-a"), now_ms=1000)
        self.store.record_heartbeat(self.payload("worker-b"), now_ms=1200)

        workers = self.store.list_online_workers(now_ms=1350)

        self.assertEqual([worker["name"] for worker in workers], ["worker-b"])
        self.assertEqual(self.store.get_worker("worker-a")["status"], "offline")

    def test_new_heartbeat_prevents_stale_expiry(self):
        self.store.record_heartbeat(self.payload(), now_ms=1000)
        self.store.record_heartbeat(self.payload(), now_ms=1299)

        expired = self.store.expire_stale(now_ms=1300)

        self.assertEqual(expired, [])
        self.assertEqual(self.store.get_worker("worker-a")["status"], "online")
