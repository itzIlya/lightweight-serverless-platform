import uuid

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

    class Meta:
        ordering = ["-queued_at"]

    def __str__(self) -> str:
        return str(self.request_id)


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
