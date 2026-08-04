from __future__ import annotations

from datetime import datetime, timezone
import uuid

import jwt
from django.conf import settings
from django.utils import timezone as django_timezone

from .keys import key_id, private_key
from .models import Account


def _timestamp(value) -> int:
    return int(value.timestamp())


def _base_claims(*, account: Account, token_type: str, lifetime) -> dict:
    now = django_timezone.now()
    expires_at = now + lifetime
    return {
        "iss": settings.JWT_ISSUER,
        "aud": settings.JWT_AUDIENCE,
        "sub": str(account.subject),
        "username": account.user.username,
        "email": account.user.email,
        "role": account.role,
        "token_type": token_type,
        "iat": _timestamp(now),
        "nbf": _timestamp(now),
        "exp": _timestamp(expires_at),
        "jti": str(uuid.uuid4()),
    }


def encode_token(payload: dict) -> str:
    return jwt.encode(
        payload,
        private_key(),
        algorithm=settings.JWT_ALGORITHM,
        headers={"kid": key_id()},
    )


def issue_token_pair(user) -> dict:
    account, _ = Account.objects.get_or_create(user=user)
    access_claims = _base_claims(
        account=account,
        token_type="access",
        lifetime=settings.JWT_ACCESS_TOKEN_LIFETIME,
    )
    refresh_claims = _base_claims(
        account=account,
        token_type="refresh",
        lifetime=settings.JWT_REFRESH_TOKEN_LIFETIME,
    )
    return {
        "access": encode_token(access_claims),
        "refresh": encode_token(refresh_claims),
    }


def decode_token(raw_token: str, *, expected_type: str | None = None) -> dict:
    claims = jwt.decode(
        raw_token,
        private_key().public_key(),
        algorithms=[settings.JWT_ALGORITHM],
        issuer=settings.JWT_ISSUER,
        audience=settings.JWT_AUDIENCE,
    )
    if expected_type and claims.get("token_type") != expected_type:
        raise jwt.InvalidTokenError("Unexpected token type.")
    return claims
