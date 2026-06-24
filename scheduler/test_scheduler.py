import json
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parent))

from scheduler import (
    choose_worker,
    make_delivery_message,
    parse_delivery_message,
    process_job_id,
    recover_stale_workers,
)


class SchedulerTests(unittest.TestCase):
    def test_choose_worker_uses_first_worker_by_name(self):
        worker = choose_worker(
            [
                {"name": "worker-b"},
                {"name": "worker-a"},
            ],
            {"type": "build"},
        )

        self.assertEqual(worker["name"], "worker-a")

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
                "queue_name": "worker:worker-a:jobs",
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
            pending_queue="scheduler-pending-jobs",
            requeue_delay_seconds=0,
        )

        self.assertTrue(dispatched)
        queue_name, delivery_message = redis_client.rpush.call_args.args
        self.assertEqual(queue_name, "worker:worker-a:jobs")
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
            queue_name="worker:worker-a:jobs",
        )

    def test_process_job_requeues_when_no_workers_are_available(self):
        backend = Mock()
        redis_client = Mock()
        backend.get_job.return_value = {
            "job_id": "job-1",
            "type": "build",
            "status": "queued",
            "payload": {"job_id": "job-1"},
        }
        backend.list_workers.return_value = []

        dispatched = process_job_id(
            job_id="job-1",
            backend=backend,
            redis_client=redis_client,
            pending_queue="scheduler-pending-jobs",
            requeue_delay_seconds=0,
        )

        self.assertFalse(dispatched)
        redis_client.rpush.assert_called_once_with("scheduler-pending-jobs", "job-1")
        backend.dispatch_job.assert_not_called()

    def test_process_job_requeues_database_state_when_worker_push_fails(self):
        backend = Mock()
        redis_client = Mock()
        backend.get_job.return_value = {
            "job_id": "job-1",
            "type": "build",
            "status": "queued",
            "payload": {"job_id": "job-1"},
        }
        backend.list_workers.return_value = [
            {
                "name": "worker-a",
                "queue_name": "worker:worker-a:jobs",
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
        }
        backend.requeue_job.return_value = {"requeued": True}

        recovered = recover_stale_workers(
            backend=backend,
            redis_client=redis_client,
            pending_queue="scheduler-pending-jobs",
            stale_after_seconds=30,
        )

        self.assertEqual(recovered, 1)
        backend.expire_stale_workers.assert_called_once_with(stale_after_seconds=30)
        backend.requeue_job.assert_called_once_with(
            "job-1",
            worker_name="worker-a",
            reason="Worker worker-a missed heartbeat.",
        )
        redis_client.lrem.assert_called_once_with(
            "worker:worker-a:processing",
            1,
            delivery_message,
        )
        redis_client.rpush.assert_called_once_with("scheduler-pending-jobs", "job-1")

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
