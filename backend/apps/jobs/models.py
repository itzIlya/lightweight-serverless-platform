import uuid

from django.db import models
from django.utils import timezone


class JobType(models.TextChoices):
    BUILD = "build", "Build"
    INVOCATION = "invocation", "Invocation"


class JobStatus(models.TextChoices):
    QUEUED = "queued", "Queued"
    DISPATCHED = "dispatched", "Dispatched"
    RUNNING = "running", "Running"
    SUCCEEDED = "succeeded", "Succeeded"
    FAILED = "failed", "Failed"
    CANCELLED = "cancelled", "Cancelled"
    DEAD_LETTERED = "dead_lettered", "Dead-lettered"


class Job(models.Model):
    job_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    type = models.CharField(max_length=20, choices=JobType.choices)
    status = models.CharField(
        max_length=20,
        choices=JobStatus.choices,
        default=JobStatus.QUEUED,
    )
    queue_name = models.CharField(max_length=120)
    payload = models.JSONField(default=dict, blank=True)
    build_attempt = models.ForeignKey(
        "functions.BuildAttempt",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="jobs",
    )
    invocation = models.ForeignKey(
        "invocations.Invocation",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="jobs",
    )
    available_at = models.DateTimeField(default=timezone.now)
    locked_until = models.DateTimeField(null=True, blank=True)
    dispatch_attempts = models.PositiveIntegerField(default=0)
    recovery_count = models.PositiveIntegerField(default=0)
    max_recovery_attempts = models.PositiveIntegerField(default=3)
    last_recovered_at = models.DateTimeField(null=True, blank=True)
    dead_lettered_at = models.DateTimeField(null=True, blank=True)
    dead_letter_reason = models.TextField(blank=True)
    last_error = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]
        indexes = [
            models.Index(fields=["status", "available_at"]),
            models.Index(fields=["type", "status"]),
        ]

    def __str__(self) -> str:
        return f"{self.type}:{self.job_id}"
