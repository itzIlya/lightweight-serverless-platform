import uuid
import hashlib
import secrets

from django.conf import settings
from django.db import models
from django.utils import timezone


class InvokeAccess(models.TextChoices):
    PRIVATE = "private", "Private"
    TOKEN = "token", "Token"
    PUBLIC = "public", "Public"


class Function(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="functions",
    )
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    invoke_access = models.CharField(
        max_length=20,
        choices=InvokeAccess.choices,
        default=InvokeAccess.PRIVATE,
    )
    active_version = models.ForeignKey(
        "functions.FunctionVersion",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.slug


def hash_invoke_token(raw_token: str) -> str:
    return hashlib.sha256(raw_token.encode("utf-8")).hexdigest()


class FunctionInvokeToken(models.Model):
    function = models.ForeignKey(
        Function,
        on_delete=models.CASCADE,
        related_name="invoke_tokens",
    )
    name = models.CharField(max_length=120)
    token_hash = models.CharField(max_length=64, unique=True)
    prefix = models.CharField(max_length=16, db_index=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_function_invoke_tokens",
    )
    is_active = models.BooleanField(default=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    revoked_at = models.DateTimeField(null=True, blank=True)
    last_used_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    @classmethod
    def create_token(cls, *, function, name: str, created_by=None, expires_at=None):
        raw_token = f"fn_{secrets.token_urlsafe(32)}"
        token = cls.objects.create(
            function=function,
            name=name,
            token_hash=hash_invoke_token(raw_token),
            prefix=raw_token[:16],
            created_by=created_by,
            expires_at=expires_at,
        )
        return token, raw_token

    def rotate(self, *, expires_at=None):
        raw_token = f"fn_{secrets.token_urlsafe(32)}"
        self.token_hash = hash_invoke_token(raw_token)
        self.prefix = raw_token[:16]
        self.expires_at = expires_at
        self.is_active = True
        self.revoked_at = None
        self.last_used_at = None
        self.save(
            update_fields=[
                "token_hash",
                "prefix",
                "expires_at",
                "is_active",
                "revoked_at",
                "last_used_at",
                "updated_at",
            ]
        )
        return raw_token

    def revoke(self, *, when=None) -> None:
        self.is_active = False
        self.revoked_at = when or timezone.now()
        self.save(update_fields=["is_active", "revoked_at", "updated_at"])

    def is_usable(self) -> bool:
        if not self.is_active:
            return False
        if self.revoked_at is not None:
            return False
        return self.expires_at is None or self.expires_at > timezone.now()

    def __str__(self) -> str:
        return f"{self.function.slug}:{self.name}"


class BuildStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    QUEUED = "queued", "Queued"
    BUILDING = "building", "Building"
    CANCELLING = "cancelling", "Cancelling"
    BUILT = "built", "Built"
    FAILED = "failed", "Failed"
    CANCELLED = "cancelled", "Cancelled"


class FunctionImageStatus(models.TextChoices):
    ACTIVE = "active", "Active"
    CANDIDATE = "candidate", "Candidate"
    PENDING_DELETE = "pending_delete", "Pending delete"
    DELETED = "deleted", "Deleted"
    DELETE_FAILED = "delete_failed", "Delete failed"


class FunctionVersion(models.Model):
    function = models.ForeignKey(
        Function,
        on_delete=models.CASCADE,
        related_name="versions",
    )
    version = models.CharField(max_length=40)
    runtime = models.CharField(max_length=40, default="python3.13")
    handler = models.CharField(max_length=255, default="handler.main")
    source_bundle = models.FileField(upload_to="function_bundles/")
    config = models.JSONField(default=dict, blank=True)
    invocation_input_mime_types = models.JSONField(default=list, blank=True)
    invocation_input_max_files = models.PositiveSmallIntegerField(default=1)
    invocation_input_max_size_mb = models.PositiveSmallIntegerField(default=10)
    invocation_input_max_total_size_mb = models.PositiveSmallIntegerField(default=10)
    declared_output_files = models.JSONField(default=list, blank=True)
    invocation_output_max_files = models.PositiveSmallIntegerField(default=5)
    invocation_output_max_file_size_mb = models.PositiveSmallIntegerField(default=10)
    invocation_output_max_total_size_mb = models.PositiveSmallIntegerField(default=10)
    invocation_max_retries = models.PositiveSmallIntegerField(default=0)
    invocation_retry_backoff_seconds = models.JSONField(default=list, blank=True)
    retry_invocation_timeouts = models.BooleanField(default=False)
    retry_invocation_function_errors = models.BooleanField(default=False)
    image_ref = models.CharField(max_length=255, blank=True)
    build_status = models.CharField(
        max_length=20,
        choices=BuildStatus.choices,
        default=BuildStatus.PENDING,
    )
    build_request_id = models.UUIDField(
        default=uuid.uuid4,
        db_index=True,
        editable=False,
    )
    build_log = models.TextField(blank=True)
    build_queued_at = models.DateTimeField(null=True, blank=True)
    build_started_at = models.DateTimeField(null=True, blank=True)
    build_finished_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [("function", "version")]
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.function.slug}:{self.version}"


class FunctionImage(models.Model):
    function = models.ForeignKey(
        Function,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="images",
    )
    function_version = models.ForeignKey(
        FunctionVersion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="images",
    )
    image_ref = models.CharField(max_length=500, unique=True)
    status = models.CharField(
        max_length=30,
        choices=FunctionImageStatus.choices,
        default=FunctionImageStatus.CANDIDATE,
        db_index=True,
    )
    reason = models.CharField(max_length=255, blank=True)
    delete_after = models.DateTimeField(null=True, blank=True, db_index=True)
    delete_attempts = models.PositiveSmallIntegerField(default=0)
    last_error = models.TextField(blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["function", "status"]),
            models.Index(fields=["status", "delete_after"]),
        ]

    def __str__(self) -> str:
        return f"{self.image_ref} ({self.status})"


