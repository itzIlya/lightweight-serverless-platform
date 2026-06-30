import json
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parent))

from scheduler import choose_worker, workers_with_queue_lengths
from shadow_orchestrator import ShadowOrchestrator


class V1V2PlacementComparisonTests(unittest.TestCase):
    def worker(self, name, *, active_jobs=0, active_builds=0):
        return {
            "name": name,
            "queue_name": f"worker:{name}:jobs",
            "invocation_queue_name": f"worker:{name}:invocations",
            "build_queue_name": f"worker:{name}:builds",
            "max_concurrency": 4,
            "metadata": {
                "active_jobs": active_jobs,
                "active_builds": active_builds,
            },
        }

    def compare(self, *, workers, queue_lengths, payload_type, job_type):
        v1_redis = Mock()
        v1_redis.llen.side_effect = lambda queue: queue_lengths.get(queue, 0)
        enriched = workers_with_queue_lengths(workers, v1_redis)
        v1_choice = choose_worker(
            enriched,
            {"payload": {"type": payload_type}},
            round_robin_state={},
        )

        shadow_redis = Mock()
        shadow_redis.hgetall.return_value = {}
        shadow_redis.llen.side_effect = lambda queue: queue_lengths.get(queue, 0)
        backend = Mock()
        backend.list_workers.return_value = workers
        worker_store = Mock()
        worker_store.list_online_workers.return_value = workers
        shadow = ShadowOrchestrator(
            shadow_redis,
            backend,
            worker_store=worker_store,
        )
        shadow.state = Mock()
        shadow.state.create_job.return_value = Mock(accepted=True)
        shadow.state.dispatch.return_value = Mock(
            accepted=True,
            code="ok",
            status="dispatched",
        )
        decision = shadow.process_event(
            "1-0",
            {
                "event_id": "event-1",
                "event_type": "job.created",
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
            },
            now_ms=100,
        )

        expected_worker = v1_choice["name"] if v1_choice else ""
        self.assertEqual(decision["selected_worker"], expected_worker)
        self.assertEqual(
            decision["decision"],
            "dispatch" if v1_choice else "no_worker",
        )
        backend.dispatch_job.assert_not_called()
        shadow_redis.rpush.assert_not_called()
        return decision

    def test_invocation_least_loaded_worker_matches(self):
        decision = self.compare(
            workers=[self.worker("worker-a"), self.worker("worker-b")],
            queue_lengths={"worker:worker-a:invocations": 2},
            payload_type="function.invoke",
            job_type="invocation",
        )
        self.assertEqual(decision["selected_worker"], "worker-b")

    def test_invocation_active_build_avoidance_matches(self):
        decision = self.compare(
            workers=[
                self.worker("worker-a", active_builds=1),
                self.worker("worker-b"),
            ],
            queue_lengths={},
            payload_type="function.invoke",
            job_type="invocation",
        )
        self.assertEqual(decision["selected_worker"], "worker-b")

    def test_build_idle_worker_requirement_matches(self):
        decision = self.compare(
            workers=[
                self.worker("worker-a", active_jobs=1),
                self.worker("worker-b"),
            ],
            queue_lengths={},
            payload_type="function.build",
            job_type="build",
        )
        self.assertEqual(decision["selected_worker"], "worker-b")

    def test_no_invocation_worker_while_all_building_matches(self):
        decision = self.compare(
            workers=[
                self.worker("worker-a", active_builds=1),
                self.worker("worker-b", active_builds=1),
            ],
            queue_lengths={},
            payload_type="function.invoke",
            job_type="invocation",
        )
        self.assertEqual(decision["decision"], "no_worker")

    def test_no_build_worker_while_all_busy_matches(self):
        decision = self.compare(
            workers=[
                self.worker("worker-a", active_jobs=1),
                self.worker("worker-b", active_jobs=2),
            ],
            queue_lengths={},
            payload_type="function.build",
            job_type="build",
        )
        self.assertEqual(decision["decision"], "no_worker")
