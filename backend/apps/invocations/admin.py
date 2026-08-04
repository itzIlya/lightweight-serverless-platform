from django.contrib import admin

from .models import (
    Invocation,
    InvocationAttempt,
    InvocationInputFile,
    InvocationLogArtifact,
    InvocationOutputFile,
    InvocationStagedCompletion,
)


@admin.register(Invocation)
class InvocationAdmin(admin.ModelAdmin):
    list_display = ("request_id", "function_version", "status", "cold_start", "queued_at")
    list_filter = ("status", "cold_start")
    search_fields = ("request_id", "function_version__function__slug")


@admin.register(InvocationAttempt)
class InvocationAttemptAdmin(admin.ModelAdmin):
    list_display = (
        "invocation",
        "attempt_number",
        "dispatch_attempt",
        "worker_name",
        "status",
        "failure_kind",
        "queued_at",
    )
    list_filter = ("status", "failure_kind")
    search_fields = ("invocation__request_id", "worker_name")


@admin.register(InvocationInputFile)
class InvocationInputFileAdmin(admin.ModelAdmin):
    list_display = (
        "invocation",
        "position",
        "original_name",
        "content_type",
        "size_bytes",
        "created_at",
    )
    search_fields = ("invocation__request_id", "original_name", "content_type")


@admin.register(InvocationOutputFile)
class InvocationOutputFileAdmin(admin.ModelAdmin):
    list_display = (
        "invocation",
        "position",
        "original_path",
        "status",
        "staged_completion",
        "content_type",
        "size_bytes",
        "created_at",
    )
    search_fields = ("invocation__request_id", "original_path", "content_type")


@admin.register(InvocationStagedCompletion)
class InvocationStagedCompletionAdmin(admin.ModelAdmin):
    list_display = (
        "completion_id",
        "invocation",
        "dispatch_attempt",
        "status",
        "artifact_commit_id",
        "expires_at",
    )
    list_filter = ("status", "terminal_status")


@admin.register(InvocationLogArtifact)
class InvocationLogArtifactAdmin(admin.ModelAdmin):
    list_display = (
        "invocation",
        "stream",
        "status",
        "staged_completion",
        "size_bytes",
        "created_at",
    )
    list_filter = ("stream", "status")
    search_fields = ("invocation__request_id", "stream", "safe_name")
