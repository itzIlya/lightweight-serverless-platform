import json
import os
import sys
import unittest
import uuid
from pathlib import Path

import redis

sys.path.insert(0, str(Path(__file__).resolve().parent))

from orchestrator_workers import WorkerOperationalStateStore
from production_orchestrator import ProductionOrchestrator


class ProductionOrchestratorTests(unittest.TestCase):
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
        self.unique = str(uuid.uuid4())
        self.event_stream = f"test:v2:events:{self.unique}"
        self.event_group = f"test-v2-group-{self.unique}"
        self.projection_stream = f"test:v2:projections:{self.unique}"
        self.ready_key = f"test:v2:ready:{self.unique}"
        self.lease_key = f"test:v2:leases:{self.unique}"
        self.orphan_stream = f"test:v2:orphans:{self.unique}"
        self.state_prefix = f"test:v2:job:{self.unique}"
        self.worker_prefix = f"test:v2:worker:{self.unique}"
        self.worker_lease_key = f"test:v2:worker-leases:{self.unique}"
        self.worker_store = WorkerOperationalStateStore(
            self.redis,
            key_prefix=self.worker_prefix,
            lease_key=self.worker_lease_key,
            lease_ttl_ms=100_000,
        )
        self.orchestrator = ProductionOrchestrator(
            self.redis,
            event_stream=self.event_stream,
            event_group=self.event_group,
            projection_stream=self.projection_stream,
            ready_key=self.ready_key,
            lease_key=self.lease_key,
            orphan_stream=self.orphan_stream,
            lease_ttl_ms=100,
            state_prefix=self.state_prefix,
            worker_store=self.worker_store,
        )
        self.orchestrator.ensure_event_group()
        self.worker_store.record_heartbeat(
            {
                "name": "worker-a",
                "hostname": "worker-a",
                "max_concurrency": 4,
                "max_build_concurrency": 1,
                "max_invocation_concurrency": 4,
                "queue_name": "worker:worker-a:jobs",
                "invocation_queue_name": "worker:worker-a:invocations",
                "build_queue_name": "worker:worker-a:builds",
                "processing_queue_name": "worker:worker-a:processing",
            },
            now_ms=1000,
        )
        self.job_id = str(uuid.uuid4())

    def tearDown(self):
        keys = [
            self.event_stream,
            self.projection_stream,
            self.ready_key,
            self.lease_key,
            self.orphan_stream,
            self.worker_lease_key,
            self.orchestrator.worker_stream("worker-a", "build"),
            self.orchestrator.worker_stream("worker-a", "invocation"),
        ]
        keys.extend(self.redis.scan_iter(f"{self.state_prefix}:*"))
        keys.extend(self.redis.scan_iter(f"{self.worker_prefix}:*"))
        if keys:
            self.redis.delete(*set(keys))

    def creation_fields(self, job_type="build"):
        payload_type = "function.build" if job_type == "build" else "function.invoke"
        payload = {
            "type": payload_type,
            "build_request_id": str(uuid.uuid4()),
            "request_id": str(uuid.uuid4()),
            "image_ref": "localhost:5000/functions/test:v1-a1-abc",
        }
        return {
            "event_id": str(uuid.uuid4()),
            "event_type": "job.created",
            "payload": json.dumps(
                {
                    "job_id": self.job_id,
                    "job_type": job_type,
                    "coordination_version": 2,
                    "status": "queued",
                    "available_at": "1970-01-01T00:00:00+00:00",
                    "payload": payload,
                }
            ),
        }

    def create_and_dispatch(self, job_type="build"):
        self.orchestrator.process_creation_event("1-0", self.creation_fields(job_type))
        count = self.orchestrator.dispatch_ready_once(now_ms=1000)
        self.assertEqual(count, 1)
        return self.orchestrator.state.get_job(self.job_id)

    def test_build_dispatch_is_atomic_and_uses_immutable_attempt_tag(self):
        job = self.create_and_dispatch()
        stream = self.orchestrator.worker_stream("worker-a", "build")
        messages = self.redis.xrange(stream)

        self.assertEqual(job["status"], "dispatched")
        self.assertEqual(job["dispatch_attempt"], 1)
        self.assertTrue(job["effective_image_ref"].endswith("-d1"))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0][1]["job_id"], self.job_id)
        self.assertEqual(messages[0][1]["dispatch_attempt"], "1")

    def test_duplicate_claim_and_completion_are_idempotent(self):
        self.create_and_dispatch()
        first_claim = self.orchestrator.claim_job(
            self.job_id,
            worker_name="worker-a",
            dispatch_attempt=1,
            now_ms=1010,
        )
        duplicate_claim = self.orchestrator.claim_job(
            self.job_id,
            worker_name="worker-a",
            dispatch_attempt=1,
            now_ms=1020,
        )
        image_ref = first_claim["payload"]["image_ref"]
        completion = {
            "worker_name": "worker-a",
            "dispatch_attempt": 1,
            "completion_id": f"{self.job_id}:1:built",
            "status": "succeeded",
            "completion_payload": {"image_ref": image_ref, "build_log": "ok"},
            "artifact_commit_id": image_ref,
        }
        first = self.orchestrator.complete_job(self.job_id, **completion, now_ms=1030)
        lost_response_retry = self.orchestrator.complete_job(
            self.job_id,
            **completion,
            now_ms=1040,
        )
        projections = self.redis.xrange(self.projection_stream)
        succeeded = [m for m in projections if m[1]["event_type"] == "job.succeeded"]

        self.assertTrue(first_claim["claimed"])
        self.assertTrue(duplicate_claim["idempotent"])
        self.assertTrue(first["completed"])
        self.assertTrue(lost_response_retry["completed"])
        self.assertTrue(lost_response_retry["idempotent"])
        self.assertEqual(len(succeeded), 1)

    def test_worker_crash_requeues_and_emits_orphan_cleanup(self):
        first = self.create_and_dispatch()
        self.orchestrator.claim_job(
            self.job_id,
            worker_name="worker-a",
            dispatch_attempt=1,
            now_ms=1010,
        )

        recovered = self.orchestrator.recover_expired_once(now_ms=1110)
        self.assertEqual(recovered, 1)
        orphan = self.redis.xrange(self.orphan_stream)[0][1]
        self.assertEqual(orphan["image_ref"], first["effective_image_ref"])

        self.assertEqual(self.orchestrator.dispatch_ready_once(now_ms=1120), 1)
        second = self.orchestrator.state.get_job(self.job_id)
        stale = self.orchestrator.complete_job(
            self.job_id,
            worker_name="worker-a",
            dispatch_attempt=1,
            completion_id=f"{self.job_id}:1:built",
            status="succeeded",
            completion_payload={"image_ref": first["effective_image_ref"]},
            artifact_commit_id=first["effective_image_ref"],
            now_ms=1130,
        )

        self.assertEqual(second["dispatch_attempt"], 2)
        self.assertTrue(second["effective_image_ref"].endswith("-d2"))
        self.assertFalse(stale["completed"])

    def test_abandoned_creation_event_is_reclaimed(self):
        self.redis.xadd(self.event_stream, self.creation_fields())
        self.redis.xreadgroup(
            self.event_group,
            "dead-consumer",
            {self.event_stream: ">"},
            count=1,
        )

        reclaimed = self.orchestrator.reclaim_events_once(min_idle_ms=0)

        self.assertEqual(reclaimed, 1)
        self.assertEqual(self.orchestrator.state.get_job(self.job_id)["status"], "queued")
        self.assertEqual(self.redis.xpending(self.event_stream, self.event_group)["pending"], 0)

    def test_invocation_old_attempt_cannot_execute_after_recovery(self):
        self.create_and_dispatch("invocation")
        claimed = self.orchestrator.claim_job(
            self.job_id,
            worker_name="worker-a",
            dispatch_attempt=1,
            now_ms=1010,
        )
        self.orchestrator.recover_expired_once(now_ms=1110)
        self.orchestrator.dispatch_ready_once(now_ms=1120)

        stale_claim = self.orchestrator.claim_job(
            self.job_id,
            worker_name="worker-a",
            dispatch_attempt=1,
            now_ms=1130,
        )
        fresh_claim = self.orchestrator.claim_job(
            self.job_id,
            worker_name="worker-a",
            dispatch_attempt=2,
            now_ms=1130,
        )

        self.assertTrue(claimed["claimed"])
        self.assertFalse(stale_claim["claimed"])
        self.assertEqual(stale_claim["code"], "stale")
        self.assertTrue(fresh_claim["claimed"])

    def test_delivery_crash_before_claim_is_recovered_and_fenced(self):
        self.create_and_dispatch("invocation")

        recovered = self.orchestrator.recover_expired_once(now_ms=1100)
        self.assertEqual(recovered, 1)
        self.assertEqual(self.orchestrator.dispatch_ready_once(now_ms=1110), 1)

        stale_delivery = self.orchestrator.claim_job(
            self.job_id,
            worker_name="worker-a",
            dispatch_attempt=1,
            now_ms=1120,
        )
        current_delivery = self.orchestrator.claim_job(
            self.job_id,
            worker_name="worker-a",
            dispatch_attempt=2,
            now_ms=1120,
        )

        self.assertFalse(stale_delivery["claimed"])
        self.assertEqual(stale_delivery["code"], "stale")
        self.assertTrue(current_delivery["claimed"])

    def test_repeated_worker_crashes_dead_letter_and_cleanup_last_image(self):
        job = self.create_and_dispatch("build")
        self.orchestrator.claim_job(
            self.job_id,
            worker_name="worker-a",
            dispatch_attempt=1,
            now_ms=1010,
        )
        self.redis.hset(
            self.orchestrator.state.key(self.job_id),
            mapping={"recovery_count": 3, "max_recovery_attempts": 3},
        )

        recovered = self.orchestrator.recover_expired_once(now_ms=1110)

        state = self.orchestrator.state.get_job(self.job_id)
        orphan = self.redis.xrange(self.orphan_stream)[0][1]
        self.assertEqual(recovered, 1)
        self.assertEqual(state["status"], "dead_lettered")
        self.assertEqual(orphan["image_ref"], job["effective_image_ref"])
        self.assertEqual(self.redis.zscore(self.ready_key, self.job_id), None)
