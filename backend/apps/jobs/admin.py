from django.contrib import admin

from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "job_id",
        "type",
        "status",
        "queue_name",
        "build_attempt",
        "invocation",
        "created_at",
        "updated_at",
    )
    list_filter = ("type", "status", "queue_name")
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
        "last_error",
        "created_at",
        "updated_at",
    )

