from django.db import models


class WorkerStatus(models.TextChoices):
    ONLINE = "online", "Online"
    OFFLINE = "offline", "Offline"
    DRAINING = "draining", "Draining"


class WorkerNode(models.Model):
    name = models.CharField(max_length=120, unique=True)
    hostname = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=WorkerStatus.choices,
        default=WorkerStatus.ONLINE,
    )
    max_concurrency = models.PositiveIntegerField(default=1)
    max_build_concurrency = models.PositiveIntegerField(default=1)
    metadata = models.JSONField(default=dict, blank=True)
    last_seen_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
