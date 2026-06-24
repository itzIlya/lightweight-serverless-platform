from __future__ import annotations

from django.contrib.auth import get_user_model

from .models import Account, AccountRole


def ensure_account(user):
    if not user or not user.is_authenticated:
        return None
    account, _ = Account.objects.get_or_create(user=user)
    return account


def get_user_role(user) -> str:
    if not user or not user.is_authenticated:
        return ""
    if user.is_superuser or user.is_staff:
        return AccountRole.ADMIN
    account = ensure_account(user)
    return account.role if account else ""


def is_platform_admin(user) -> bool:
    return get_user_role(user) == AccountRole.ADMIN


def create_user_with_account(
    *,
    username: str,
    password: str,
    email: str = "",
    role: str = AccountRole.USER,
):
    user = get_user_model().objects.create_user(
        username=username,
        email=email,
        password=password,
    )
    Account.objects.create(user=user, role=role)
    return user