class BuildAttempt(models.Model):
    request_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    build_id = models.UUIDField(default=uuid.uuid4, db_index=True, editable=False)
    function_version = models.ForeignKey(
        FunctionVersion,
        on_delete=models.CASCADE,
        related_name="build_attempts",
    )
    attempt_number = models.PositiveIntegerField(default=1)
    status = models.CharField(
        max_length=20,
        choices=BuildStatus.choices,
        default=BuildStatus.QUEUED,
    )
    image_ref = models.CharField(max_length=255, blank=True)
    log = models.TextField(blank=True)
    queued_at = models.DateTimeField(default=timezone.now)
    started_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    cancel_requested_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["build_id", "attempt_number"],
                name="unique_build_attempt_number",
            )
        ]

    def __str__(self) -> str:
        return (
            f"{self.function_version} build={self.build_id} "
            f"attempt={self.attempt_number}"
        )


class BuildPolicy(models.Model):
    max_retries = models.PositiveSmallIntegerField(default=2)
    max_builds_per_user_per_hour = models.PositiveIntegerField(default=20)
    max_builds_per_function_per_hour = models.PositiveIntegerField(default=10)
    max_queued_builds_per_user = models.PositiveIntegerField(default=5)
    max_queued_builds_per_function = models.PositiveIntegerField(default=3)
    max_concurrent_builds = models.PositiveIntegerField(default=2)
    build_lease_seconds = models.PositiveIntegerField(default=3600)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "build policy"

    def save(self, *args, **kwargs):
        self.pk = 1
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Build policy ({self.max_retries} retries)"


class BuildLeaseStatus(models.TextChoices):
    ACTIVE = "active", "Active"
    RELEASED = "released", "Released"
    EXPIRED = "expired", "Expired"


class BuildLease(models.Model):
    build_attempt = models.ForeignKey(
        BuildAttempt,
        on_delete=models.CASCADE,
        related_name="leases",
    )
    worker = models.ForeignKey(
        "workers.WorkerNode",
        on_delete=models.CASCADE,
        related_name="build_leases",
    )
    status = models.CharField(
        max_length=20,
        choices=BuildLeaseStatus.choices,
        default=BuildLeaseStatus.ACTIVE,
    )
    acquired_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField()
    released_at = models.DateTimeField(null=True, blank=True)
    release_reason = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-acquired_at"]

    def __str__(self) -> str:
        return f"{self.build_attempt.request_id} on {self.worker.name}"
