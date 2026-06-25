import uuid
import hashlib
import secrets

from django.db import models
from django.utils.text import get_valid_filename

from apps.functions.models import FunctionVersion


class InvocationStatus(models.TextChoices):
    QUEUED = "queued", "Queued"
    RUNNING = "running", "Running"
    SUCCEEDED = "succeeded", "Succeeded"
    FAILED = "failed", "Failed"
    TIMEOUT = "timeout", "Timeout"
    CANCELLED = "cancelled", "Cancelled"


class Invocation(models.Model):
    request_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    function_version = models.ForeignKey(
        FunctionVersion,
        on_delete=models.CASCADE,
        related_name="invocations",
    )
    status = models.CharField(
        max_length=20,
        choices=InvocationStatus.choices,
        default=InvocationStatus.QUEUED,
    )
    event = models.JSONField(default=dict, blank=True)
    result = models.JSONField(default=dict, blank=True)
    stdout = models.TextField(blank=True)
    stderr = models.TextField(blank=True)
    exit_code = models.IntegerField(null=True, blank=True)
    cold_start = models.BooleanField(default=False)
    retry_count = models.PositiveIntegerField(default=0)
    error_message = models.TextField(blank=True)
    queued_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    duration_ms = models.PositiveIntegerField(null=True, blank=True)
    read_token_hash = models.CharField(max_length=64, blank=True, db_index=True)
    read_token_prefix = models.CharField(max_length=16, blank=True, db_index=True)

    class Meta:
        ordering = ["-queued_at"]

    def __str__(self) -> str:
        return str(self.request_id)

    def issue_read_token(self) -> str:
        raw_token = f"inv_{secrets.token_urlsafe(32)}"
        self.read_token_hash = hash_invocation_read_token(raw_token)
        self.read_token_prefix = raw_token[:16]
        self.save(update_fields=["read_token_hash", "read_token_prefix"])
        return raw_token


def hash_invocation_read_token(raw_token: str) -> str:
    return hashlib.sha256(raw_token.encode("utf-8")).hexdigest()


def invocation_input_upload_to(instance, filename: str) -> str:
    safe_name = get_valid_filename(filename) or "input"
    return (
        f"invocation_inputs/{instance.invocation.request_id}/"
        f"{instance.position:03d}-{safe_name}"
    )


class InvocationInputFile(models.Model):
    invocation = models.ForeignKey(
        Invocation,
        on_delete=models.CASCADE,
        related_name="input_files",
    )
    position = models.PositiveSmallIntegerField(default=0)
    field_name = models.CharField(max_length=120, default="files")
    original_name = models.CharField(max_length=255)
    content_type = models.CharField(max_length=255, blank=True)
    size_bytes = models.PositiveIntegerField(default=0)
    file = models.FileField(upload_to=invocation_input_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["position", "created_at"]

    def __str__(self) -> str:
        return f"{self.invocation.request_id}:{self.original_name}"


def invocation_output_upload_to(instance, filename: str) -> str:
    safe_name = get_valid_filename(filename) or "output"
    return (
        f"invocation_outputs/{instance.invocation.request_id}/"
        f"{instance.position:03d}-{safe_name}"
    )


class InvocationOutputFile(models.Model):
    invocation = models.ForeignKey(
        Invocation,
        on_delete=models.CASCADE,
        related_name="output_files",
    )
    file = models.FileField(upload_to=invocation_output_upload_to)
    original_path = models.CharField(max_length=500)
    safe_name = models.CharField(max_length=255)
    content_type = models.CharField(max_length=255, blank=True)
    size_bytes = models.PositiveIntegerField(default=0)
    position = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["position", "created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["invocation", "original_path"],
                name="unique_invocation_output_path",
            )
        ]

    def __str__(self) -> str:
        return f"{self.invocation.request_id}:{self.original_path}"
