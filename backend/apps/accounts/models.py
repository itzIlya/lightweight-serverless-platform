from django.conf import settings
from django.db import models


class AccountRole(models.TextChoices):
    USER = "user", "User"
    ADMIN = "admin", "Admin"


class Account(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="account",
    )
    role = models.CharField(
        max_length=20,
        choices=AccountRole.choices,
        default=AccountRole.USER,
    )
    external_subject = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        unique=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["user__username"]

    def __str__(self) -> str:
        return f"{self.user.username} ({self.role})"
