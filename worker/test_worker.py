import io
from pathlib import Path
import tarfile
import tempfile
import sys
import unittest
from unittest.mock import Mock, patch

from requests.exceptions import ReadTimeout

sys.path.insert(0, str(Path(__file__).resolve().parent))

from backend_client import BackendReportError
from builder import BuildCancelled, BuildError, BuildResult
from executor import DockerExecutor, ExecutionError, ExecutionResult
from warm_pool import WarmContainerKey, WarmContainerPool
from worker import (
    WorkerActivity,
    acknowledge_processing_job,
    claim_job_for_execution,
    classify_invocation_failure,
    job_report_metadata,
    move_job_to_processing,
    move_next_job_to_processing,
    move_next_job_to_processing_for_capacity,
    parse_delivery_message,
    process_build_job,
    process_v2_build_job,
    process_v2_invocation_job,
    read_v2_stream_delivery,
    run_claimed_job,
    worker_processing_queue_name,
    heartbeat_loop,
    warm_pool_heartbeat_metadata,
)


class FakeExecResult:
    def __init__(self, exit_code=0, output=(b"", b"")):
        self.exit_code = exit_code
        self.output = output


class BuildWorkerTests(unittest.TestCase):
    def test_classifies_nonzero_exit_as_function_failure(self):
        result = ExecutionResult(
            status="failed",
            result={},
            stdout="",
            stderr="",
            exit_code=1,
            duration_ms=10,
            error_message="Container exited with a non-zero status.",
        )

        self.assertEqual(classify_invocation_failure(result), "function")

    def test_classifies_missing_exit_code_as_platform_failure(self):
        result = ExecutionResult(
            status="failed",
            result={},
            stdout="",
            stderr="",
            exit_code=None,
            duration_ms=10,
            error_message="docker daemon unavailable",
        )

        self.assertEqual(classify_invocation_failure(result), "platform")

    def test_v2_stream_delivery_reads_worker_consumer_group(self):
        redis_client = Mock()
        redis_client.xreadgroup.return_value = [
            (
                "worker:worker-a:v2:builds",
                [("1-0", {"job_id": "job-1", "dispatch_attempt": "2"})],
            )
        ]

        delivery = read_v2_stream_delivery(
            redis_client,
            "worker:worker-a:v2:builds",
            "worker-a",
        )

        self.assertEqual(delivery[0], "1-0")
        self.assertEqual(delivery[1]["dispatch_attempt"], "2")
        redis_client.xreadgroup.assert_called_once_with(
            "v2-workers",
            "worker-a",
            {"worker:worker-a:v2:builds": ">"},
            count=1,
            block=1,
        )

    def test_v2_build_uses_orchestrator_without_django_coordination(self):
        backend = Mock()
        backend.is_build_cancel_requested.return_value = False
        builder = Mock()
        builder.build.return_value = BuildResult(
            image_ref="localhost:5000/functions/example:v1-a1-abc-d1",
            build_log="built",
            duration_ms=10,
        )
        orchestrator = Mock()
        orchestrator.complete_job.return_value = {"completed": True}
        job = {
            "type": "function.build",
            "job_id": "job-1",
            "dispatch_attempt": 1,
            "build_request_id": "build-1",
            "image_ref": "localhost:5000/functions/example:v1-a1-abc-d1",
        }

        completed = process_v2_build_job(
            job,
            backend,
            builder,
            orchestrator,
            worker_name="worker-a",
        )

        self.assertTrue(completed)
        backend.acquire_build_lease.assert_not_called()
        backend.report_build.assert_not_called()
        orchestrator.complete_job.assert_called_once()
        completion = orchestrator.complete_job.call_args.args[1]
        self.assertEqual(completion["status"], "succeeded")
        self.assertEqual(completion["artifact_commit_id"], job["image_ref"])

    def test_v2_invocation_hands_staged_completion_to_orchestrator(self):
        backend = Mock()
        executor = Mock()
        executor.run.return_value = ExecutionResult(
            status="succeeded",
            result={"ok": True},
            stdout="done",
            stderr="",
            exit_code=0,
            duration_ms=5,
            error_message="",
            cold_start=True,
            output_manifest=[
                {
                    "original_path": "report.txt",
                    "size_bytes": 4,
                    "checksum_sha256": "abc123",
                }
            ],
        )
        orchestrator = Mock()
        orchestrator.complete_job.return_value = {"completed": True}
        job = {
            "type": "function.invoke",
            "job_id": "job-1",
            "dispatch_attempt": 1,
            "request_id": "invoke-1",
        }

        completed = process_v2_invocation_job(
            job,
            backend,
            executor,
            orchestrator,
            worker_name="worker-a",
        )

        self.assertTrue(completed)
        backend.report_invocation.assert_not_called()
        self.assertEqual(
            orchestrator.complete_job.call_args.args[1]["status"],
            "succeeded",
        )
        orchestrator.complete_job.assert_called_once()
        completion = orchestrator.complete_job.call_args.args[1]
        self.assertEqual(completion["completion_payload"]["result"], {"ok": True})
        self.assertEqual(
            completion["completion_payload"]["output_manifest"][0]["original_path"],
            "report.txt",
        )
        self.assertEqual(job["completion_id"], "job-1:1:invocation")

    def test_v2_staged_upload_failure_withholds_completion(self):
        backend = Mock()
        executor = Mock()
        executor.run.side_effect = BackendReportError("backend unavailable")
        orchestrator = Mock()
        job = {
            "type": "function.invoke",
            "job_id": "job-1",
            "dispatch_attempt": 1,
            "request_id": "invoke-1",
        }

        completed = process_v2_invocation_job(
            job,
            backend,
            executor,
            orchestrator,
            worker_name="worker-a",
        )

        self.assertFalse(completed)
        orchestrator.complete_job.assert_not_called()

    def test_heartbeat_updates_orchestrator_and_backend_projection(self):
        backend = Mock()
        operational_store = Mock()
        activity = WorkerActivity()
        activity.start("function.invoke")
        stop_event = Mock()
        stop_event.wait.side_effect = [False, True]

        heartbeat_loop(
            backend,
            worker_name="worker-a",
            interval_seconds=0,
            activity=activity,
            stop_event=stop_event,
            operational_store=operational_store,
            operational_payload={
                "hostname": "worker-a.local",
                "max_concurrency": 4,
            },
        )

        operational_store.record_heartbeat.assert_called_once_with(
            {
                "name": "worker-a",
                "hostname": "worker-a.local",
                "max_concurrency": 4,
                "status": "online",
                "active_jobs": 1,
                "active_builds": 0,
                "active_invocations": 1,
            }
        )
        backend.heartbeat_worker.assert_called_once_with(
            {
                "name": "worker-a",
                "status": "online",
                "active_jobs": 1,
                "active_builds": 0,
                "active_invocations": 1,
                "metadata": {},
            }
        )

    def test_heartbeat_includes_live_warm_inventory(self):
        backend = Mock()
        operational_store = Mock()
        stop_event = Mock()
        stop_event.wait.side_effect = [False, True]
        warm_inventory = {
            "enabled": True,
            "containers": [
                {
                    "function_version_id": "10",
                    "image_ref": "image:v1",
                    "handler": "handler.main",
                    "memory_mb": 128,
                    "output_tmpfs_size_bytes": 10 * 1024 * 1024,
                    "idle_count": 1,
                    "busy_count": 0,
                }
            ],
        }

        heartbeat_loop(
            backend,
            worker_name="worker-a",
            interval_seconds=0,
            stop_event=stop_event,
            operational_store=operational_store,
            operational_payload={"metadata": {"legacy_queue_name": "worker-a:jobs"}},
            warm_inventory_provider=lambda: warm_inventory,
        )

        self.assertEqual(
            operational_store.record_heartbeat.call_args.args[0]["metadata"],
            {
                "legacy_queue_name": "worker-a:jobs",
                "warm_pool": warm_inventory,
            },
        )
        self.assertEqual(
            backend.heartbeat_worker.call_args.args[0]["metadata"],
            {"warm_pool": warm_inventory},
        )

    def test_heartbeat_reports_draining_status(self):
        backend = Mock()
        operational_store = Mock()
        stop_event = Mock()
        stop_event.wait.side_effect = [False, True]

        heartbeat_loop(
            backend,
            worker_name="worker-a",
            interval_seconds=0,
            stop_event=stop_event,
            operational_store=operational_store,
            status_provider=lambda: "draining",
        )

        self.assertEqual(
            operational_store.record_heartbeat.call_args.args[0]["status"],
            "draining",
        )
        self.assertEqual(
            backend.heartbeat_worker.call_args.args[0]["status"],
            "draining",
        )

    def test_orchestrator_heartbeat_failure_does_not_skip_backend_projection(self):
        backend = Mock()
        operational_store = Mock()
        operational_store.record_heartbeat.side_effect = RuntimeError("redis down")
        stop_event = Mock()
        stop_event.wait.side_effect = [False, True]

        heartbeat_loop(
            backend,
            worker_name="worker-a",
            interval_seconds=0,
            stop_event=stop_event,
            operational_store=operational_store,
        )

        backend.heartbeat_worker.assert_called_once()

    def test_transient_backend_transport_error_does_not_stop_heartbeat_loop(self):
        backend = Mock()
        backend.heartbeat_worker.side_effect = [ConnectionResetError(), {}]
        stop_event = Mock()
        stop_event.wait.side_effect = [False, False, True]

        heartbeat_loop(
            backend,
            worker_name="worker-a",
            interval_seconds=0,
            stop_event=stop_event,
        )

        self.assertEqual(backend.heartbeat_worker.call_count, 2)

    def test_worker_processing_queue_name_replaces_jobs_suffix(self):
        self.assertEqual(
            worker_processing_queue_name("worker:worker-a:jobs"),
            "worker:worker-a:processing",
        )

    def test_worker_processing_queue_name_is_shared_for_split_queues(self):
        self.assertEqual(
            worker_processing_queue_name("worker:worker-a:invocations"),
            "worker:worker-a:processing",
        )
        self.assertEqual(
            worker_processing_queue_name("worker:worker-a:builds"),
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

    def test_move_next_job_to_processing_prefers_invocation_queue(self):
        redis_client = Mock()
        redis_client.execute_command.side_effect = ["invoke-1"]

        delivery, source_queue = move_next_job_to_processing(
            redis_client,
            "worker:worker-a:invocations",
            "worker:worker-a:builds",
            "worker:worker-a:processing",
        )

        self.assertEqual(delivery, "invoke-1")
        self.assertEqual(source_queue, "worker:worker-a:invocations")
        redis_client.execute_command.assert_called_once_with(
            "LMOVE",
            "worker:worker-a:invocations",
            "worker:worker-a:processing",
            "LEFT",
            "RIGHT",
        )

    def test_move_next_job_to_processing_uses_build_queue_when_invocations_empty(self):
        redis_client = Mock()
        redis_client.execute_command.side_effect = [None, "build-1"]

        delivery, source_queue = move_next_job_to_processing(
            redis_client,
            "worker:worker-a:invocations",
            "worker:worker-a:builds",
            "worker:worker-a:processing",
        )

        self.assertEqual(delivery, "build-1")
        self.assertEqual(source_queue, "worker:worker-a:builds")
        self.assertEqual(redis_client.execute_command.call_args_list[1].args[1], "worker:worker-a:builds")

    def test_worker_activity_reports_active_job_types_and_capacity(self):
        activity = WorkerActivity()
        self.assertTrue(
            activity.can_start_invocation(
                max_concurrency=2,
                max_invocation_concurrency=1,
            )
        )

        activity.start("function.invoke")
        self.assertEqual(
            activity.snapshot(),
            {
                "active_jobs": 1,
                "active_builds": 0,
                "active_invocations": 1,
            },
        )
        self.assertFalse(
            activity.can_start_invocation(
                max_concurrency=2,
                max_invocation_concurrency=1,
            )
        )
        self.assertTrue(
            activity.can_start_build(
                max_concurrency=2,
                max_build_concurrency=1,
            )
        )

        activity.start("function.build")
        self.assertEqual(
            activity.snapshot(),
            {
                "active_jobs": 2,
                "active_builds": 1,
                "active_invocations": 1,
            },
        )
        self.assertFalse(
            activity.can_start_build(
                max_concurrency=2,
                max_build_concurrency=1,
            )
        )
        activity.finish("function.invoke")
        activity.finish("function.build")
        self.assertEqual(
            activity.snapshot(),
            {
                "active_jobs": 0,
                "active_builds": 0,
                "active_invocations": 0,
            },
        )

    def test_capacity_aware_move_does_not_pop_without_capacity(self):
        redis_client = Mock()

        delivery, source_queue = move_next_job_to_processing_for_capacity(
            redis_client,
            "worker:worker-a:invocations",
            "worker:worker-a:builds",
            "worker:worker-a:processing",
            can_run_invocation=False,
            can_run_build=False,
        )

        self.assertIsNone(delivery)
        self.assertIsNone(source_queue)
        redis_client.execute_command.assert_not_called()

    def test_capacity_aware_move_prefers_invocation_when_capacity_exists(self):
        redis_client = Mock()
        redis_client.execute_command.return_value = "invoke-1"

        delivery, source_queue = move_next_job_to_processing_for_capacity(
            redis_client,
            "worker:worker-a:invocations",
            "worker:worker-a:builds",
            "worker:worker-a:processing",
            can_run_invocation=True,
            can_run_build=True,
        )

        self.assertEqual(delivery, "invoke-1")
        self.assertEqual(source_queue, "worker:worker-a:invocations")
        redis_client.execute_command.assert_called_once_with(
            "LMOVE",
            "worker:worker-a:invocations",
            "worker:worker-a:processing",
            "LEFT",
            "RIGHT",
        )

    def test_capacity_aware_move_checks_build_when_invocation_capacity_is_full(self):
        redis_client = Mock()
        redis_client.execute_command.return_value = None

        delivery, source_queue = move_next_job_to_processing_for_capacity(
            redis_client,
            "worker:worker-a:invocations",
            "worker:worker-a:builds",
            "worker:worker-a:processing",
            can_run_invocation=False,
            can_run_build=True,
        )

        self.assertIsNone(delivery)
        self.assertIsNone(source_queue)
        redis_client.execute_command.assert_called_once_with(
            "LMOVE",
            "worker:worker-a:builds",
            "worker:worker-a:processing",
            "LEFT",
            "RIGHT",
        )

    def test_run_claimed_job_acks_after_invocation_finishes(self):
        backend = Mock()
        redis_client = Mock()
        activity = WorkerActivity()
        activity.start("function.invoke")
        executor = Mock()
        executor.run.return_value = ExecutionResult(
            status="succeeded",
            result={"ok": True},
            stdout="hello",
            stderr="",
            exit_code=0,
            duration_ms=12,
            error_message="",
            cold_start=True,
        )

        run_claimed_job(
            job={
                "type": "function.invoke",
                "request_id": "invoke-1",
                "job_id": "job-1",
                "dispatch_attempt": 1,
                "assigned_worker": "worker-a",
            },
            backend=backend,
            redis_client=redis_client,
            processing_queue_name="worker:worker-a:processing",
            delivery_message='{"job_id":"job-1","dispatch_attempt":1}',
            source_queue_name="worker:worker-a:invocations",
            worker_name="worker-a",
            hostname="worker-a.local",
            max_build_concurrency=1,
            activity=activity,
            executor_factory=lambda backend_client: executor,
        )

        self.assertEqual(backend.report_invocation.call_count, 2)
        redis_client.lrem.assert_called_once_with(
            "worker:worker-a:processing",
            1,
            '{"job_id":"job-1","dispatch_attempt":1}',
        )
        self.assertEqual(
            activity.snapshot(),
            {
                "active_jobs": 0,
                "active_builds": 0,
                "active_invocations": 0,
            },
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

    def test_copy_directory_from_container_uses_docker_archive(self):
        executor = DockerExecutor(docker_client=Mock())
        container = Mock()

        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            destination_dir = root_path / "destination"
            export_dir = root_path / "export"
            export_dir.mkdir()
            (export_dir / "report.txt").write_text("report", encoding="utf-8")
            container.get_archive.return_value = (
                [executor._build_tar_archive(export_dir)],
                {},
            )

            executor._copy_directory_from_container(
                container,
                "/sandbox/export",
                destination_dir,
            )

            container.get_archive.assert_called_once_with("/sandbox/export")
            container.exec_run.assert_not_called()
            self.assertEqual(
                (destination_dir / "export" / "report.txt").read_text(encoding="utf-8"),
                "report",
            )

    def test_collect_declared_output_files_ignores_extra_files(self):
        executor = DockerExecutor(docker_client=Mock())

        with tempfile.TemporaryDirectory() as root:
            output_dir = Path(root) / "output"
            nested_dir = output_dir / "nested"
            nested_dir.mkdir(parents=True)
            (output_dir / "report.txt").write_text("report", encoding="utf-8")
            (output_dir / "result.json").write_text("{}", encoding="utf-8")
            (output_dir / "extra.txt").write_text("extra", encoding="utf-8")
            (nested_dir / "nested-report.txt").write_text("nested", encoding="utf-8")

            collected = executor._collect_declared_output_files(
                {
                    "declared_output_files": [
                        "report.txt",
                    ]
                },
                output_dir,
            )

            self.assertEqual(len(collected), 1)
            self.assertEqual(collected[0]["original_path"], "report.txt")
            self.assertEqual(collected[0]["path"], output_dir / "report.txt")

    def test_upload_output_files_sends_declared_files_to_backend(self):
        backend = Mock()
        executor = DockerExecutor(docker_client=Mock(), backend_client=backend)

        with tempfile.TemporaryDirectory() as root:
            output_dir = Path(root) / "output"
            output_dir.mkdir()
            report = output_dir / "report.txt"
            report.write_text("report", encoding="utf-8")

            executor._upload_output_files(
                {
                    "request_id": "request-1",
                    "declared_output_files": ["report.txt"],
                },
                [{"original_path": "report.txt", "path": report}],
            )

            backend.upload_invocation_output.assert_called_once_with(
                "request-1",
                original_path="report.txt",
                file_path=report,
                position=0,
                content_type="text/plain",
            )

    def test_v2_upload_stages_file_and_returns_checksum_manifest(self):
        backend = Mock()
        executor = DockerExecutor(docker_client=Mock(), backend_client=backend)

        with tempfile.TemporaryDirectory() as root:
            report = Path(root) / "report.txt"
            report.write_text("report", encoding="utf-8")

            manifest = executor._upload_output_files(
                {
                    "request_id": "request-1",
                    "job_id": "job-1",
                    "dispatch_attempt": 2,
                    "completion_id": "job-1:2:invocation",
                    "coordination_version": 2,
                },
                [{"original_path": "report.txt", "path": report}],
            )

            backend.upload_staged_invocation_output.assert_called_once()
            upload = backend.upload_staged_invocation_output.call_args
            self.assertEqual(upload.args[0], "request-1")
            self.assertEqual(upload.kwargs["completion_id"], "job-1:2:invocation")
            self.assertEqual(manifest[0]["original_path"], "report.txt")
            self.assertEqual(manifest[0]["size_bytes"], 6)
            self.assertEqual(len(manifest[0]["checksum_sha256"]), 64)
            backend.upload_invocation_output.assert_not_called()

    def test_direct_upload_environment_uses_scoped_token_and_raw_endpoint(self):
        backend = Mock()
        backend.token = "change-me"
        with patch.dict(
            "os.environ",
            {
                "WORKER_RUNNER_DIRECT_OUTPUT_UPLOAD_ENABLED": "true",
                "BACKEND_BASE_URL": "http://backend:8000",
            },
        ):
            executor = DockerExecutor(docker_client=Mock(), backend_client=backend)

        job = {
            "request_id": "request-1",
            "job_id": "job-1",
            "dispatch_attempt": 2,
            "completion_id": "job-1:2:invocation",
            "coordination_version": 2,
            "declared_output_files": ["report.txt"],
            "invocation_output_max_files": 1,
            "invocation_output_max_file_size_mb": 1,
            "invocation_output_max_total_size_mb": 1,
        }

        environment = executor._runner_environment(
            job,
            {"ok": True},
            [],
            direct_output_upload=True,
        )

        self.assertEqual(environment["FUNCTION_OUTPUT_DIRECT_UPLOAD_ENABLED"], "1")
        self.assertEqual(
            environment["FUNCTION_OUTPUT_UPLOAD_URL"],
            "http://backend:8000/api/internal/invocations/request-1/runner-staged-outputs/",
        )
        self.assertEqual(environment["FUNCTION_OUTPUT_UPLOAD_JOB_ID"], "job-1")
        self.assertEqual(environment["FUNCTION_OUTPUT_UPLOAD_DISPATCH_ATTEMPT"], "2")
        self.assertEqual(
            environment["FUNCTION_OUTPUT_UPLOAD_COMPLETION_ID"],
            "job-1:2:invocation",
        )
        self.assertIn(".", environment["FUNCTION_OUTPUT_UPLOAD_TOKEN"])

    def test_direct_upload_cold_path_skips_docker_output_export(self):
        backend = Mock()
        backend.token = "change-me"
        backend.list_invocation_inputs.return_value = []
        docker_client = Mock()
        volume = Mock()
        volume.name = "volume-1"
        container = Mock()
        container.wait.return_value = {"StatusCode": 0}
        container.logs.side_effect = [
            (
                b'__FUNCTION_RESULT__={"ok": true}\n'
                b'__FUNCTION_OUTPUT_MANIFEST__=[{"original_path": "report.txt", "size_bytes": 6, "checksum_sha256": ""}]\n'
                b'__FUNCTION_TIMING__={"runner_output_upload_ms": 12}\n'
            ),
            b"",
        ]
        docker_client.volumes.create.return_value = volume
        docker_client.containers.create.return_value = container

        with patch.dict(
            "os.environ",
            {
                "WORKER_RUNNER_DIRECT_OUTPUT_UPLOAD_ENABLED": "true",
                "BACKEND_BASE_URL": "http://backend:8000",
                "FUNCTION_CONTAINER_NETWORK": "serverless-platform_default",
            },
        ):
            executor = DockerExecutor(
                docker_client=docker_client,
                backend_client=backend,
                warm_enabled=False,
            )
        executor._copy_directory_into_container = Mock()
        executor._copy_directory_from_container = Mock()
        executor._remove_container = Mock()
        executor._remove_volume = Mock()

        result = executor.run(
            {
                "request_id": "request-1",
                "job_id": "job-1",
                "dispatch_attempt": 2,
                "completion_id": "job-1:2:invocation",
                "coordination_version": 2,
                "image_ref": "localhost:5000/functions/example:v1",
                "declared_output_files": ["report.txt"],
                "invocation_output_max_files": 1,
                "invocation_output_max_file_size_mb": 1,
                "invocation_output_max_total_size_mb": 1,
            }
        )

        self.assertEqual(result.status, "succeeded")
        self.assertEqual(result.result, {"ok": True})
        self.assertEqual(
            result.output_manifest,
            [
                {
                    "original_path": "report.txt",
                    "size_bytes": 6,
                    "checksum_sha256": "",
                }
            ],
        )
        self.assertEqual(result.timing_ms["docker_export_copy_ms"], 0)
        self.assertEqual(result.timing_ms["runner_output_upload_ms"], 12)
        executor._copy_directory_from_container.assert_not_called()
        backend.upload_staged_invocation_output.assert_not_called()
        create_kwargs = docker_client.containers.create.call_args.kwargs
        self.assertFalse(create_kwargs["network_disabled"])
        self.assertEqual(create_kwargs["network"], "serverless-platform_default")
        self.assertEqual(create_kwargs["command"], ["-c", "python /runner.py"])

    def test_resident_warm_container_publishes_control_port(self):
        docker_client = Mock()
        volume = Mock()
        volume.name = "warm-volume"
        container = Mock()
        container.attrs = {
            "NetworkSettings": {
                "Ports": {"8765/tcp": [{"HostPort": "49153"}]},
            },
        }
        docker_client.volumes.create.return_value = volume
        docker_client.containers.create.return_value = container

        with patch.dict(
            "os.environ",
            {
                "WORKER_WARM_RESIDENT_RUNNER_ENABLED": "true",
                "FUNCTION_CONTAINER_NETWORK": "serverless-platform_default",
            },
        ):
            executor = DockerExecutor(
                docker_client=docker_client,
                warm_enabled=True,
            )
        executor._wait_for_resident_warm_runner = Mock()

        key = WarmContainerKey(
            function_version_id="10",
            image_ref="image:v1",
            handler="handler.main",
            memory_mb=128,
            output_tmpfs_size_bytes=10 * 1024 * 1024,
        )
        record = executor._create_warm_container(
            key=key,
            image_ref="image:v1",
            memory_mb=128,
            output_tmpfs_size_bytes=10 * 1024 * 1024,
            request_id="request-1",
            direct_output_upload=False,
        )

        create_kwargs = docker_client.containers.create.call_args.kwargs
        self.assertEqual(create_kwargs["entrypoint"], ["python"])
        self.assertEqual(create_kwargs["command"], ["/runner.py", "--serve"])
        self.assertEqual(
            create_kwargs["ports"],
            {"8765/tcp": ("127.0.0.1", None)},
        )
        self.assertFalse(create_kwargs["network_disabled"])
        self.assertEqual(create_kwargs["network"], "serverless-platform_default")
        self.assertEqual(record.metadata["control_url"], "http://127.0.0.1:49153")
        executor._wait_for_resident_warm_runner.assert_called_once_with(
            "http://127.0.0.1:49153",
            timeout_seconds=5,
        )

    def test_resident_warm_runner_skips_docker_exec_runner(self):
        docker_client = Mock()
        volume = Mock()
        volume.name = "warm-volume"
        container = Mock()
        container.attrs = {
            "NetworkSettings": {
                "Ports": {"8765/tcp": [{"HostPort": "49153"}]},
            },
        }
        docker_client.volumes.create.return_value = volume
        docker_client.containers.create.return_value = container
        backend = Mock()
        backend.list_invocation_inputs.return_value = []

        with patch.dict(
            "os.environ",
            {"WORKER_WARM_RESIDENT_RUNNER_ENABLED": "true"},
        ):
            executor = DockerExecutor(
                docker_client=docker_client,
                backend_client=backend,
                warm_enabled=True,
            )
        executor._wait_for_resident_warm_runner = Mock()
        executor._prepare_resident_warm_runner = Mock()
        executor._invoke_resident_warm_runner = Mock(
            return_value=(
                0,
                (
                    '__FUNCTION_RESULT__={"ok": true}\n'
                    '__FUNCTION_TIMING__={"runner_resident_reused": 1}\n'
                ),
                "",
            )
        )
        executor._exec_runner_in_warm_container = Mock()
        executor._cleanup_warm_sandbox = Mock()
        executor._copy_directory_into_container = Mock()
        executor._copy_tmpfs_directory_from_container = Mock()

        result = executor.run(
            {
                "request_id": "request-1",
                "function_version_id": 10,
                "image_ref": "image:v1",
                "handler": "handler.main",
                "config": {"memory_mb": 128, "timeout_seconds": 5},
                "event": {"value": 1},
                "declared_output_files": [],
                "invocation_output_max_total_size_mb": 10,
            }
        )

        self.assertEqual(result.status, "succeeded")
        self.assertEqual(result.result, {"ok": True})
        self.assertEqual(result.timing_ms["runner_resident_reused"], 1)
        self.assertEqual(result.timing_ms["docker_export_copy_ms"], 0)
        executor._prepare_resident_warm_runner.assert_called_once()
        executor._invoke_resident_warm_runner.assert_called_once()
        executor._exec_runner_in_warm_container.assert_not_called()
        executor._cleanup_warm_sandbox.assert_not_called()
        executor._copy_tmpfs_directory_from_container.assert_not_called()

    def test_worker_output_validation_rejects_non_list_declaration(self):
        executor = DockerExecutor(docker_client=Mock())

        with tempfile.TemporaryDirectory() as root:
            output_dir = Path(root) / "output"
            output_dir.mkdir()

            with self.assertRaisesRegex(Exception, "must be a list"):
                executor._validate_declared_output_files(
                    {"declared_output_files": "report.txt"},
                    output_dir,
                )

    def test_worker_output_validation_rejects_unsafe_declared_name(self):
        executor = DockerExecutor(docker_client=Mock())

        with tempfile.TemporaryDirectory() as root:
            output_dir = Path(root) / "output"
            output_dir.mkdir()

            with self.assertRaisesRegex(Exception, "unsafe or reserved"):
                executor._validate_declared_output_files(
                    {"declared_output_files": ["../secret.txt"]},
                    output_dir,
                )

    def test_worker_output_validation_rejects_result_json_declaration(self):
        executor = DockerExecutor(docker_client=Mock())

        with tempfile.TemporaryDirectory() as root:
            output_dir = Path(root) / "output"
            output_dir.mkdir()

            with self.assertRaisesRegex(Exception, "unsafe or reserved"):
                executor._validate_declared_output_files(
                    {"declared_output_files": ["result.json"]},
                    output_dir,
                )

    def test_worker_output_validation_rejects_directory_output(self):
        executor = DockerExecutor(docker_client=Mock())

        with tempfile.TemporaryDirectory() as root:
            output_dir = Path(root) / "output"
            (output_dir / "report.txt").mkdir(parents=True)

            with self.assertRaisesRegex(Exception, "not a file"):
                executor._validate_declared_output_files(
                    {"declared_output_files": ["report.txt"]},
                    output_dir,
                )

    def test_worker_output_validation_enforces_file_count_limit(self):
        executor = DockerExecutor(docker_client=Mock())

        with tempfile.TemporaryDirectory() as root:
            output_dir = Path(root) / "output"
            output_dir.mkdir()
            (output_dir / "one.txt").write_text("1", encoding="utf-8")
            (output_dir / "two.txt").write_text("2", encoding="utf-8")

            with self.assertRaisesRegex(Exception, "limit is 1"):
                executor._validate_declared_output_files(
                    {
                        "declared_output_files": ["one.txt", "two.txt"],
                        "invocation_output_max_files": 1,
                    },
                    output_dir,
                )

    def test_worker_output_validation_enforces_per_file_size_limit(self):
        executor = DockerExecutor(docker_client=Mock())

        with tempfile.TemporaryDirectory() as root:
            output_dir = Path(root) / "output"
            output_dir.mkdir()
            (output_dir / "report.txt").write_bytes(b"123")

            with self.assertRaisesRegex(Exception, "per-file limit is 0"):
                executor._validate_declared_output_files(
                    {
                        "declared_output_files": ["report.txt"],
                        "invocation_output_max_file_size_mb": 0,
                    },
                    output_dir,
                )

    def test_worker_output_validation_enforces_total_size_limit(self):
        executor = DockerExecutor(docker_client=Mock())

        with tempfile.TemporaryDirectory() as root:
            output_dir = Path(root) / "output"
            output_dir.mkdir()
            (output_dir / "one.txt").write_bytes(b"1")
            (output_dir / "two.txt").write_bytes(b"2")

            with self.assertRaisesRegex(Exception, "total limit is 0"):
                executor._validate_declared_output_files(
                    {
                        "declared_output_files": ["one.txt", "two.txt"],
                        "invocation_output_max_files": 2,
                        "invocation_output_max_total_size_mb": 0,
                    },
                    output_dir,
                )

    def test_worker_output_validation_missing_declared_output_is_allowed(self):
        executor = DockerExecutor(docker_client=Mock())

        with tempfile.TemporaryDirectory() as root:
            output_dir = Path(root) / "output"
            output_dir.mkdir()

            files = executor._validate_declared_output_files(
                {"declared_output_files": ["report.txt"]},
                output_dir,
            )

            self.assertEqual(files, [])

    def test_effective_output_dir_uses_docker_archive_nested_output_dir(self):
        executor = DockerExecutor(docker_client=Mock())

        with tempfile.TemporaryDirectory() as root:
            output_dir = Path(root) / "output"
            nested_output_dir = output_dir / "output"
            nested_output_dir.mkdir(parents=True)

            self.assertEqual(
                executor._effective_output_dir(output_dir),
                nested_output_dir,
            )

    def test_effective_output_dir_uses_sandbox_output_archive_layout(self):
        executor = DockerExecutor(docker_client=Mock())

        with tempfile.TemporaryDirectory() as root:
            output_dir = Path(root) / "output"
            nested_output_dir = output_dir / "sandbox" / "output"
            nested_output_dir.mkdir(parents=True)

            self.assertEqual(
                executor._effective_output_dir(output_dir),
                nested_output_dir,
            )

    def test_copy_tmpfs_directory_from_container_streams_files_with_exec_tar(self):
        executor = DockerExecutor(docker_client=Mock())
        archive_buffer = io.BytesIO()
        with tarfile.open(fileobj=archive_buffer, mode="w") as archive:
            body = b"hello"
            info = tarfile.TarInfo("report.txt")
            info.size = len(body)
            archive.addfile(info, io.BytesIO(body))

        container = Mock()
        container.exec_run.return_value = FakeExecResult(
            exit_code=0,
            output=(archive_buffer.getvalue(), b""),
        )

        with tempfile.TemporaryDirectory() as root:
            output_dir = Path(root) / "output"
            executor._copy_tmpfs_directory_from_container(
                container,
                "/sandbox/output",
                output_dir,
            )

            self.assertEqual(
                (output_dir / "report.txt").read_text(encoding="utf-8"),
                "hello",
            )
            container.exec_run.assert_called_once()

    def test_worker_output_validation_skips_upload_when_invalid(self):
        executor = DockerExecutor(docker_client=Mock(), warm_enabled=False)
        executor._copy_directory_into_container = Mock()
        executor._copy_directory_from_container = Mock()
        executor._remove_container = Mock()
        executor._remove_volume = Mock()
        container = Mock()
        container.attrs = {"State": {"Running": False, "ExitCode": 0}}
        container.logs.return_value = b""
        volume = Mock()
        volume.name = "volume-1"
        executor.docker_client.volumes.create.return_value = volume
        executor.docker_client.containers.create.return_value = container
        executor.backend_client = Mock()
        executor.backend_client.list_invocation_inputs.return_value = []

        def copy_outputs(container, source_path, destination_dir):
            output_dir = destination_dir / "export" / "output"
            output_dir.mkdir(parents=True)
            (output_dir / "report.txt").write_bytes(b"too large")

        executor._copy_directory_from_container.side_effect = copy_outputs

        result = executor.run(
            {
                "request_id": "request-1",
                "image_ref": "localhost:5000/functions/example:v1",
                "declared_output_files": ["report.txt"],
                "invocation_output_max_file_size_mb": 0,
            }
        )

        self.assertIsInstance(result, ExecutionResult)
        self.assertEqual(result.status, "failed")
        self.assertIn("per-file limit", result.error_message)
        executor.backend_client.upload_invocation_output.assert_not_called()

    def test_executor_fails_invocation_when_output_export_fails(self):
        executor = DockerExecutor(docker_client=Mock(), warm_enabled=False)
        executor._copy_directory_into_container = Mock()
        executor._copy_directory_from_container = Mock()
        executor._remove_container = Mock()
        executor._remove_volume = Mock()
        container = Mock()
        container.attrs = {"State": {"Running": False, "ExitCode": 0}}
        container.logs.return_value = b""
        volume = Mock()
        volume.name = "volume-1"
        executor.docker_client.volumes.create.return_value = volume
        executor.docker_client.containers.create.return_value = container
        executor.backend_client = Mock()
        executor.backend_client.list_invocation_inputs.return_value = []

        def copy_export(container, source_path, destination_dir):
            export_dir = destination_dir / "export"
            export_dir.mkdir(parents=True)
            (export_dir / "output_copy_exit_code").write_text("1", encoding="utf-8")
            (export_dir / "output_copy_error.txt").write_text(
                "copy failed",
                encoding="utf-8",
            )

        executor._copy_directory_from_container.side_effect = copy_export

        result = executor.run(
            {
                "request_id": "request-1",
                "image_ref": "localhost:5000/functions/example:v1",
                "declared_output_files": ["report.txt"],
            }
        )

        self.assertEqual(result.status, "failed")
        self.assertIn("copy failed", result.error_message)
        executor.backend_client.upload_invocation_output.assert_not_called()

    def test_cold_executor_skips_output_export_when_no_outputs_declared(self):
        executor = DockerExecutor(
            docker_client=Mock(),
            backend_client=Mock(),
            warm_enabled=False,
        )
        executor.backend_client.list_invocation_inputs.return_value = []
        executor._copy_directory_into_container = Mock()
        executor._copy_directory_from_container = Mock()
        executor._remove_container = Mock()
        executor._remove_volume = Mock()
        container = Mock()
        container.wait.return_value = {"StatusCode": 0}
        container.logs.side_effect = [b'__FUNCTION_RESULT__={"ok": true}\n', b""]
        volume = Mock()
        volume.name = "volume-1"
        executor.docker_client.volumes.create.return_value = volume
        executor.docker_client.containers.create.return_value = container

        result = executor.run(
            {
                "request_id": "request-1",
                "image_ref": "localhost:5000/functions/example:v1",
                "declared_output_files": [],
                "invocation_output_max_total_size_mb": 10,
            }
        )

        self.assertEqual(result.status, "succeeded")
        self.assertEqual(result.result, {"ok": True})
        self.assertEqual(result.output_manifest, [])
        self.assertEqual(result.timing_ms["docker_export_copy_ms"], 0)
        self.assertEqual(result.timing_ms["output_validation_ms"], 0)
        self.assertEqual(result.timing_ms["output_upload_ms"], 0)
        executor._copy_directory_from_container.assert_not_called()
        create_kwargs = executor.docker_client.containers.create.call_args.kwargs
        self.assertEqual(create_kwargs["entrypoint"], ["sh"])
        self.assertEqual(create_kwargs["command"], ["-c", "python /runner.py"])

    def test_executor_mounts_output_as_size_limited_tmpfs(self):
        executor = DockerExecutor(
            docker_client=Mock(),
            backend_client=Mock(),
            warm_enabled=False,
        )
        executor.backend_client.list_invocation_inputs.return_value = []
        executor._copy_directory_into_container = Mock()
        executor._copy_directory_from_container = Mock()
        executor._remove_container = Mock()
        executor._remove_volume = Mock()
        container = Mock()
        container.attrs = {"State": {"Running": False, "ExitCode": 0}}
        container.logs.return_value = b""
        volume = Mock()
        volume.name = "volume-1"
        executor.docker_client.volumes.create.return_value = volume
        executor.docker_client.containers.create.return_value = container

        executor.run(
            {
                "request_id": "request-1",
                "image_ref": "localhost:5000/functions/example:v1",
                "declared_output_files": [],
                "invocation_output_max_total_size_mb": 10,
            }
        )

        create_kwargs = executor.docker_client.containers.create.call_args.kwargs
        self.assertEqual(
            create_kwargs["tmpfs"],
            {"/sandbox/output": "size=10485760"},
        )
        self.assertEqual(create_kwargs["entrypoint"], ["sh"])
        self.assertEqual(create_kwargs["command"][0], "-c")
        self.assertIn("python /runner.py", create_kwargs["command"][1])
        self.assertNotIn("/sandbox/export/output", create_kwargs["command"][1])
        self.assertNotIn("cp -a /sandbox/output/.", create_kwargs["command"][1])
        self.assertNotIn("sleep", create_kwargs["command"][1])

    def test_executor_keeps_output_export_when_outputs_are_declared(self):
        executor = DockerExecutor(
            docker_client=Mock(),
            backend_client=Mock(),
            warm_enabled=False,
        )
        executor.backend_client.list_invocation_inputs.return_value = []
        executor._copy_directory_into_container = Mock()
        executor._copy_directory_from_container = Mock()
        executor._remove_container = Mock()
        executor._remove_volume = Mock()
        container = Mock()
        container.wait.return_value = {"StatusCode": 0}
        container.logs.side_effect = [b'__FUNCTION_RESULT__={"ok": true}\n', b""]
        volume = Mock()
        volume.name = "volume-1"
        executor.docker_client.volumes.create.return_value = volume
        executor.docker_client.containers.create.return_value = container

        def copy_export(container, source_path, destination_dir):
            output_dir = destination_dir / "export" / "output"
            output_dir.mkdir(parents=True)
            (output_dir / "report.txt").write_text("report", encoding="utf-8")

        executor._copy_directory_from_container.side_effect = copy_export

        executor.run(
            {
                "request_id": "request-1",
                "image_ref": "localhost:5000/functions/example:v1",
                "declared_output_files": ["report.txt"],
                "invocation_output_max_files": 1,
                "invocation_output_max_file_size_mb": 1,
                "invocation_output_max_total_size_mb": 10,
            }
        )

        create_kwargs = executor.docker_client.containers.create.call_args.kwargs
        self.assertIn("/sandbox/export/output", create_kwargs["command"][1])
        self.assertIn("cp -a /sandbox/output/.", create_kwargs["command"][1])
        executor._copy_directory_from_container.assert_called_once()

    def test_output_tmpfs_size_has_one_megabyte_floor(self):
        executor = DockerExecutor(docker_client=Mock())

        self.assertEqual(
            executor._output_tmpfs_size_bytes(
                {"invocation_output_max_total_size_mb": 0}
            ),
            1024 * 1024,
        )

    def test_warm_pool_reuses_same_function_version_container(self):
        docker_client = Mock()
        volume = Mock()
        volume.name = "warm-volume"
        container = Mock()
        container.exec_run.return_value = FakeExecResult()
        docker_client.volumes.create.return_value = volume
        docker_client.containers.create.return_value = container
        executor = DockerExecutor(
            docker_client=docker_client,
            warm_enabled=True,
        )
        executor._copy_directory_into_container = Mock()
        executor._copy_directory_from_container = Mock()
        executor._copy_tmpfs_directory_from_container = Mock()
        executor._exec_runner_in_warm_container = Mock(
            return_value=(0, '__FUNCTION_RESULT__={"ok": true}\n', "")
        )

        job = {
            "request_id": "request-1",
            "function_version_id": 10,
            "image_ref": "localhost:5000/functions/example:v1",
            "handler": "handler.main",
            "config": {"memory_mb": 128, "timeout_seconds": 5},
            "event": {"value": 1},
            "declared_output_files": [],
        }

        first = executor.run(job)
        second = executor.run({**job, "request_id": "request-2"})

        self.assertTrue(first.cold_start)
        self.assertFalse(second.cold_start)
        self.assertEqual(first.status, "succeeded")
        self.assertEqual(second.status, "succeeded")
        self.assertEqual(docker_client.containers.create.call_count, 1)
        executor._copy_tmpfs_directory_from_container.assert_not_called()
        container.remove.assert_not_called()

    def test_warm_pool_inventory_groups_idle_and_busy_by_key(self):
        key = WarmContainerKey(
            function_version_id="10",
            image_ref="image:v1",
            handler="handler.main",
            memory_mb=128,
            output_tmpfs_size_bytes=10 * 1024 * 1024,
        )
        pool = WarmContainerPool(
            max_containers=2,
            max_per_key=2,
            idle_ttl_seconds=60,
            max_age_seconds=0,
            max_uses=0,
        )
        idle = pool.add_busy(key=key, container=Mock(), volume=Mock())
        pool.add_busy(key=key, container=Mock(), volume=Mock())
        pool.release(idle, reusable=True)

        self.assertEqual(
            pool.inventory(),
            [
                {
                    "function_version_id": "10",
                    "image_ref": "image:v1",
                    "handler": "handler.main",
                    "memory_mb": 128,
                    "output_tmpfs_size_bytes": 10 * 1024 * 1024,
                    "idle_count": 1,
                    "busy_count": 1,
                    "use_count": 1,
                    "hit_count": 0,
                }
            ],
        )

    def test_warm_pool_heartbeat_metadata_reports_disabled_executor(self):
        executor = DockerExecutor(docker_client=Mock(), warm_enabled=False)

        self.assertEqual(
            warm_pool_heartbeat_metadata(executor),
            {
                "enabled": False,
                "containers": [],
            },
        )

    def test_warm_pool_does_not_reuse_different_function_version(self):
        docker_client = Mock()
        volumes = [Mock(), Mock()]
        containers = [Mock(), Mock()]
        for index, volume in enumerate(volumes):
            volume.name = f"warm-volume-{index}"
        for container in containers:
            container.exec_run.return_value = FakeExecResult()
        docker_client.volumes.create.side_effect = volumes
        docker_client.containers.create.side_effect = containers
        executor = DockerExecutor(
            docker_client=docker_client,
            warm_enabled=True,
        )
        executor._copy_directory_into_container = Mock()
        executor._copy_directory_from_container = Mock()
        executor._exec_runner_in_warm_container = Mock(
            return_value=(0, '__FUNCTION_RESULT__={"ok": true}\n', "")
        )

        base_job = {
            "request_id": "request-1",
            "image_ref": "localhost:5000/functions/example:v1",
            "handler": "handler.main",
            "config": {"memory_mb": 128, "timeout_seconds": 5},
            "event": {},
            "declared_output_files": [],
        }

        first = executor.run({**base_job, "function_version_id": 10})
        second = executor.run(
            {**base_job, "request_id": "request-2", "function_version_id": 11}
        )

        self.assertTrue(first.cold_start)
        self.assertTrue(second.cold_start)
        self.assertEqual(docker_client.containers.create.call_count, 2)

    def test_warm_container_failed_invocation_is_destroyed(self):
        docker_client = Mock()
        volumes = [Mock(), Mock()]
        containers = [Mock(), Mock()]
        for index, volume in enumerate(volumes):
            volume.name = f"warm-volume-{index}"
        for container in containers:
            container.exec_run.return_value = FakeExecResult()
        docker_client.volumes.create.side_effect = volumes
        docker_client.containers.create.side_effect = containers
        executor = DockerExecutor(
            docker_client=docker_client,
            warm_enabled=True,
        )
        executor._copy_directory_into_container = Mock()
        executor._copy_directory_from_container = Mock()
        executor._exec_runner_in_warm_container = Mock(
            side_effect=[
                (1, '__FUNCTION_RESULT__={"ok": false}\n', ""),
                (0, '__FUNCTION_RESULT__={"ok": true}\n', ""),
            ]
        )

        job = {
            "request_id": "request-1",
            "function_version_id": 10,
            "image_ref": "localhost:5000/functions/example:v1",
            "handler": "handler.main",
            "config": {"memory_mb": 128, "timeout_seconds": 5},
            "event": {},
            "declared_output_files": [],
        }

        first = executor.run(job)
        second = executor.run({**job, "request_id": "request-2"})

        self.assertEqual(first.status, "failed")
        self.assertTrue(second.cold_start)
        containers[0].remove.assert_called_once_with(force=True)
        self.assertEqual(docker_client.containers.create.call_count, 2)

    def test_warm_pool_evicts_idle_container_after_ttl(self):
        now = [100.0]
        pool = WarmContainerPool(
            max_containers=2,
            max_per_key=1,
            idle_ttl_seconds=10,
            max_age_seconds=100,
            max_uses=100,
            now=lambda: now[0],
        )
        key = WarmContainerKey(
            function_version_id="10",
            image_ref="image",
            handler="handler.main",
            memory_mb=128,
            output_tmpfs_size_bytes=1024 * 1024,
        )
        container = Mock()
        volume = Mock()
        record = pool.add_busy(key=key, container=container, volume=volume)

        pool.release(record, reusable=True)
        now[0] = 111.0
        self.assertIsNone(pool.acquire(key))

        container.remove.assert_called_once_with(force=True)
        volume.remove.assert_called_once_with(force=True)

    def test_warm_pool_evicts_least_recently_used_when_full(self):
        now = [100.0]
        pool = WarmContainerPool(
            max_containers=1,
            max_per_key=1,
            idle_ttl_seconds=100,
            max_age_seconds=100,
            max_uses=100,
            now=lambda: now[0],
        )
        first_key = WarmContainerKey("1", "image-1", "handler.main", 128, 1024 * 1024)
        second_key = WarmContainerKey("2", "image-2", "handler.main", 128, 1024 * 1024)
        first_container = Mock()
        second_container = Mock()
        first = pool.add_busy(key=first_key, container=first_container)
        pool.release(first, reusable=True)
        now[0] = 101.0
        second = pool.add_busy(key=second_key, container=second_container)
        pool.release(second, reusable=True)

        self.assertIsNone(pool.acquire(first_key))
        self.assertIsNotNone(pool.acquire(second_key))
        first_container.remove.assert_called_once_with(force=True)
        second_container.remove.assert_not_called()

    def test_warm_pool_preserves_hot_container_under_container_pressure(self):
        now = [100.0]
        pool = WarmContainerPool(
            max_containers=2,
            max_per_key=2,
            idle_ttl_seconds=100,
            max_age_seconds=100,
            max_uses=100,
            now=lambda: now[0],
        )
        hot_key = WarmContainerKey("hot", "image-hot", "handler.main", 128, 1024 * 1024)
        cold_key = WarmContainerKey("cold", "image-cold", "handler.main", 128, 1024 * 1024)
        new_key = WarmContainerKey("new", "image-new", "handler.main", 128, 1024 * 1024)
        hot_container = Mock()
        cold_container = Mock()
        new_container = Mock()

        hot = pool.add_busy(key=hot_key, container=hot_container)
        pool.release(hot, reusable=True)
        now[0] = 101.0
        hot_reuse = pool.acquire(hot_key)
        pool.release(hot_reuse, reusable=True)
        now[0] = 102.0
        cold = pool.add_busy(key=cold_key, container=cold_container)
        pool.release(cold, reusable=True)
        now[0] = 103.0
        new = pool.add_busy(key=new_key, container=new_container)
        pool.release(new, reusable=True)

        self.assertIsNotNone(pool.acquire(hot_key))
        self.assertIsNone(pool.acquire(cold_key))
        self.assertIsNotNone(pool.acquire(new_key))
        self.assertEqual(cold.eviction_reason, "pool_container_pressure")
        self.assertEqual(pool.eviction_log[-1]["reason"], "pool_container_pressure")
        hot_container.remove.assert_not_called()
        cold_container.remove.assert_called_once_with(force=True)

    def test_warm_pool_memory_pressure_evicts_large_cold_container_first(self):
        now = [100.0]
        pool = WarmContainerPool(
            max_containers=4,
            max_per_key=4,
            idle_ttl_seconds=100,
            max_age_seconds=100,
            max_uses=100,
            max_memory_mb=300,
            now=lambda: now[0],
        )
        hot_small_key = WarmContainerKey(
            "hot-small",
            "image-hot-small",
            "handler.main",
            128,
            1024 * 1024,
        )
        cold_large_key = WarmContainerKey(
            "cold-large",
            "image-cold-large",
            "handler.main",
            256,
            1024 * 1024,
        )
        new_small_key = WarmContainerKey(
            "new-small",
            "image-new-small",
            "handler.main",
            128,
            1024 * 1024,
        )
        hot_container = Mock()
        cold_container = Mock()

        hot = pool.add_busy(key=hot_small_key, container=hot_container)
        pool.release(hot, reusable=True)
        now[0] = 101.0
        hot_reuse = pool.acquire(hot_small_key)
        pool.release(hot_reuse, reusable=True)
        now[0] = 102.0
        cold = pool.add_busy(key=cold_large_key, container=cold_container)
        pool.release(cold, reusable=True)
        now[0] = 103.0
        new = pool.add_busy(key=new_small_key, container=Mock())
        pool.release(new, reusable=True)

        self.assertIsNotNone(pool.acquire(hot_small_key))
        self.assertIsNone(pool.acquire(cold_large_key))
        self.assertIsNotNone(pool.acquire(new_small_key))
        self.assertEqual(cold.eviction_reason, "pool_memory_pressure")
        cold_container.remove.assert_called_once_with(force=True)
        hot_container.remove.assert_not_called()

    def test_warm_pool_per_function_limit_evicts_low_value_same_key_container(self):
        now = [100.0]
        pool = WarmContainerPool(
            max_containers=4,
            max_per_key=1,
            idle_ttl_seconds=100,
            max_age_seconds=100,
            max_uses=100,
            now=lambda: now[0],
        )
        key = WarmContainerKey("same", "image", "handler.main", 128, 1024 * 1024)
        hot_container = Mock()
        cold_container = Mock()

        hot = pool.add_busy(key=key, container=hot_container)
        pool.release(hot, reusable=True)
        now[0] = 101.0
        hot_reuse = pool.acquire(key)
        pool.release(hot_reuse, reusable=True)
        now[0] = 102.0
        cold = pool.add_busy(key=key, container=cold_container)
        pool.release(cold, reusable=True)

        self.assertIsNotNone(pool.acquire(key))
        self.assertEqual(cold.eviction_reason, "function_over_limit")
        cold_container.remove.assert_called_once_with(force=True)
        hot_container.remove.assert_not_called()

    def test_warm_pool_records_retirement_eviction_reasons(self):
        now = [100.0]
        pool = WarmContainerPool(
            max_containers=2,
            max_per_key=1,
            idle_ttl_seconds=10,
            max_age_seconds=100,
            max_uses=100,
            now=lambda: now[0],
        )
        key = WarmContainerKey("10", "image", "handler.main", 128, 1024 * 1024)
        container = Mock()
        record = pool.add_busy(key=key, container=container)

        pool.release(record, reusable=True)
        now[0] = 111.0
        pool.evict_expired()

        self.assertEqual(record.eviction_reason, "idle_ttl")
        self.assertEqual(pool.eviction_log[-1]["reason"], "idle_ttl")

    def test_wait_for_exit_returns_container_exit_code(self):
        executor = DockerExecutor(docker_client=Mock())
        container = Mock()
        container.wait.return_value = {"StatusCode": 7}

        self.assertEqual(executor._wait_for_exit(container, 1), 7)
        container.wait.assert_called_once_with(timeout=1)
        container.kill.assert_not_called()

    def test_read_runner_timings_accepts_only_internal_integer_fields(self):
        executor = DockerExecutor(docker_client=Mock())
        stdout = "\n".join(
            [
                "user output",
                '__FUNCTION_TIMING__={"runner_handler_import_ms": 12, '
                '"runner_handler_execution_ms": 1000, "other": 99, '
                '"runner_invalid": "no"}',
            ]
        )

        self.assertEqual(
            executor._read_runner_timings(stdout),
            {
                "runner_handler_import_ms": 12,
                "runner_handler_execution_ms": 1000,
            },
        )

    def test_read_runner_timings_ignores_malformed_marker(self):
        executor = DockerExecutor(docker_client=Mock())

        self.assertEqual(
            executor._read_runner_timings("__FUNCTION_TIMING__=not-json"),
            {},
        )

    def test_wait_for_exit_kills_container_after_timeout(self):
        executor = DockerExecutor(docker_client=Mock())
        container = Mock()
        container.wait.side_effect = ReadTimeout("timed out")

        with self.assertRaisesRegex(
            ExecutionError,
            "Function execution timed out after 3 seconds.",
        ):
            executor._wait_for_exit(container, 3)

        container.wait.assert_called_once_with(timeout=3)
        container.kill.assert_called_once_with()
