import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import override_settings
from django.urls import reverse
from rest_framework.test import APITestCase

from .keys import private_key
from .models import Account, AccountRole


@override_settings(
    JWT_KEY_PATH=settings.BASE_DIR / "keys" / "test_jwt_private.pem",
)
class UserServiceAuthTests(APITestCase):
    def test_register_returns_rs256_token_pair_and_jwks_verifies_access(self):
        response = self.client.post(
            reverse("userservice-register"),
            data={
                "username": "ilya",
                "email": "ilya@example.com",
                "first_name": "Ilya",
                "last_name": "Prototype",
                "password": "StrongerPass123!",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertEqual(response.data["user"]["first_name"], "Ilya")
        self.assertEqual(response.data["user"]["last_name"], "Prototype")
        self.assertEqual(response.data["user"]["role"], AccountRole.USER)
        self.assertTrue(Account.objects.filter(user__username="ilya").exists())

        jwks = self.client.get(reverse("userservice-jwks"))
        key = jwt.PyJWK.from_dict(jwks.data["keys"][0]).key
        claims = jwt.decode(
            response.data["access"],
            key=key,
            algorithms=["RS256"],
            issuer=settings.JWT_ISSUER,
            audience=settings.JWT_AUDIENCE,
        )
        self.assertEqual(claims["token_type"], "access")
        self.assertEqual(claims["username"], "ilya")

    def test_login_and_refresh_return_new_token_pair(self):
        user = get_user_model().objects.create_user(
            username="admin",
            email="admin@example.com",
            password="StrongerPass123!",
            is_staff=True,
        )
        Account.objects.create(user=user, role=AccountRole.ADMIN)

        login = self.client.post(
            reverse("userservice-token"),
            data={"username": "admin", "password": "StrongerPass123!"},
            format="json",
        )
        self.assertEqual(login.status_code, 200)
        self.assertEqual(login.data["user"]["role"], AccountRole.ADMIN)

        refresh = self.client.post(
            reverse("userservice-token-refresh"),
            data={"refresh": login.data["refresh"]},
            format="json",
        )
        self.assertEqual(refresh.status_code, 200)
        self.assertIn("access", refresh.data)
        self.assertIn("refresh", refresh.data)

    def test_logout_returns_stateless_client_cleanup_contract(self):
        response = self.client.post(reverse("userservice-logout"), format="json")

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["logged_out"])
        self.assertIn("stateless", response.data["detail"])

    def test_me_uses_userservice_access_token(self):
        user = get_user_model().objects.create_user(
            username="me",
            password="StrongerPass123!",
        )
        Account.objects.create(user=user, role=AccountRole.USER)
        token = jwt.encode(
            {
                "iss": settings.JWT_ISSUER,
                "aud": settings.JWT_AUDIENCE,
                "sub": str(user.userservice_account.subject),
                "username": user.username,
                "email": user.email,
                "role": AccountRole.USER,
                "token_type": "access",
                "exp": 4102444800,
            },
            private_key(),
            algorithm="RS256",
            headers={"kid": "test"},
        )

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        response = self.client.get(reverse("userservice-me"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], "me")
