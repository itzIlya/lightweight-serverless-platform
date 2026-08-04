from __future__ import annotations

from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

from .models import Account
from .tokens import decode_token


class UserServiceJWTAuthentication(authentication.BaseAuthentication):
    keyword = "Bearer"

    def authenticate(self, request):
        header = authentication.get_authorization_header(request).decode("utf-8")
        if not header:
            return None
        parts = header.split()
        if len(parts) != 2 or parts[0] != self.keyword:
            return None
        try:
            claims = decode_token(parts[1], expected_type="access")
        except Exception as exc:
            raise AuthenticationFailed("Invalid access token.") from exc

        subject = claims.get("sub")
        if not subject:
            raise AuthenticationFailed("Token is missing subject.")
        account = Account.objects.select_related("user").filter(subject=subject).first()
        if account is None:
            raise AuthenticationFailed("User no longer exists.")
        return account.user, claims
