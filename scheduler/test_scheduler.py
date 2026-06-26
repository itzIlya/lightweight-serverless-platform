import json
import sys
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parent))

from scheduler import (
    choose_build_worker,
    choose_invocation_worker,
    choose_worker,
    make_delivery_message,
    parse_delivery_message,
    process_job_id,
    recover_stale_workers,
)


class SchedulerTests(unittest.TestCase):
    def test_choose_worker_uses_round_robin_tie_breaker(self):
        state = {}
        worker = choose_worker(
            [
                {"name": "worker-b"},
                {"name": "worker-a"},
            ],
            {"payload": {"type": "unknown"}},
            round_robin_state=state,
        )
        next_worker = choose_worker(
            [
                {"name": "worker-b"},
                {"name": "worker-a"},
            ],
            {"payload": {"type": "unknown"}},
            round_robin_state=state,
        )

        self.assertEqual(worker["name"], "worker-a")
        self.assertEqual(next_worker["name"], "worker-b")

    def test_choose_invocation_worker_uses_recent_light_worker(self):
        worker = choose_invocation_worker(
            [
                {
                    "name": "worker-a",
                    "metadata": {"active_jobs": 0, "active_builds": 0},
                    "queued_invocations": 1,
                    "queued_builds": 0,
                },
                {
                    "name": "worker-b",
                    "metadata": {"active_jobs": 0, "active_builds": 0},
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
            ],
            {"payload": {"type": "function.invoke", "function_version_id": 10}},
            recent_invocations={
                "10": {
                    "worker_name": "worker-a",
                    "last_seen": 100,
                }
            },
            affinity_ttl_seconds=10,
            sticky_max_invocation_load=2,
            round_robin_state={},
            now=105,
        )

        self.assertEqual(worker["name"], "worker-a")

    def test_choose_invocation_worker_ignores_expired_recent_worker(self):
        worker = choose_invocation_worker(
            [
                {
                    "name": "worker-a",
                    "metadata": {"active_jobs": 0, "active_builds": 0},
                    "queued_invocations": 1,
                    "queued_builds": 0,
                },
                {
                    "name": "worker-b",
                    "metadata": {"active_jobs": 0, "active_builds": 0},
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
            ],
            {"payload": {"type": "function.invoke", "function_version_id": 10}},
            recent_invocations={
                "10": {
                    "worker_name": "worker-a",
                    "last_seen": 100,
                }
            },
            affinity_ttl_seconds=10,
            sticky_max_invocation_load=2,
            round_robin_state={},
            now=111,
        )

        self.assertEqual(worker["name"], "worker-b")

    def test_choose_invocation_worker_ignores_overloaded_recent_worker(self):
        worker = choose_invocation_worker(
            [
                {
                    "name": "worker-a",
                    "metadata": {"active_jobs": 2, "active_builds": 0},
                    "queued_invocations": 1,
                    "queued_builds": 0,
                },
                {
                    "name": "worker-b",
                    "metadata": {"active_jobs": 0, "active_builds": 0},
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
            ],
            {"payload": {"type": "function.invoke", "function_version_id": 10}},
            recent_invocations={
                "10": {
                    "worker_name": "worker-a",
                    "last_seen": 100,
                }
            },
            affinity_ttl_seconds=10,
            sticky_max_invocation_load=2,
            round_robin_state={},
            now=105,
        )

        self.assertEqual(worker["name"], "worker-b")

    def test_choose_invocation_worker_prefers_no_build_queue(self):
        worker = choose_invocation_worker(
            [
                {
                    "name": "worker-a",
                    "metadata": {"active_jobs": 0, "active_builds": 0},
                    "queued_invocations": 0,
                    "queued_builds": 1,
                },
                {
                    "name": "worker-b",
                    "metadata": {"active_jobs": 0, "active_builds": 0},
                    "queued_invocations": 2,
                    "queued_builds": 0,
                },
            ],
            {"payload": {"type": "function.invoke", "function_version_id": 10}},
            recent_invocations={},
            affinity_ttl_seconds=10,
            sticky_max_invocation_load=2,
            round_robin_state={},
            now=105,
        )

        self.assertEqual(worker["name"], "worker-b")

    def test_choose_invocation_worker_avoids_active_builds(self):
        worker = choose_invocation_worker(
            [
                {
                    "name": "worker-a",
                    "metadata": {"active_jobs": 1, "active_builds": 1},
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
                {
                    "name": "worker-b",
                    "metadata": {"active_jobs": 0, "active_builds": 0},
                    "queued_invocations": 2,
                    "queued_builds": 0,
                },
            ],
            {"payload": {"type": "function.invoke", "function_version_id": 10}},
            recent_invocations={},
            affinity_ttl_seconds=10,
            sticky_max_invocation_load=2,
            round_robin_state={},
            now=105,
        )

        self.assertEqual(worker["name"], "worker-b")

    def test_choose_invocation_worker_returns_none_when_every_worker_building(self):
        worker = choose_invocation_worker(
            [
                {
                    "name": "worker-a",
                    "metadata": {"active_jobs": 1, "active_builds": 1},
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
                {
                    "name": "worker-b",
                    "metadata": {"active_jobs": 1, "active_builds": 1},
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
            ],
            {"payload": {"type": "function.invoke", "function_version_id": 10}},
            recent_invocations={},
            affinity_ttl_seconds=10,
            sticky_max_invocation_load=2,
            round_robin_state={},
            now=105,
        )

        self.assertIsNone(worker)

    def test_choose_build_worker_requires_idle_worker(self):
        worker = choose_build_worker(
            [
                {
                    "name": "worker-a",
                    "metadata": {"active_jobs": 1, "active_builds": 0},
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
                {
                    "name": "worker-b",
                    "metadata": {"active_jobs": 0, "active_builds": 0},
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
            ],
            round_robin_state={},
        )

        self.assertEqual(worker["name"], "worker-b")

    def test_choose_build_worker_returns_none_without_idle_worker(self):
        worker = choose_build_worker(
            [
                {
                    "name": "worker-a",
                    "metadata": {"active_jobs": 1, "active_builds": 0},
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
                {
                    "name": "worker-b",
                    "metadata": {"active_jobs": 0, "active_builds": 0},
                    "queued_invocations": 1,
                    "queued_builds": 0,
                },
            ],
            round_robin_state={},
        )

        self.assertIsNone(worker)

    def test_delivery_message_round_trips_job_id_and_attempt(self):
        message = make_delivery_message("job-1", 3)

        self.assertEqual(
            parse_delivery_message(message),
            {
                "job_id": "job-1",
                "dispatch_attempt": 3,
            },
        )

    def test_process_job_dispatches_delivery_message_to_worker_queue(self):
        backend = Mock()
        redis_client = Mock()
        backend.get_job.return_value = {
            "job_id": "job-1",
            "type": "build",
            "status": "queued",
            "payload": {
                "job_id": "job-1",
                "type": "function.build",
                "build_request_id": "build-1",
            },
        }
        backend.list_workers.return_value = [
            {
                "name": "worker-a",
                "invocation_queue_name": "worker:worker-a:invocations",
                "build_queue_name": "worker:worker-a:builds",
            }
        ]
        backend.dispatch_job.return_value = {
            "dispatched": True,
            "job": {
                "payload": {
                    "dispatch_attempt": 1,
                }
            },
        }

        dispatched = process_job_id(
            job_id="job-1",
            backend=backend,
            redis_client=redis_client,
            pending_queue="scheduler-pending-builds",
            pending_queues={
                "function.invoke": "scheduler-pending-invocations",
                "function.build": "scheduler-pending-builds",
            },
            requeue_delay_seconds=0,
        )

        self.assertTrue(dispatched)
        queue_name, delivery_message = redis_client.rpush.call_args.args
        self.assertEqual(queue_name, "worker:worker-a:builds")
        self.assertEqual(
            json.loads(delivery_message),
            {
                "job_id": "job-1",
                "dispatch_attempt": 1,
            },
        )
        backend.dispatch_job.assert_called_once_with(
            "job-1",
            worker_name="worker-a",
            queue_name="worker:worker-a:builds",
        )

    def test_process_job_requeues_when_no_workers_are_available(self):
        backend = Mock()
        redis_client = Mock()
        backend.get_job.return_value = {
            "job_id": "job-1",
            "type": "build",
            "status": "queued",
            "payload": {"job_id": "job-1", "type": "function.build"},
        }
        backend.list_workers.return_value = []

        dispatched = process_job_id(
            job_id="job-1",
            backend=backend,
            redis_client=redis_client,
            pending_queue="scheduler-pending-jobs",
            pending_queues={
                "function.invoke": "scheduler-pending-invocations",
                "function.build": "scheduler-pending-builds",
            },
            requeue_delay_seconds=0,
        )

        self.assertFalse(dispatched)
        redis_client.rpush.assert_called_once_with("scheduler-pending-builds", "job-1")
        backend.dispatch_job.assert_not_called()

    def test_process_job_requeues_when_job_is_not_available_yet(self):
        backend = Mock()
        redis_client = Mock()
        backend.get_job.return_value = {
            "job_id": "job-1",
            "type": "invocation",
            "status": "queued",
            "available_at": (
                datetime.now(timezone.utc) + timedelta(seconds=5)
            ).isoformat(),
            "payload": {"job_id": "job-1", "type": "function.invoke"},
        }

        dispatched = process_job_id(
            job_id="job-1",
            backend=backend,
            redis_client=redis_client,
            pending_queue="scheduler-pending-jobs",
            pending_queues={
                "function.invoke": "scheduler-pending-invocations",
                "function.build": "scheduler-pending-builds",
            },
            requeue_delay_seconds=0,
        )

        self.assertFalse(dispatched)
        redis_client.rpush.assert_called_once_with(
            "scheduler-pending-invocations",
            "job-1",
        )
        backend.list_workers.assert_not_called()
        backend.dispatch_job.assert_not_called()

    def test_process_job_requeues_database_state_when_worker_push_fails(self):
        backend = Mock()
        redis_client = Mock()
        backend.get_job.return_value = {
            "job_id": "job-1",
            "type": "build",
            "status": "queued",
            "payload": {"job_id": "job-1", "type": "function.build"},
        }
        backend.list_workers.return_value = [
            {
                "name": "worker-a",
                "invocation_queue_name": "worker:worker-a:invocations",
                "build_queue_name": "worker:worker-a:builds",
            }
        ]
        backend.dispatch_job.return_value = {
            "dispatched": True,
            "job": {
                "payload": {
                    "dispatch_attempt": 1,
                }
            },
        }
        redis_client.rpush.side_effect = RuntimeError("redis unavailable")

        with self.assertRaises(RuntimeError):
            process_job_id(
                job_id="job-1",
                backend=backend,
                redis_client=redis_client,
                pending_queue="scheduler-pending-jobs",
                requeue_delay_seconds=0,
            )

        backend.requeue_job.assert_called_once_with(
            "job-1",
            worker_name="worker-a",
            reason="Scheduler failed to push job ID to worker queue.",
        )

    def test_recover_stale_workers_requeues_processing_jobs(self):
        backend = Mock()
        redis_client = Mock()
        backend.expire_stale_workers.return_value = {
            "expired": [
                {
                    "name": "worker-a",
                    "processing_queue_name": "worker:worker-a:processing",
                }
            ]
        }
        delivery_message = make_delivery_message("job-1", 1)
        redis_client.lrange.return_value = [delivery_message]
        backend.get_job.return_value = {
            "job_id": "job-1",
            "status": "running",
            "payload": {"type": "function.invoke"},
        }
        backend.requeue_job.return_value = {
            "requeued": True,
            "job": {
                "queue_name": "scheduler-pending-invocations",
                "payload": {"type": "function.invoke"},
            },
        }

        recovered = recover_stale_workers(
            backend=backend,
            redis_client=redis_client,
            pending_queue="scheduler-pending-jobs",
            pending_queues={
                "function.invoke": "scheduler-pending-invocations",
                "function.build": "scheduler-pending-builds",
            },
            stale_after_seconds=30,
        )

        self.assertEqual(recovered, 1)
        backend.expire_stale_workers.assert_called_once_with(stale_after_seconds=30)
        backend.requeue_job.assert_called_once_with(
            "job-1",
            worker_name="worker-a",
            reason="Worker worker-a missed heartbeat.",
            recovery=True,
        )
        redis_client.lrem.assert_called_once_with(
            "worker:worker-a:processing",
            1,
            delivery_message,
        )
        redis_client.rpush.assert_called_once_with(
            "scheduler-pending-invocations",
            "job-1",
        )

    def test_recover_stale_workers_removes_dead_lettered_processing_job(self):
        backend = Mock()
        redis_client = Mock()
        backend.expire_stale_workers.return_value = {
            "expired": [
                {
                    "name": "worker-a",
                    "processing_queue_name": "worker:worker-a:processing",
                }
            ]
        }
        delivery_message = make_delivery_message("job-1", 1)
        redis_client.lrange.return_value = [delivery_message]
        backend.get_job.return_value = {
            "job_id": "job-1",
            "status": "running",
        }
        backend.requeue_job.return_value = {
            "requeued": False,
            "dead_lettered": True,
            "status": "dead_lettered",
        }

        recovered = recover_stale_workers(
            backend=backend,
            redis_client=redis_client,
            pending_queue="scheduler-pending-jobs",
            stale_after_seconds=30,
        )

        self.assertEqual(recovered, 0)
        backend.requeue_job.assert_called_once_with(
            "job-1",
            worker_name="worker-a",
            reason="Worker worker-a missed heartbeat.",
            recovery=True,
        )
        redis_client.lrem.assert_called_once_with(
            "worker:worker-a:processing",
            1,
            delivery_message,
        )
        redis_client.rpush.assert_not_called()

    def test_recover_stale_workers_cleans_terminal_processing_jobs(self):
        backend = Mock()
        redis_client = Mock()
        backend.expire_stale_workers.return_value = {
            "expired": [
                {
                    "name": "worker-a",
                    "processing_queue_name": "worker:worker-a:processing",
                }
            ]
        }
        delivery_message = make_delivery_message("job-1", 1)
        redis_client.lrange.return_value = [delivery_message]
        backend.get_job.return_value = {
            "job_id": "job-1",
            "status": "succeeded",
        }

        recovered = recover_stale_workers(
            backend=backend,
            redis_client=redis_client,
            pending_queue="scheduler-pending-jobs",
            stale_after_seconds=30,
        )

        self.assertEqual(recovered, 0)
        backend.requeue_job.assert_not_called()
        redis_client.lrem.assert_called_once_with(
            "worker:worker-a:processing",
            1,
            delivery_message,
        )
        redis_client.rpush.assert_not_called()


if __name__ == "__main__":
    unittest.main()
