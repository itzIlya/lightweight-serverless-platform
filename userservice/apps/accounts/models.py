import uuid

from django.conf import settings
from django.db import models


class AccountRole(models.TextChoices):
    USER = "user", "User"
    ADMIN = "admin", "Admin"


class Account(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="userservice_account",
    )
    subject = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    role = models.CharField(
        max_length=20,
        choices=AccountRole.choices,
        default=AccountRole.USER,
    )
    email_verified_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["user__username"]

    def __str__(self) -> str:
        return f"{self.user.username} ({self.subject})"
