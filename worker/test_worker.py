from pathlib import Path
import tempfile
import sys
import unittest
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parent))

from backend_client import BackendReportError
from builder import BuildCancelled, BuildError, BuildResult
from executor import DockerExecutor
from worker import (
    acknowledge_processing_job,
    claim_job_for_execution,
    job_report_metadata,
    move_job_to_processing,
    parse_delivery_message,
    process_build_job,
    worker_processing_queue_name,
)


class BuildWorkerTests(unittest.TestCase):
    def test_worker_processing_queue_name_replaces_jobs_suffix(self):
        self.assertEqual(
            worker_processing_queue_name("worker:worker-a:jobs"),
            "worker:worker-a:processing",
        )

    def test_move_job_to_processing_uses_atomic_redis_move(self):
        redis_client = Mock()
        redis_client.execute_command.return_value = "job-1"

        job_id = move_job_to_processing(
            redis_client,
            "worker:worker-a:jobs",
            "worker:worker-a:processing",
        )

        self.assertEqual(job_id, "job-1")
        redis_client.execute_command.assert_called_once_with(
            "BLMOVE",
            "worker:worker-a:jobs",
            "worker:worker-a:processing",
            "LEFT",
            "RIGHT",
            5,
        )

    def test_acknowledge_processing_job_removes_job_id(self):
        redis_client = Mock()

        acknowledge_processing_job(
            redis_client,
            "worker:worker-a:processing",
            "job-1",
        )

        redis_client.lrem.assert_called_once_with(
            "worker:worker-a:processing",
            1,
            "job-1",
        )

    def test_parse_delivery_message_reads_json_envelope(self):
        self.assertEqual(
            parse_delivery_message('{"job_id":"job-1","dispatch_attempt":2}'),
            {
                "job_id": "job-1",
                "dispatch_attempt": 2,
            },
        )

    def test_parse_delivery_message_supports_legacy_job_id(self):
        self.assertEqual(
            parse_delivery_message("job-1"),
            {
                "job_id": "job-1",
                "dispatch_attempt": None,
            },
        )

    def test_claim_job_returns_payload_when_claimed(self):
        backend = Mock()
        backend.claim_job.return_value = {
            "claimed": True,
            "job": {
                "job_id": "job-1",
                "status": "running",
                "payload": {"type": "function.invoke"},
            },
        }

        payload = claim_job_for_execution(
            backend,
            job_id="job-1",
            worker_name="worker-a",
            dispatch_attempt=2,
        )

        self.assertEqual(payload, {"type": "function.invoke"})
        backend.claim_job.assert_called_once_with(
            "job-1",
            {
                "worker_name": "worker-a",
                "dispatch_attempt": 2,
            },
        )

    def test_claim_job_skips_unclaimed_jobs(self):
        backend = Mock()
        backend.claim_job.return_value = {
            "claimed": False,
            "stale": True,
            "status": "queued",
        }

        payload = claim_job_for_execution(
            backend,
            job_id="job-1",
            worker_name="worker-a",
            dispatch_attempt=2,
        )

        self.assertIsNone(payload)

    def test_claim_job_skips_deliveries_without_attempt(self):
        backend = Mock()

        payload = claim_job_for_execution(
            backend,
            job_id="job-1",
            worker_name="worker-a",
            dispatch_attempt=None,
        )

        self.assertIsNone(payload)
        backend.claim_job.assert_not_called()

    def test_job_report_metadata_uses_dispatch_context(self):
        metadata = job_report_metadata(
            {
                "job_id": "job-1",
                "dispatch_attempt": 2,
                "assigned_worker": "worker-a",
            }
        )

        self.assertEqual(
            metadata,
            {
                "job_id": "job-1",
                "dispatch_attempt": 2,
                "worker_name": "worker-a",
            },
        )

    def test_successful_build_reports_building_then_built(self):
        backend = Mock()
        backend.is_build_cancel_requested.return_value = False
        backend.acquire_build_lease.return_value = {
            "granted": True,
            "lease_id": 101,
        }
        backend.download_build_source.side_effect = (
            lambda build_request_id, destination: destination.write_bytes(b"zip")
        )
        builder = Mock()
        builder.build.return_value = BuildResult(
            image_ref="localhost:5000/functions/echo:v1-v1",
            build_log="built and pushed",
            duration_ms=123,
        )
        job = {
            "build_request_id": "build-1",
            "image_ref": "localhost:5000/functions/echo:v1-v1",
        }

        process_build_job(job, backend, builder)

        self.assertEqual(backend.report_build.call_count, 2)
        backend.acquire_build_lease.assert_called_once()
        backend.release_build_lease.assert_called_once()
        first_payload = backend.report_build.call_args_list[0].args[1]
        final_payload = backend.report_build.call_args_list[1].args[1]
        self.assertEqual(first_payload["status"], "building")
        self.assertEqual(final_payload["status"], "built")
        self.assertEqual(
            final_payload["image_ref"],
            "localhost:5000/functions/echo:v1-v1",
        )
        self.assertEqual(final_payload["build_log"], "built and pushed")

    def test_builder_failure_is_reported_as_failed(self):
        backend = Mock()
        backend.is_build_cancel_requested.return_value = False
        backend.acquire_build_lease.return_value = {
            "granted": True,
            "lease_id": 102,
        }
        backend.download_build_source.side_effect = (
            lambda build_request_id, destination: destination.write_bytes(b"zip")
        )
        builder = Mock()
        builder.build.side_effect = BuildError("Unsupported runtime: node22")

        process_build_job(
            {"build_request_id": "build-2"},
            backend,
            builder,
        )

        final_payload = backend.report_build.call_args_list[-1].args[1]
        self.assertEqual(final_payload["status"], "failed")
        self.assertIn("Unsupported runtime", final_payload["build_log"])
        backend.release_build_lease.assert_called_once()

    def test_source_download_failure_is_reported_as_failed(self):
        backend = Mock()
        backend.is_build_cancel_requested.return_value = False
        backend.acquire_build_lease.return_value = {
            "granted": True,
            "lease_id": 103,
        }
        backend.download_build_source.side_effect = BackendReportError(
            "source download failed"
        )
        builder = Mock()

        process_build_job(
            {"build_request_id": "build-3"},
            backend,
            builder,
        )

        builder.build.assert_not_called()
        final_payload = backend.report_build.call_args_list[-1].args[1]
        self.assertEqual(final_payload["status"], "failed")
        self.assertIn("source download failed", final_payload["build_log"])
        backend.release_build_lease.assert_called_once()

    def test_cancelled_queued_job_never_reaches_builder(self):
        backend = Mock()
        backend.is_build_cancel_requested.return_value = True
        builder = Mock()

        process_build_job(
            {"build_request_id": "build-4"},
            backend,
            builder,
        )

        builder.build.assert_not_called()
        final_payload = backend.report_build.call_args_list[-1].args[1]
        self.assertEqual(final_payload["status"], "cancelled")

    def test_cancellation_during_build_is_reported(self):
        backend = Mock()
        backend.is_build_cancel_requested.return_value = False
        backend.acquire_build_lease.return_value = {
            "granted": True,
            "lease_id": 104,
        }
        backend.download_build_source.side_effect = (
            lambda build_request_id, destination: destination.write_bytes(b"zip")
        )
        builder = Mock()
        builder.build.side_effect = BuildCancelled("Build cancelled by user.")

        process_build_job(
            {"build_request_id": "build-5"},
            backend,
            builder,
        )

        final_payload = backend.report_build.call_args_list[-1].args[1]
        self.assertEqual(final_payload["status"], "cancelled")
        backend.release_build_lease.assert_called_once()

    def test_build_without_available_lease_is_requeued(self):
        backend = Mock()
        backend.is_build_cancel_requested.return_value = False
        backend.acquire_build_lease.return_value = {
            "granted": False,
            "reason": "Global build concurrency limit reached.",
        }
        builder = Mock()
        requeue = Mock()

        process_build_job(
            {"build_request_id": "build-6"},
            backend,
            builder,
            worker_name="worker-a",
            requeue=requeue,
        )

        builder.build.assert_not_called()
        backend.report_build.assert_not_called()
        backend.release_build_lease.assert_not_called()
        requeue.assert_called_once()

    def test_invocation_inputs_are_downloaded_into_sandbox(self):
        backend = Mock()
        backend.list_invocation_inputs.return_value = [
            {
                "id": 11,
                "position": 0,
                "original_name": "document.pdf",
                "content_type": "application/pdf",
                "size_bytes": 4,
            }
        ]

        def download(request_id, file_id, destination):
            destination.write_bytes(b"pdf")

        backend.download_invocation_input.side_effect = download
        executor = DockerExecutor(docker_client=Mock(), backend_client=backend)

        with tempfile.TemporaryDirectory() as root:
            files_dir = Path(root) / "files"
            files_dir.mkdir()
            prepared = executor._prepare_input_files(
                {"request_id": "request-1"},
                files_dir,
            )
            self.assertEqual(len(prepared), 1)
            self.assertEqual(prepared[0]["name"], "document.pdf")
            self.assertTrue((files_dir / "000-document.pdf").exists())

    def test_input_archive_keeps_the_input_directory_layout(self):
        executor = DockerExecutor(docker_client=Mock())

        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            input_dir = root_path / "input"
            files_dir = input_dir / "files"
            files_dir.mkdir(parents=True)
            (input_dir / "event.json").write_text('{"value": 1}', encoding="utf-8")
            (files_dir / "000-document.pdf").write_bytes(b"pdf")

            archive = executor._build_tar_archive(input_dir)
            extracted = root_path / "extracted"
            executor._extract_tar_archive(archive, extracted)

            self.assertEqual(
                (extracted / "input" / "event.json").read_text(encoding="utf-8"),
                '{"value": 1}',
            )
            self.assertEqual(
                (extracted / "input" / "files" / "000-document.pdf").read_bytes(),
                b"pdf",
            )
