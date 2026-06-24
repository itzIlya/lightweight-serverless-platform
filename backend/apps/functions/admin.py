from django.contrib import admin

from .models import (
    BuildAttempt,
    BuildLease,
    BuildPolicy,
    Function,
    FunctionInvokeToken,
    FunctionVersion,
)


@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    list_display = ("slug", "name", "owner", "invoke_access", "created_at")
    list_filter = ("invoke_access",)
    search_fields = ("slug", "name", "owner__username")


@admin.register(FunctionInvokeToken)
class FunctionInvokeTokenAdmin(admin.ModelAdmin):
    list_display = ("function", "name", "prefix", "is_active", "expires_at", "last_used_at")
    list_filter = ("is_active",)
    search_fields = ("function__slug", "name", "prefix")
    readonly_fields = ("token_hash", "prefix", "last_used_at", "created_at", "updated_at")


@admin.register(FunctionVersion)
class FunctionVersionAdmin(admin.ModelAdmin):
    list_display = ("function", "version", "runtime", "build_status", "created_at")
    list_filter = ("runtime", "build_status")
    search_fields = ("function__slug", "version", "handler")


@admin.register(BuildAttempt)
class BuildAttemptAdmin(admin.ModelAdmin):
    list_display = (
        "request_id",
        "function_version",
        "attempt_number",
        "status",
        "queued_at",
        "finished_at",
    )
    list_filter = ("status", "attempt_number")
    search_fields = (
        "request_id",
        "build_id",
        "function_version__function__slug",
        "function_version__version",
    )
    readonly_fields = (
        "request_id",
        "build_id",
        "function_version",
        "attempt_number",
        "status",
        "image_ref",
        "log",
        "queued_at",
        "started_at",
        "finished_at",
        "cancel_requested_at",
        "created_at",
        "updated_at",
    )


@admin.register(BuildLease)
class BuildLeaseAdmin(admin.ModelAdmin):
    list_display = (
        "build_attempt",
        "worker",
        "status",
        "acquired_at",
        "expires_at",
        "released_at",
    )
    list_filter = ("status", "worker")
    search_fields = (
        "build_attempt__request_id",
        "build_attempt__function_version__function__slug",
        "worker__name",
    )
    readonly_fields = (
        "build_attempt",
        "worker",
        "status",
        "acquired_at",
        "expires_at",
        "released_at",
        "release_reason",
        "created_at",
        "updated_at",
    )


@admin.register(BuildPolicy)
class BuildPolicyAdmin(admin.ModelAdmin):
    list_display = (
        "max_retries",
        "max_builds_per_user_per_hour",
        "max_builds_per_function_per_hour",
        "max_queued_builds_per_user",
        "max_queued_builds_per_function",
        "max_concurrent_builds",
        "build_lease_seconds",
        "updated_at",
    )

    def has_add_permission(self, request):
        return not BuildPolicy.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
