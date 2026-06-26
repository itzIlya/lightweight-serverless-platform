from pathlib import Path
import tempfile
import sys
import unittest
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parent))

from backend_client import BackendReportError
from builder import BuildCancelled, BuildError, BuildResult
from executor import DockerExecutor, ExecutionResult
from worker import (
    WorkerActivity,
    acknowledge_processing_job,
    claim_job_for_execution,
    job_report_metadata,
    move_job_to_processing,
    move_next_job_to_processing,
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

    def test_worker_activity_reports_active_builds(self):
        activity = WorkerActivity()
        activity.start("function.build")
        self.assertEqual(
            activity.snapshot(),
            {
                "active_jobs": 1,
                "active_builds": 1,
            },
        )
        activity.finish("function.build")
        self.assertEqual(
            activity.snapshot(),
            {
                "active_jobs": 0,
                "active_builds": 0,
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

    def test_worker_output_validation_skips_upload_when_invalid(self):
        executor = DockerExecutor(docker_client=Mock())
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
        executor = DockerExecutor(docker_client=Mock())
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

    def test_executor_mounts_output_as_size_limited_tmpfs(self):
        executor = DockerExecutor(docker_client=Mock(), backend_client=Mock())
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
        self.assertIn("/sandbox/export/output", create_kwargs["command"][1])
        self.assertIn("cp -a /sandbox/output/.", create_kwargs["command"][1])
        self.assertNotIn("sleep", create_kwargs["command"][1])

    def test_output_tmpfs_size_has_one_megabyte_floor(self):
        executor = DockerExecutor(docker_client=Mock())

        self.assertEqual(
            executor._output_tmpfs_size_bytes(
                {"invocation_output_max_total_size_mb": 0}
            ),
            1024 * 1024,
        )

    def test_wait_for_exit_returns_container_exit_code(self):
        executor = DockerExecutor(docker_client=Mock())
        container = Mock()
        container.attrs = {"State": {"Running": False, "ExitCode": 7}}

        self.assertEqual(executor._wait_for_exit(container, 1), 7)
        container.kill.assert_not_called()
