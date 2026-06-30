import json
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parent))

from shadow_orchestrator import ShadowOrchestrator


class ShadowOrchestratorTests(unittest.TestCase):
    def setUp(self):
        self.redis = Mock()
        self.redis.hgetall.return_value = {}
        self.redis.llen.return_value = 0
        self.backend = Mock()
        self.backend.list_workers.return_value = [
            {
                "name": "worker-a",
                "queue_name": "worker:worker-a:jobs",
                "invocation_queue_name": "worker:worker-a:invocations",
                "build_queue_name": "worker:worker-a:builds",
                "max_concurrency": 4,
                "metadata": {"active_jobs": 0, "active_builds": 0},
            }
        ]
        self.worker_store = Mock()
        self.worker_store.list_online_workers.return_value = (
            self.backend.list_workers.return_value
        )
        self.shadow = ShadowOrchestrator(
            self.redis,
            self.backend,
            worker_store=self.worker_store,
        )
        self.shadow.state = Mock()
        self.shadow.state.create_job.return_value = Mock(accepted=True)
        self.shadow.state.dispatch.return_value = Mock(
            accepted=True,
            code="ok",
            status="dispatched",
        )

    def fields(self, job_type="invocation", payload_type="function.invoke"):
        return {
            "event_id": "event-1",
            "event_type": "job.created",
            "aggregate_id": "job-1",
            "payload": json.dumps(
                {
                    "job_id": "job-1",
                    "job_type": job_type,
                    "coordination_version": 1,
                    "status": "queued",
                    "available_at": "1970-01-01T00:00:00+00:00",
                    "payload": {"type": payload_type},
                }
            ),
        }

    def test_invocation_is_modeled_but_never_dispatched_to_production(self):
        decision = self.shadow.process_event("1-0", self.fields(), now_ms=100)

        self.assertEqual(decision["decision"], "dispatch")
        self.assertEqual(decision["selected_worker"], "worker-a")
        self.assertEqual(decision["queue_name"], "worker:worker-a:invocations")
        self.shadow.state.dispatch.assert_called_once()
        self.backend.dispatch_job.assert_not_called()
        self.redis.rpush.assert_not_called()

    def test_build_uses_build_queue(self):
        decision = self.shadow.process_event(
            "1-0",
            self.fields("build", "function.build"),
            now_ms=100,
        )

        self.assertEqual(decision["queue_name"], "worker:worker-a:builds")
        self.backend.dispatch_job.assert_not_called()
        self.redis.rpush.assert_not_called()

    def test_no_worker_remains_queued(self):
        self.worker_store.list_online_workers.return_value = []

        decision = self.shadow.process_event("1-0", self.fields(), now_ms=100)

        self.assertEqual(decision["decision"], "no_worker")
        self.assertEqual(decision["shadow_status"], "queued")
        self.shadow.state.dispatch.assert_not_called()

    def test_existing_decision_makes_replay_idempotent(self):
        self.redis.hgetall.return_value = {"decision": "dispatch"}

        decision = self.shadow.process_event("1-0", self.fields(), now_ms=100)

        self.assertEqual(decision, {"decision": "dispatch"})
        self.worker_store.list_online_workers.assert_not_called()
        self.shadow.state.create_job.assert_not_called()

    def test_run_once_acks_only_after_processing(self):
        self.redis.xreadgroup.return_value = [
            ("orchestrator:events", [("1-0", self.fields())])
        ]

        processed = self.shadow.run_once(block_ms=0)

        self.assertEqual(processed, 1)
        self.redis.xack.assert_called_once_with(
            "orchestrator:events",
            "orchestrator-shadow-v1",
            "1-0",
        )
