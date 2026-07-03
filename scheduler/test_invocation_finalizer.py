import json
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parent))

from invocation_finalizer import FinalizationError, InvocationFinalizer


class InvocationFinalizerTests(unittest.TestCase):
    def setUp(self):
        self.redis = Mock()
        self.backend = Mock()
        self.orchestrator = Mock()
        self.finalizer = InvocationFinalizer(
            self.redis,
            self.backend,
            self.orchestrator,
        )
        self.fields = {
            "payload": json.dumps(
                {
                    "job_id": "job-1",
                    "dispatch_attempt": 2,
                    "completion_id": "job-1:2:invocation",
                    "completion_status": "succeeded",
                    "completion_payload": {
                        "request_id": "request-1",
                        "result": {"ok": True},
                        "output_manifest": [],
                    },
                }
            )
        }

    def test_commit_then_terminal_transition_then_ack(self):
        self.backend.post.return_value = {"artifact_commit_id": "commit-1"}
        self.orchestrator.post.return_value = {"finalized": True}

        accepted = self.finalizer.process_message("1-0", self.fields)

        self.assertTrue(accepted)
        self.assertIn("/commit/", self.backend.post.call_args.args[0])
        self.assertEqual(
            self.orchestrator.post.call_args.args[1]["artifact_commit_id"],
            "commit-1",
        )
        self.redis.xack.assert_called_once()

    def test_backend_failure_leaves_finalization_pending(self):
        self.backend.post.side_effect = FinalizationError("backend down")

        with self.assertRaises(FinalizationError):
            self.finalizer.process_message("1-0", self.fields)

        self.orchestrator.post.assert_not_called()
        self.redis.xack.assert_not_called()

    def test_terminal_failure_after_backend_commit_is_retryable(self):
        self.backend.post.return_value = {"artifact_commit_id": "commit-1"}
        self.orchestrator.post.return_value = {
            "finalized": False,
            "code": "redis unavailable",
        }

        with self.assertRaises(FinalizationError):
            self.finalizer.process_message("1-0", self.fields)

        self.backend.post.assert_called_once()
        self.redis.xack.assert_not_called()

    def test_restart_reclaims_pending_finalization(self):
        self.backend.post.return_value = {"artifact_commit_id": "commit-1"}
        self.orchestrator.post.return_value = {"finalized": True}
        self.redis.xautoclaim.return_value = (
            "0-0",
            [("1-0", self.fields)],
            [],
        )

        reclaimed = self.finalizer.reclaim_once(min_idle_ms=0)

        self.assertEqual(reclaimed, 1)
        self.redis.xack.assert_called_once_with(
            self.finalizer.stream,
            self.finalizer.group,
            "1-0",
        )
