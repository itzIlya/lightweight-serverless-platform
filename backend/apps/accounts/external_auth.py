from __future__ import annotations

import json
import time
import urllib.request

import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

from .models import Account


_jwks_cache = {
    "expires_at": 0,
    "keys": [],
}


class ExternalUserServiceJWTAuthentication(authentication.BaseAuthentication):
    keyword = "Bearer"

    def authenticate_header(self, request):
        return self.keyword

    def authenticate(self, request):
        header = authentication.get_authorization_header(request).decode("utf-8")
        if not header:
            return None
        parts = header.split()
        if len(parts) != 2 or parts[0] != self.keyword:
            return None

        raw_token = parts[1]
        try:
            unverified_header = jwt.get_unverified_header(raw_token)
        except jwt.InvalidTokenError:
            return None
        if unverified_header.get("alg") != settings.USERSERVICE_JWT_ALGORITHM:
            return None

        try:
            claims = _decode_external_token(raw_token, unverified_header)
        except Exception as exc:
            raise AuthenticationFailed("Invalid userservice access token.") from exc

        if claims.get("token_type") != "access":
            raise AuthenticationFailed("Userservice token must be an access token.")

        user = _sync_shadow_user(claims)
        return user, claims


def _decode_external_token(raw_token: str, unverified_header: dict) -> dict:
    key = _get_key(unverified_header.get("kid"))
    return jwt.decode(
        raw_token,
        key=key,
        algorithms=[settings.USERSERVICE_JWT_ALGORITHM],
        issuer=settings.USERSERVICE_JWT_ISSUER,
        audience=settings.USERSERVICE_JWT_AUDIENCE,
    )


def _get_key(kid: str | None):
    if not settings.USERSERVICE_JWKS_URL:
        raise AuthenticationFailed("Userservice JWKS URL is not configured.")

    for jwk in _get_jwks():
        if jwk.get("kid") == kid:
            return jwt.PyJWK.from_dict(jwk).key
    _jwks_cache["expires_at"] = 0
    for jwk in _get_jwks():
        if jwk.get("kid") == kid:
            return jwt.PyJWK.from_dict(jwk).key
    raise AuthenticationFailed("Userservice signing key is unknown.")


def _get_jwks() -> list[dict]:
    now = time.monotonic()
    if _jwks_cache["keys"] and _jwks_cache["expires_at"] > now:
        return _jwks_cache["keys"]

    with urllib.request.urlopen(settings.USERSERVICE_JWKS_URL, timeout=2) as response:
        payload = response.read()
    data = json.loads(payload)
    keys = data.get("keys", [])
    _jwks_cache["keys"] = keys
    _jwks_cache["expires_at"] = now + settings.USERSERVICE_JWKS_CACHE_SECONDS
    return keys


def clear_jwks_cache() -> None:
    _jwks_cache["expires_at"] = 0
    _jwks_cache["keys"] = []


def _sync_shadow_user(claims: dict):
    subject = str(claims.get("sub") or "").strip()
    if not subject:
        raise AuthenticationFailed("Userservice token is missing subject.")

    account = Account.objects.select_related("user").filter(
        external_subject=subject
    ).first()
    if account is not None:
        _update_shadow_user(account, claims)
        return account.user

    username = _unique_shadow_username(claims)
    user = get_user_model().objects.create_user(
        username=username,
        email=claims.get("email", "") or "",
    )
    user.set_unusable_password()
    user.save(update_fields=["password"])
    role = claims.get("role") or "user"
    if role not in {"user", "admin"}:
        role = "user"
    account = Account.objects.create(
        user=user,
        role=role,
        external_subject=subject,
    )
    return account.user


def _update_shadow_user(account: Account, claims: dict) -> None:
    changed_user_fields = []
    email = claims.get("email", "") or ""
    if email and account.user.email != email:
        account.user.email = email
        changed_user_fields.append("email")
    if changed_user_fields:
        account.user.save(update_fields=changed_user_fields)

    role = claims.get("role") or account.role
    if role not in {"user", "admin"}:
        role = "user"
    if account.role != role:
        account.role = role
        account.save(update_fields=["role", "updated_at"])


def _unique_shadow_username(claims: dict) -> str:
    subject = str(claims.get("sub") or "").replace("-", "")
    preferred = str(claims.get("username") or "").strip()
    base = preferred[:120] if preferred else f"user_{subject[:24]}"
    base = base or f"user_{subject[:24]}"
    candidate = base
    suffix = 1
    User = get_user_model()
    while User.objects.filter(username=candidate).exists():
        suffix += 1
        candidate = f"{base[:140]}_{suffix}"
    return candidate
