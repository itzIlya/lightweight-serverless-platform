import os
import sys
import unittest
import uuid
from pathlib import Path

import redis

sys.path.insert(0, str(Path(__file__).resolve().parent))

from orchestrator_state import V2JobStateStore, V2JobStatus


class V2JobStateStoreTests(unittest.TestCase):
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
        self.prefix = f"test:orchestrator:v2:{uuid.uuid4()}"
        self.store = V2JobStateStore(self.redis, key_prefix=self.prefix)
        self.job_id = str(uuid.uuid4())

    def tearDown(self):
        keys = list(self.redis.scan_iter(f"{self.prefix}:*"))
        if keys:
            self.redis.delete(*keys)

    def create(self, *, available_at_ms=0):
        return self.store.create_job(
            self.job_id,
            "invocation",
            available_at_ms=available_at_ms,
            now_ms=100,
        )

    def dispatch(self, *, now_ms=200):
        return self.store.dispatch(
            self.job_id,
            worker_name="worker-a",
            queue_name="worker:worker-a:invocations",
            now_ms=now_ms,
        )

    def claim(self, *, worker="worker-a", attempt=1):
        return self.store.claim(
            self.job_id,
            worker_name=worker,
            dispatch_attempt=attempt,
            lease_expires_at_ms=1000,
            now_ms=300,
        )

    def test_create_is_v2_and_idempotent(self):
        created = self.create()
        duplicate = self.create()
        job = self.store.get_job(self.job_id)

        self.assertTrue(created.accepted)
        self.assertEqual(created.status, V2JobStatus.QUEUED)
        self.assertFalse(duplicate.accepted)
        self.assertEqual(duplicate.code, "exists")
        self.assertTrue(duplicate.idempotent)
        self.assertEqual(job["coordination_version"], 2)
        self.assertEqual(job["dispatch_attempt"], 0)

    def test_dispatch_requires_available_queued_job(self):
        self.create(available_at_ms=500)

        early = self.dispatch(now_ms=499)
        accepted = self.dispatch(now_ms=500)
        duplicate = self.dispatch(now_ms=501)

        self.assertEqual(early.code, "not_available")
        self.assertTrue(accepted.accepted)
        self.assertEqual(accepted.dispatch_attempt, 1)
        self.assertEqual(duplicate.code, "invalid_state")

    def test_claim_is_fenced_and_idempotent(self):
        self.create()
        self.dispatch()

        wrong_worker = self.claim(worker="worker-b")
        wrong_attempt = self.claim(attempt=2)
        accepted = self.claim()
        duplicate = self.claim()

        self.assertEqual(wrong_worker.code, "stale")
        self.assertEqual(wrong_attempt.code, "stale")
        self.assertTrue(accepted.accepted)
        self.assertEqual(accepted.status, V2JobStatus.RUNNING)
        self.assertTrue(duplicate.accepted)
        self.assertTrue(duplicate.idempotent)

    def test_lease_renewal_requires_running_owner(self):
        self.create()
        self.dispatch()
        before_claim = self.store.renew_lease(
            self.job_id,
            worker_name="worker-a",
            dispatch_attempt=1,
            lease_expires_at_ms=2000,
            now_ms=400,
        )
        self.claim()
        stale = self.store.renew_lease(
            self.job_id,
            worker_name="worker-b",
            dispatch_attempt=1,
            lease_expires_at_ms=2000,
            now_ms=400,
        )
        renewed = self.store.renew_lease(
            self.job_id,
            worker_name="worker-a",
            dispatch_attempt=1,
            lease_expires_at_ms=2000,
            now_ms=400,
        )

        self.assertEqual(before_claim.code, "invalid_state")
        self.assertEqual(stale.code, "stale")
        self.assertTrue(renewed.accepted)
        self.assertEqual(self.store.get_job(self.job_id)["lease_expires_at_ms"], 2000)

    def test_finalization_requires_running_and_matching_completion(self):
        self.create()
        before_running = self.store.begin_finalization(
            self.job_id,
            worker_name="worker-a",
            dispatch_attempt=0,
            completion_id="completion-1",
            completion_payload={"result": {"ok": True}},
            now_ms=400,
        )
        self.dispatch()
        self.claim()
        accepted = self.store.begin_finalization(
            self.job_id,
            worker_name="worker-a",
            dispatch_attempt=1,
            completion_id="completion-1",
            completion_payload={"result": {"ok": True}},
            now_ms=400,
        )
        duplicate = self.store.begin_finalization(
            self.job_id,
            worker_name="worker-a",
            dispatch_attempt=1,
            completion_id="completion-1",
            completion_payload={"result": {"ok": True}},
            now_ms=401,
        )
        conflict = self.store.begin_finalization(
            self.job_id,
            worker_name="worker-a",
            dispatch_attempt=1,
            completion_id="completion-2",
            completion_payload={},
            now_ms=402,
        )

        self.assertEqual(before_running.code, "invalid_state")
        self.assertTrue(accepted.accepted)
        self.assertTrue(duplicate.idempotent)
        self.assertEqual(conflict.code, "completion_conflict")
        self.assertEqual(
            self.store.get_job(self.job_id)["completion_payload"],
            {"result": {"ok": True}},
        )

    def test_success_requires_artifact_commit_before_terminal_state(self):
        self.create()
        self.dispatch()
        self.claim()
        self.store.begin_finalization(
            self.job_id,
            worker_name="worker-a",
            dispatch_attempt=1,
            completion_id="completion-1",
            completion_payload={"result": {"ok": True}},
            now_ms=400,
        )

        missing_commit = self.store.finish_finalization(
            self.job_id,
            completion_id="completion-1",
            terminal_status=V2JobStatus.SUCCEEDED,
            now_ms=500,
        )
        accepted = self.store.finish_finalization(
            self.job_id,
            completion_id="completion-1",
            terminal_status=V2JobStatus.SUCCEEDED,
            artifact_commit_id="artifact-commit-1",
            now_ms=501,
        )
        duplicate = self.store.finish_finalization(
            self.job_id,
            completion_id="completion-1",
            terminal_status=V2JobStatus.SUCCEEDED,
            artifact_commit_id="artifact-commit-1",
            now_ms=502,
        )

        self.assertEqual(missing_commit.code, "missing_artifact_commit")
        self.assertEqual(missing_commit.status, V2JobStatus.FINALIZING)
        self.assertTrue(accepted.accepted)
        self.assertTrue(duplicate.idempotent)
        self.assertEqual(self.store.get_job(self.job_id)["status"], "succeeded")

    def test_requeue_increments_attempt_only_on_next_dispatch(self):
        self.create()
        self.dispatch()
        self.claim()

        stale = self.store.requeue(
            self.job_id,
            dispatch_attempt=2,
            available_at_ms=600,
            reason="wrong attempt",
            now_ms=500,
        )
        accepted = self.store.requeue(
            self.job_id,
            dispatch_attempt=1,
            available_at_ms=600,
            reason="worker lost",
            now_ms=500,
        )
        dispatched = self.dispatch(now_ms=600)
        old_claim = self.claim(attempt=1)

        self.assertEqual(stale.code, "stale")
        self.assertTrue(accepted.accepted)
        self.assertEqual(self.store.get_job(self.job_id)["recovery_count"], 1)
        self.assertEqual(dispatched.dispatch_attempt, 2)
        self.assertEqual(old_claim.code, "stale")

    def test_terminal_jobs_cannot_be_reopened(self):
        self.create()
        self.dispatch()
        cancelled = self.store.cancel(
            self.job_id,
            reason="owner cancelled",
            dispatch_attempt=1,
            now_ms=500,
        )
        claim = self.claim()
        requeue = self.store.requeue(
            self.job_id,
            dispatch_attempt=1,
            available_at_ms=600,
            reason="should not reopen",
            now_ms=600,
        )
        dead_letter = self.store.dead_letter(
            self.job_id,
            reason="should not replace terminal state",
            dispatch_attempt=1,
            now_ms=600,
        )

        self.assertTrue(cancelled.accepted)
        self.assertEqual(claim.code, "terminal")
        self.assertEqual(requeue.code, "terminal")
        self.assertEqual(dead_letter.code, "terminal")
        self.assertEqual(self.store.get_job(self.job_id)["status"], "cancelled")


if __name__ == "__main__":
    unittest.main()

