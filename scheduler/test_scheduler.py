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
    invocation_route_key,
    invocation_warm_key,
    make_delivery_message,
    parse_delivery_message,
    process_job_id,
    recover_stale_workers,
    remember_local_warm_reservation,
    worker_idle_warm_count,
    worker_recovery_queues,
)


class SchedulerTests(unittest.TestCase):
    def test_v1_scheduler_refuses_v2_job(self):
        backend = Mock()
        redis_client = Mock()
        backend.get_job.return_value = {
            "job_id": "job-v2",
            "coordination_version": 2,
            "status": "queued",
        }

        dispatched = process_job_id(
            job_id="job-v2",
            backend=backend,
            redis_client=redis_client,
            pending_queue="scheduler-pending-jobs",
            requeue_delay_seconds=0,
        )

        self.assertFalse(dispatched)
        backend.list_workers.assert_not_called()
        backend.dispatch_job.assert_not_called()
        redis_client.rpush.assert_not_called()

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

    def warm_metadata(self, *, idle_count=1, image_ref="image:v1"):
        return {
            "active_jobs": 0,
            "active_builds": 0,
            "max_invocation_concurrency": 4,
            "warm_pool": {
                "enabled": True,
                "containers": [
                    {
                        "function_version_id": "10",
                        "image_ref": image_ref,
                        "handler": "handler.main",
                        "memory_mb": 128,
                        "output_tmpfs_size_bytes": 10 * 1024 * 1024,
                        "idle_count": idle_count,
                        "busy_count": 0,
                    }
                ],
            },
        }

    def warm_job(self, *, image_ref="image:v1"):
        return {
            "payload": {
                "type": "function.invoke",
                "function_version_id": 10,
                "image_ref": image_ref,
                "handler": "handler.main",
                "config": {"memory_mb": 128},
                "invocation_output_max_total_size_mb": 10,
            }
        }

    def test_choose_invocation_worker_prefers_exact_idle_warm_container(self):
        worker = choose_invocation_worker(
            [
                {
                    "name": "worker-a",
                    "max_concurrency": 4,
                    "metadata": self.warm_metadata(),
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
            self.warm_job(),
            round_robin_state={},
            now=105,
        )

        self.assertEqual(worker["name"], "worker-a")

    def test_choose_invocation_worker_falls_back_to_least_loaded_without_warm_match(self):
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
            round_robin_state={},
            now=111,
        )

        self.assertEqual(worker["name"], "worker-b")

    def test_choose_invocation_worker_ignores_warm_image_mismatch(self):
        worker = choose_invocation_worker(
            [
                {
                    "name": "worker-a",
                    "metadata": self.warm_metadata(image_ref="image:old"),
                    "queued_invocations": 2,
                    "queued_builds": 0,
                },
                {
                    "name": "worker-b",
                    "metadata": {"active_jobs": 0, "active_builds": 0},
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
            ],
            self.warm_job(image_ref="image:v1"),
            round_robin_state={},
            now=105,
        )

        self.assertEqual(worker["name"], "worker-b")

    def test_choose_invocation_worker_ignores_warm_worker_with_active_build(self):
        worker = choose_invocation_worker(
            [
                {
                    "name": "worker-a",
                    "metadata": {
                        **self.warm_metadata(),
                        "active_jobs": 1,
                        "active_builds": 1,
                    },
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
            self.warm_job(),
            round_robin_state={},
            now=105,
        )

        self.assertEqual(worker["name"], "worker-b")

    def test_choose_invocation_worker_uses_predictive_sticky_route_as_hint(self):
        job = self.warm_job()
        worker = choose_invocation_worker(
            [
                {
                    "name": "worker-a",
                    "max_concurrency": 4,
                    "metadata": {
                        "active_jobs": 0,
                        "active_builds": 0,
                        "max_invocation_concurrency": 4,
                    },
                    "queued_invocations": 1,
                    "queued_builds": 0,
                },
                {
                    "name": "worker-b",
                    "max_concurrency": 4,
                    "metadata": {
                        "active_jobs": 0,
                        "active_builds": 0,
                        "max_invocation_concurrency": 4,
                    },
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
            ],
            job,
            local_recent_invocation_routes={
                invocation_route_key(job): {
                    "worker_name": "worker-a",
                    "updated_at": 99,
                }
            },
            local_load_ttl_seconds=10,
            round_robin_state={},
            now=100,
        )

        self.assertEqual(worker["name"], "worker-a")

    def test_choose_invocation_worker_does_not_let_predictive_sticky_hide_pressure(self):
        job = self.warm_job()
        worker = choose_invocation_worker(
            [
                {
                    "name": "worker-a",
                    "max_concurrency": 4,
                    "metadata": {
                        "active_jobs": 0,
                        "active_builds": 0,
                        "max_invocation_concurrency": 4,
                    },
                    "queued_invocations": 2,
                    "queued_builds": 0,
                },
                {
                    "name": "worker-b",
                    "max_concurrency": 4,
                    "metadata": {
                        "active_jobs": 0,
                        "active_builds": 0,
                        "max_invocation_concurrency": 4,
                    },
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
            ],
            job,
            local_recent_invocation_routes={
                invocation_route_key(job): {
                    "worker_name": "worker-a",
                    "updated_at": 99,
                }
            },
            local_load_ttl_seconds=10,
            predictive_sticky_load_slack=1,
            round_robin_state={},
            now=100,
        )

        self.assertEqual(worker["name"], "worker-b")

    def test_choose_invocation_worker_limits_predictive_sticky_local_burst(self):
        job = self.warm_job()
        worker = choose_invocation_worker(
            [
                {
                    "name": "worker-a",
                    "max_concurrency": 4,
                    "metadata": {
                        "active_jobs": 0,
                        "active_builds": 0,
                        "max_invocation_concurrency": 4,
                    },
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
                {
                    "name": "worker-b",
                    "max_concurrency": 4,
                    "metadata": {
                        "active_jobs": 0,
                        "active_builds": 0,
                        "max_invocation_concurrency": 4,
                    },
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
            ],
            job,
            local_invocation_loads={"worker-a": [99, 99]},
            local_recent_invocation_routes={
                invocation_route_key(job): {
                    "worker_name": "worker-a",
                    "updated_at": 99,
                }
            },
            local_load_ttl_seconds=10,
            predictive_sticky_max_local_dispatches=1,
            round_robin_state={},
            now=100,
        )

        self.assertEqual(worker["name"], "worker-b")

    def test_choose_invocation_worker_prefers_known_warm_over_predictive_sticky(self):
        job = self.warm_job()
        worker = choose_invocation_worker(
            [
                {
                    "name": "worker-a",
                    "max_concurrency": 4,
                    "metadata": {
                        "active_jobs": 0,
                        "active_builds": 0,
                        "max_invocation_concurrency": 4,
                    },
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
                {
                    "name": "worker-b",
                    "metadata": self.warm_metadata(),
                    "queued_invocations": 1,
                    "queued_builds": 0,
                },
            ],
            job,
            local_recent_invocation_routes={
                invocation_route_key(job): {
                    "worker_name": "worker-a",
                    "updated_at": 99,
                }
            },
            local_load_ttl_seconds=10,
            round_robin_state={},
            now=100,
        )

        self.assertEqual(worker["name"], "worker-b")

    def test_choose_invocation_worker_ignores_stale_predictive_sticky_route(self):
        job = self.warm_job()
        worker = choose_invocation_worker(
            [
                {
                    "name": "worker-a",
                    "max_concurrency": 4,
                    "metadata": {
                        "active_jobs": 0,
                        "active_builds": 0,
                        "max_invocation_concurrency": 4,
                    },
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
                {
                    "name": "worker-b",
                    "max_concurrency": 4,
                    "metadata": {
                        "active_jobs": 0,
                        "active_builds": 0,
                        "max_invocation_concurrency": 4,
                    },
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
            ],
            job,
            local_recent_invocation_routes={
                invocation_route_key(job): {
                    "worker_name": "worker-b",
                    "updated_at": 80,
                }
            },
            local_load_ttl_seconds=10,
            round_robin_state={},
            now=100,
        )

        self.assertEqual(worker["name"], "worker-a")

    def test_local_warm_reservation_prevents_overbooking_one_idle_container(self):
        job = self.warm_job()
        worker = {
            "name": "worker-a",
            "metadata": self.warm_metadata(idle_count=1),
            "queued_invocations": 0,
            "queued_builds": 0,
        }
        reservations = {}

        remember_local_warm_reservation(
            job,
            worker,
            local_warm_reservations=reservations,
            local_load_ttl_seconds=10,
        )

        self.assertEqual(
            worker_idle_warm_count(
                worker,
                invocation_warm_key(job),
                local_warm_reservations=reservations,
                local_load_ttl_seconds=10,
                now=105,
            ),
            0,
        )

    def test_choose_invocation_worker_uses_local_dispatch_load_for_bursts(self):
        worker = choose_invocation_worker(
            [
                {
                    "name": "worker-a",
                    "max_concurrency": 4,
                    "metadata": {
                        "active_jobs": 0,
                        "active_builds": 0,
                        "max_invocation_concurrency": 4,
                    },
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
                {
                    "name": "worker-b",
                    "max_concurrency": 4,
                    "metadata": {
                        "active_jobs": 0,
                        "active_builds": 0,
                        "max_invocation_concurrency": 4,
                    },
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
                {
                    "name": "worker-c",
                    "max_concurrency": 4,
                    "metadata": {
                        "active_jobs": 0,
                        "active_builds": 0,
                        "max_invocation_concurrency": 4,
                    },
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
            ],
            {"payload": {"type": "function.invoke", "function_version_id": 10}},
            local_invocation_loads={
                "worker-a": [99, 99, 99, 99],
                "worker-b": [99],
            },
            local_load_ttl_seconds=10,
            round_robin_state={},
            now=100,
        )

        self.assertEqual(worker["name"], "worker-c")

    def test_choose_invocation_worker_honors_local_dispatch_load_for_repeat_calls(self):
        worker = choose_invocation_worker(
            [
                {
                    "name": "worker-a",
                    "max_concurrency": 4,
                    "metadata": {
                        "active_jobs": 0,
                        "active_builds": 0,
                        "max_invocation_concurrency": 4,
                    },
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
                {
                    "name": "worker-b",
                    "max_concurrency": 4,
                    "metadata": {
                        "active_jobs": 0,
                        "active_builds": 0,
                        "max_invocation_concurrency": 4,
                    },
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
            ],
            {"payload": {"type": "function.invoke", "function_version_id": 10}},
            local_invocation_loads={"worker-a": [99, 99, 99]},
            local_load_ttl_seconds=10,
            round_robin_state={},
            now=100,
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
            round_robin_state={},
            now=105,
        )

        self.assertIsNone(worker)

    def test_choose_build_worker_avoids_active_builds(self):
        worker = choose_build_worker(
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
                    "queued_invocations": 0,
                    "queued_builds": 0,
                },
            ],
            round_robin_state={},
        )

        self.assertEqual(worker["name"], "worker-b")

    def test_choose_build_worker_prefers_lowest_invocation_pressure(self):
        worker = choose_build_worker(
            [
                {
                    "name": "worker-a",
                    "metadata": {"active_jobs": 2, "active_builds": 0, "active_invocations": 2},
                    "queued_invocations": 1,
                    "queued_builds": 0,
                },
                {
                    "name": "worker-b",
                    "metadata": {"active_jobs": 1, "active_builds": 0, "active_invocations": 1},
                    "queued_invocations": 1,
                    "queued_builds": 0,
                },
                {
                    "name": "worker-c",
                    "metadata": {"active_jobs": 0, "active_builds": 0, "active_invocations": 0},
                    "queued_invocations": 4,
                    "queued_builds": 0,
                },
            ],
            round_robin_state={},
        )

        self.assertEqual(worker["name"], "worker-b")

    def test_choose_build_worker_uses_queue_and_round_robin_for_ties(self):
        state = {}
        workers = [
            {
                "name": "worker-a",
                "metadata": {"active_jobs": 0, "active_builds": 0},
                "queued_invocations": 0,
                "queued_builds": 1,
            },
            {
                "name": "worker-b",
                "metadata": {"active_jobs": 0, "active_builds": 0},
                "queued_invocations": 0,
                "queued_builds": 0,
            },
            {
                "name": "worker-c",
                "metadata": {"active_jobs": 0, "active_builds": 0},
                "queued_invocations": 0,
                "queued_builds": 0,
            },
        ]

        first = choose_build_worker(workers, round_robin_state=state)
        second = choose_build_worker(workers, round_robin_state=state)

        self.assertEqual(first["name"], "worker-b")
        self.assertEqual(second["name"], "worker-c")

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

    def test_process_job_expires_stale_workers_before_placement(self):
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
            requeue_delay_seconds=0,
            stale_after_seconds=30,
        )

        self.assertTrue(dispatched)
        backend.expire_stale_workers.assert_called_once_with(
            stale_after_seconds=30,
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

    def test_recover_stale_workers_requeues_delivery_queue_jobs(self):
        backend = Mock()
        redis_client = Mock()
        backend.expire_stale_workers.return_value = {
            "expired": [
                {
                    "name": "worker-a",
                    "queue_name": "worker:worker-a:jobs",
                    "invocation_queue_name": "worker:worker-a:invocations",
                    "build_queue_name": "worker:worker-a:builds",
                    "processing_queue_name": "worker:worker-a:processing",
                }
            ]
        }
        delivery_message = make_delivery_message("job-1", 1)
        redis_client.lrange.side_effect = [
            [],
            [],
            [delivery_message],
            [],
        ]
        backend.get_job.return_value = {
            "job_id": "job-1",
            "status": "dispatched",
            "payload": {"type": "function.build"},
        }
        backend.requeue_job.return_value = {
            "requeued": True,
            "job": {
                "queue_name": "scheduler-pending-builds",
                "payload": {"type": "function.build"},
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
        self.assertEqual(
            [call.args[0] for call in redis_client.lrange.call_args_list],
            [
                "worker:worker-a:processing",
                "worker:worker-a:invocations",
                "worker:worker-a:builds",
                "worker:worker-a:jobs",
            ],
        )
        redis_client.lrem.assert_called_once_with(
            "worker:worker-a:builds",
            1,
            delivery_message,
        )
        redis_client.rpush.assert_called_once_with(
            "scheduler-pending-builds",
            "job-1",
        )

    def test_worker_recovery_queues_are_unique_and_ordered(self):
        self.assertEqual(
            worker_recovery_queues(
                {
                    "queue_name": "worker:worker-a:jobs",
                    "invocation_queue_name": "worker:worker-a:jobs",
                    "build_queue_name": "worker:worker-a:builds",
                    "processing_queue_name": "worker:worker-a:processing",
                }
            ),
            [
                "worker:worker-a:processing",
                "worker:worker-a:jobs",
                "worker:worker-a:builds",
            ],
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
