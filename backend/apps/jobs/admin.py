from django.contrib import admin

from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "job_id",
        "type",
        "status",
        "queue_name",
        "recovery_count",
        "max_recovery_attempts",
        "build_attempt",
        "invocation",
        "available_at",
        "dead_lettered_at",
        "created_at",
        "updated_at",
    )
    list_filter = ("type", "status", "queue_name", "dead_lettered_at")
    search_fields = (
        "job_id",
        "build_attempt__request_id",
        "invocation__request_id",
    )
    readonly_fields = (
        "job_id",
        "type",
        "status",
        "queue_name",
        "payload",
        "build_attempt",
        "invocation",
        "available_at",
        "locked_until",
        "dispatch_attempts",
        "recovery_count",
        "max_recovery_attempts",
        "last_recovered_at",
        "dead_lettered_at",
        "dead_letter_reason",
        "last_error",
        "created_at",
        "updated_at",
    )
