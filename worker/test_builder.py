from pathlib import Path
import tempfile
import unittest
import zipfile

from builder import (
    RUNNER_SOURCE,
    BuildCancelled,
    BuildError,
    base_image_for_runtime,
    check_cancelled,
    extract_source_bundle,
)


class BuilderTests(unittest.TestCase):
    def test_runner_emits_internal_phase_timings(self):
        self.assertIn("runner_handler_import_ms", RUNNER_SOURCE)
        self.assertIn("runner_handler_execution_ms", RUNNER_SOURCE)
        self.assertIn("runner_module_imports_ms", RUNNER_SOURCE)
        self.assertIn("runner_result_write_ms", RUNNER_SOURCE)
        self.assertIn("__FUNCTION_TIMING__=", RUNNER_SOURCE)

    def test_runtime_selects_python_slim_image(self):
        self.assertEqual(
            base_image_for_runtime("python3.13"),
            "python:3.13-slim",
        )

    def test_unsupported_runtime_is_rejected(self):
        with self.assertRaises(BuildError):
            base_image_for_runtime("node22")

    def test_archive_traversal_is_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            archive_path = Path(root) / "unsafe.zip"
            output_path = Path(root) / "output"
            output_path.mkdir()
            with zipfile.ZipFile(archive_path, "w") as archive:
                archive.writestr("../handler.py", "pass")

            with self.assertRaises(BuildError):
                extract_source_bundle(archive_path, output_path)

    def test_cancellation_callback_stops_build(self):
        with self.assertRaises(BuildCancelled):
            check_cancelled(lambda: True)
