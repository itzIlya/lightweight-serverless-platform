from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Account, AccountRole


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
