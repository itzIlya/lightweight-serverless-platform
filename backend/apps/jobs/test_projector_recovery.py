from unittest.mock import Mock, patch

from django.test import SimpleTestCase

from .projector import OrchestratorProjector


class OrchestratorProjectorRecoveryTests(SimpleTestCase):
    def test_projection_failure_keeps_stream_entry_pending(self):
        redis_client = Mock()
        redis_client.xreadgroup.return_value = [
            (
                "orchestrator:v2:projections",
                [("1-0", {"event_type": "job.succeeded", "payload": "{}"})],
            )
        ]
        projector = OrchestratorProjector(redis_client)

        with patch(
            "apps.jobs.projector.apply_orchestrator_projection",
            side_effect=RuntimeError("postgres unavailable"),
        ):
            with self.assertRaises(RuntimeError):
                projector.process_once(block_ms=0)

        redis_client.xack.assert_not_called()

    def test_restart_reclaims_and_acks_projection_after_success(self):
        redis_client = Mock()
        fields = {"event_type": "job.succeeded", "payload": "{}"}
        redis_client.xautoclaim.return_value = ("0-0", [("1-0", fields)], [])
        projector = OrchestratorProjector(redis_client)

        with patch(
            "apps.jobs.projector.apply_orchestrator_projection",
            return_value=True,
        ):
            reclaimed = projector.reclaim_once(min_idle_ms=0)

        self.assertEqual(reclaimed, 1)
        redis_client.xack.assert_called_once_with(
            projector.stream,
            projector.group,
            "1-0",
        )
