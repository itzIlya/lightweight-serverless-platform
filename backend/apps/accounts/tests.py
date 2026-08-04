from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import override_settings
import base64
import importlib.util
import jwt
import unittest
from unittest.mock import patch
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Account, AccountRole
from apps.functions.models import Function


def authenticate_with_jwt(client, user) -> None:
    access = RefreshToken.for_user(user).access_token
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")


class AccountAuthTests(APITestCase):
    def test_register_returns_user_and_jwt_pair(self):
        response = self.client.post(
            reverse("auth-register"),
            data={
                "username": "ilya",
                "email": "ilya@example.com",
                "password": "StrongerPass123!",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertEqual(response.data["user"]["username"], "ilya")
        self.assertEqual(response.data["user"]["role"], AccountRole.USER)
        self.assertTrue(Account.objects.filter(user__username="ilya").exists())

    def test_login_response_includes_user_role(self):
        user = get_user_model().objects.create_user(
            username="admin",
            password="StrongerPass123!",
            is_staff=True,
        )
        Account.objects.create(user=user, role=AccountRole.ADMIN)

        response = self.client.post(
            reverse("token-obtain-pair"),
            data={
                "username": "admin",
                "password": "StrongerPass123!",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertEqual(response.data["user"]["role"], AccountRole.ADMIN)

    def test_me_returns_authenticated_user(self):
        user = get_user_model().objects.create_user(username="me")
        Account.objects.create(user=user, role=AccountRole.USER)
        authenticate_with_jwt(self.client, user)

        response = self.client.get(reverse("auth-me"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], "me")
        self.assertEqual(response.data["role"], AccountRole.USER)


def _b64url_uint(value: int) -> str:
    raw = value.to_bytes((value.bit_length() + 7) // 8, "big")
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode("ascii")


def _rsa_jwk(key, kid="test-key") -> dict:
    numbers = key.public_key().public_numbers()
    return {
        "kty": "RSA",
        "use": "sig",
        "kid": kid,
        "alg": "RS256",
        "n": _b64url_uint(numbers.n),
        "e": _b64url_uint(numbers.e),
    }


@override_settings(
    USERSERVICE_JWKS_URL="http://userservice.test/jwks/",
    USERSERVICE_JWT_ISSUER="serverless-userservice",
    USERSERVICE_JWT_AUDIENCE="serverless-platform",
)
@unittest.skipUnless(
    importlib.util.find_spec("cryptography"),
    "cryptography is required for RS256 userservice JWT tests",
)
class ExternalUserServiceJWTTests(APITestCase):
    def test_backend_accepts_userservice_jwt_and_creates_shadow_owner(self):
        from cryptography.hazmat.primitives.asymmetric import rsa

        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        token = jwt.encode(
            {
                "iss": "serverless-userservice",
                "aud": "serverless-platform",
                "sub": "user-subject-123",
                "username": "external-owner",
                "email": "owner@example.com",
                "role": AccountRole.USER,
                "token_type": "access",
                "exp": 4102444800,
            },
            key,
            algorithm="RS256",
            headers={"kid": "test-key"},
        )

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        with patch("apps.accounts.external_auth._get_jwks", return_value=[_rsa_jwk(key)]):
            response = self.client.post(
                "/api/functions/",
                data={"name": "External Auth Function"},
                format="json",
            )

        self.assertEqual(response.status_code, 201)
        function = Function.objects.get()
        account = Account.objects.get(user=function.owner)
        self.assertEqual(account.external_subject, "user-subject-123")
        self.assertEqual(account.role, AccountRole.USER)
