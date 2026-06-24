from django.contrib import admin

from .models import WorkerNode


@admin.register(WorkerNode)
class WorkerNodeAdmin(admin.ModelAdmin):
    list_display = ("name", "hostname", "status", "max_concurrency", "last_seen_at")
    list_filter = ("status",)
    search_fields = ("name", "hostname")

