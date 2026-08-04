import io
import shutil
import tempfile
import zipfile
from datetime import timedelta
from pathlib import Path

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.utils import timezone

from apps.functions.models import Function, FunctionVersion
from apps.jobs.models import Job, JobStatus, JobType

from .management.commands.cleanup_expired_invocations import (
    cleanup_expired_invocations,
)
from .models import (
    Invocation,
    InvocationInputFile,
    InvocationLogArtifact,
    InvocationOutputFile,
    InvocationStatus,
)


def function_bundle() -> SimpleUploadedFile:
    data = io.BytesIO()
    with zipfile.ZipFile(data, "w") as archive:
        archive.writestr(
            "handler.py",
            "def main(event, context):\n    return {'ok': True}\n",
        )
        archive.writestr("requirements.txt", "")
    return SimpleUploadedFile(
        "function.zip",
        data.getvalue(),
        content_type="application/zip",
    )


class InvocationRetentionTests(TestCase):
    def setUp(self):
        self.media_root = tempfile.mkdtemp(prefix="invocation-retention-media-")
        self.override = override_settings(MEDIA_ROOT=self.media_root)
        self.override.enable()
        user = get_user_model().objects.create_user(username="retention-owner")
        function = Function.objects.create(
            owner=user,
            name="Retention Function",
            slug="retention-function",
        )
        self.version = FunctionVersion.objects.create(
            function=function,
            version="v1",
            source_bundle=function_bundle(),
            image_ref="localhost:5000/functions/retention:v1",
            build_status="built",
            declared_output_files=["report.txt"],
        )

    def tearDown(self):
        self.override.disable()
        shutil.rmtree(self.media_root, ignore_errors=True)

    def create_invocation(self, *, status, age_days: int) -> Invocation:
        invocation = Invocation.objects.create(
            function_version=self.version,
            event={"age_days": age_days},
            result={"ok": True},
            status=status,
            stdout="stdout",
            stderr="stderr",
        )
        queued_at = timezone.now() - timedelta(days=age_days)
        Invocation.objects.filter(pk=invocation.pk).update(queued_at=queued_at)
        invocation.refresh_from_db()
        return invocation

    def attach_files(self, invocation: Invocation):
        input_file = InvocationInputFile.objects.create(
            invocation=invocation,
            position=0,
            field_name="files",
            original_name="input.txt",
            content_type="text/plain",
            size_bytes=5,
        )
        input_file.file.save("input.txt", ContentFile(b"input"), save=True)

        output_file = InvocationOutputFile.objects.create(
            invocation=invocation,
            original_path="report.txt",
            safe_name="report.txt",
            content_type="text/plain",
            size_bytes=6,
            position=0,
        )
        output_file.file.save("report.txt", ContentFile(b"output"), save=True)

        log_file = InvocationLogArtifact.objects.create(
            invocation=invocation,
            stream="stdout",
            safe_name="stdout.txt",
            content_type="text/plain",
            size_bytes=6,
            preview="stdout",
        )
        log_file.file.save("stdout.txt", ContentFile(b"stdout"), save=True)
        return (
            Path(input_file.file.path),
            Path(output_file.file.path),
            Path(log_file.file.path),
        )

    def test_cleanup_deletes_expired_terminal_invocation_and_artifacts(self):
        invocation = self.create_invocation(
            status=InvocationStatus.SUCCEEDED,
            age_days=8,
        )
        input_path, output_path, log_path = self.attach_files(invocation)
        source_path = Path(self.version.source_bundle.path)
        Job.objects.create(
            type=JobType.INVOCATION,
            status=JobStatus.SUCCEEDED,
            queue_name="worker:worker-a:invocations",
            invocation=invocation,
        )

        deleted = cleanup_expired_invocations(retention_days=7)

        self.assertEqual(deleted, 1)
        self.assertFalse(Invocation.objects.filter(pk=invocation.pk).exists())
        self.assertFalse(Job.objects.filter(invocation_id=invocation.pk).exists())
        self.assertFalse(input_path.exists())
        self.assertFalse(output_path.exists())
        self.assertFalse(log_path.exists())
        self.assertTrue(source_path.exists())

    def test_cleanup_keeps_recent_terminal_invocation(self):
        invocation = self.create_invocation(
            status=InvocationStatus.FAILED,
            age_days=6,
        )

        deleted = cleanup_expired_invocations(retention_days=7)

        self.assertEqual(deleted, 0)
        self.assertTrue(Invocation.objects.filter(pk=invocation.pk).exists())

    def test_cleanup_keeps_old_running_invocation(self):
        invocation = self.create_invocation(
            status=InvocationStatus.RUNNING,
            age_days=30,
        )

        deleted = cleanup_expired_invocations(retention_days=7)

        self.assertEqual(deleted, 0)
        self.assertTrue(Invocation.objects.filter(pk=invocation.pk).exists())

    def test_cleanup_dry_run_counts_without_deleting(self):
        invocation = self.create_invocation(
            status=InvocationStatus.CANCELLED,
            age_days=8,
        )

        deleted = cleanup_expired_invocations(retention_days=7, dry_run=True)

        self.assertEqual(deleted, 1)
        self.assertTrue(Invocation.objects.filter(pk=invocation.pk).exists())
