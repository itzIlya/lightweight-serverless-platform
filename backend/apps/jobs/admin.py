from django.contrib import admin

from .models import Job, OutboxEvent


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "job_id",
        "type",
        "status",
        "coordination_version",
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
    list_filter = (
        "type",
        "status",
        "coordination_version",
        "queue_name",
        "dead_lettered_at",
    )
    search_fields = (
        "job_id",
        "build_attempt__request_id",
        "invocation__request_id",
    )
    readonly_fields = (
        "job_id",
        "type",
        "status",
        "coordination_version",
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


@admin.register(OutboxEvent)
class OutboxEventAdmin(admin.ModelAdmin):
    list_display = (
        "event_id",
        "event_type",
        "aggregate_id",
        "publish_attempts",
        "published_at",
        "stream_id",
        "created_at",
    )
    list_filter = ("event_type", "published_at")
    search_fields = ("event_id", "aggregate_id")
    readonly_fields = (
        "event_id",
        "aggregate_id",
        "event_type",
        "payload",
        "publish_attempts",
        "published_at",
        "stream_id",
        "last_error",
        "created_at",
        "updated_at",
    )
