import io
from unittest.mock import patch
import zipfile

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from apps.accounts.models import Account, AccountRole
from apps.invocations.models import Invocation
from apps.workers.models import WorkerNode

from .models import (
    BuildStatus,
    Function,
    FunctionInvokeToken,
    FunctionVersion,
    InvokeAccess,
)


def function_bundle() -> SimpleUploadedFile:
    data = io.BytesIO()
    with zipfile.ZipFile(data, "w") as archive:
        archive.writestr(
            "handler.py",
            "def main(event, context):\n    return {'echo': event}\n",
        )
        archive.writestr("requirements.txt", "")
        archive.writestr("config.json", "{}")
    return SimpleUploadedFile(
        "function.zip",
        data.getvalue(),
        content_type="application/zip",
    )


def authenticate_with_jwt(client, user) -> None:
    access = RefreshToken.for_user(user).access_token
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")


class OwnershipAuthorizationTests(APITestCase):
    def setUp(self):
        user_model = get_user_model()
        self.alice = user_model.objects.create_user(username="alice")
        self.bob = user_model.objects.create_user(username="bob")
        self.admin = user_model.objects.create_user(username="admin", is_staff=True)
        Account.objects.create(user=self.alice, role=AccountRole.USER)
        Account.objects.create(user=self.bob, role=AccountRole.USER)
        Account.objects.create(user=self.admin, role=AccountRole.ADMIN)
        self.alice_function = Function.objects.create(
            owner=self.alice,
            name="Alice Function",
            slug="alice-function",
        )
        self.bob_function = Function.objects.create(
            owner=self.bob,
            name="Bob Function",
            slug="bob-function",
        )
        self.bob_version = FunctionVersion.objects.create(
            function=self.bob_function,
            version="v1",
            source_bundle=function_bundle(),
        )

    def test_function_create_uses_authenticated_user_not_owner_id(self):
        authenticate_with_jwt(self.client, self.alice)

        response = self.client.post(
            reverse("function-list"),
            data={
                "owner_id": self.bob.id,
                "name": "Created By Alice",
                "description": "",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        function = Function.objects.get(id=response.data["id"])
        self.assertEqual(function.owner, self.alice)

    def test_user_only_lists_their_own_functions(self):
        authenticate_with_jwt(self.client, self.alice)

        response = self.client.get(reverse("function-list"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual([item["slug"] for item in response.data], ["alice-function"])

    def test_user_cannot_access_another_users_version_or_builds(self):
        authenticate_with_jwt(self.client, self.alice)

        detail = self.client.get(
            reverse("function-version-detail", args=[self.bob_version.id])
        )
        build = self.client.post(
            reverse("function-version-build", args=[self.bob_version.id])
        )

        self.assertEqual(detail.status_code, 404)
        self.assertEqual(build.status_code, 404)

    def test_user_cannot_access_another_users_invocation_history(self):
        invocation = Invocation.objects.create(
            function_version=self.bob_version,
            event={},
        )
        authenticate_with_jwt(self.client, self.alice)

        detail = self.client.get(reverse("invocation-detail", args=[invocation.id]))

        self.assertEqual(detail.status_code, 404)

    def test_workers_endpoint_is_admin_only(self):
        WorkerNode.objects.create(name="worker-1", hostname="worker-1")

        authenticate_with_jwt(self.client, self.alice)
        user_response = self.client.get(reverse("worker-list"))
        authenticate_with_jwt(self.client, self.admin)
        admin_response = self.client.get(reverse("worker-list"))

        self.assertEqual(user_response.status_code, 403)
        self.assertEqual(admin_response.status_code, 200)


class InvocationAccessTests(APITestCase):
    def setUp(self):
        self.owner = get_user_model().objects.create_user(username="owner")
        Account.objects.create(user=self.owner, role=AccountRole.USER)
        self.function = Function.objects.create(
            owner=self.owner,
            name="Callable",
            slug="callable",
        )
        self.version = FunctionVersion.objects.create(
            function=self.function,
            version="v1",
            source_bundle=function_bundle(),
            image_ref="localhost:5000/functions/callable:v1-v1",
            build_status=BuildStatus.BUILT,
        )

    @patch("apps.functions.views.enqueue_invocation")
    def test_private_function_requires_owner_jwt(self, enqueue):
        response = self.client.post(
            reverse("function-invoke", args=[self.function.id]),
            data={"event": {}},
            format="json",
        )

        self.assertEqual(response.status_code, 401)
        enqueue.assert_not_called()

    @patch("apps.functions.views.enqueue_invocation")
    def test_owner_jwt_can_invoke_private_function(self, enqueue):
        authenticate_with_jwt(self.client, self.owner)

        response = self.client.post(
            reverse("function-invoke", args=[self.function.id]),
            data={"event": {}},
            format="json",
        )

        self.assertEqual(response.status_code, 202)
        enqueue.assert_called_once()

    @patch("apps.functions.views.enqueue_invocation")
    def test_function_invoke_token_is_separate_from_jwt(self, enqueue):
        self.function.invoke_access = InvokeAccess.TOKEN
        self.function.save()
        _, raw_token = FunctionInvokeToken.create_token(
            function=self.function,
            name="client token",
            created_by=self.owner,
        )

        invoke_response = self.client.post(
            reverse("function-invoke", args=[self.function.id]),
            data={"event": {}},
            format="json",
            HTTP_X_FUNCTION_TOKEN=raw_token,
        )
        management_response = self.client.get(reverse("function-list"))

        self.assertEqual(invoke_response.status_code, 202)
        self.assertEqual(management_response.status_code, 401)
        enqueue.assert_called_once()

    @patch("apps.functions.views.enqueue_invocation")
    def test_public_function_can_be_invoked_without_jwt(self, enqueue):
        self.function.invoke_access = InvokeAccess.PUBLIC
        self.function.save()

        response = self.client.post(
            reverse("function-invoke", args=[self.function.id]),
            data={"event": {}},
            format="json",
        )

        self.assertEqual(response.status_code, 202)
        enqueue.assert_called_once()
