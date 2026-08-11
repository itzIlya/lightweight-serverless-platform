import io
from unittest.mock import patch
import zipfile

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from apps.accounts.models import Account, AccountRole
from apps.invocations.models import Invocation, InvocationAuthType
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
        self.other = get_user_model().objects.create_user(username="other")
        self.admin = get_user_model().objects.create_user(
            username="token-admin",
            is_staff=True,
        )
        Account.objects.create(user=self.owner, role=AccountRole.USER)
        Account.objects.create(user=self.other, role=AccountRole.USER)
        Account.objects.create(user=self.admin, role=AccountRole.ADMIN)
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


class FunctionInvokeTokenManagementTests(APITestCase):
    def setUp(self):
        self.owner = get_user_model().objects.create_user(username="token-owner")
        self.other = get_user_model().objects.create_user(username="token-other")
        self.admin = get_user_model().objects.create_user(
            username="token-platform-admin",
            is_staff=True,
        )
        Account.objects.create(user=self.owner, role=AccountRole.USER)
        Account.objects.create(user=self.other, role=AccountRole.USER)
        Account.objects.create(user=self.admin, role=AccountRole.ADMIN)
        self.function = Function.objects.create(
            owner=self.owner,
            name="Token Callable",
            slug="token-callable",
            invoke_access=InvokeAccess.TOKEN,
        )
        self.version = FunctionVersion.objects.create(
            function=self.function,
            version="v1",
            source_bundle=function_bundle(),
            image_ref="localhost:5000/functions/token-callable:v1-v1",
            build_status=BuildStatus.BUILT,
        )

    def token_list_url(self):
        return f"/api/functions/{self.function.id}/tokens/"

    def token_detail_url(self, token):
        return f"/api/functions/{self.function.id}/tokens/{token.id}/"

    def token_revoke_url(self, token):
        return f"/api/functions/{self.function.id}/tokens/{token.id}/revoke/"

    def token_rotate_url(self, token):
        return f"/api/functions/{self.function.id}/tokens/{token.id}/rotate/"

    def create_token_via_api(self, *, name="client", expires_at=None):
        payload = {"name": name}
        if expires_at is not None:
            payload["expires_at"] = expires_at
        return self.client.post(self.token_list_url(), data=payload, format="json")

    def test_owner_can_create_token_and_raw_token_is_returned_once(self):
        authenticate_with_jwt(self.client, self.owner)

        create_response = self.create_token_via_api(name="mobile-client")
        list_response = self.client.get(self.token_list_url())
        detail_response = self.client.get(
            self.token_detail_url(FunctionInvokeToken.objects.get())
        )

        self.assertEqual(create_response.status_code, 201, create_response.content)
        self.assertTrue(create_response.data["raw_token"].startswith("fn_"))
        self.assertEqual(create_response.data["token"]["name"], "mobile-client")
        self.assertNotIn("token_hash", create_response.data["token"])
        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(len(list_response.data), 1)
        self.assertNotIn("raw_token", list_response.data[0])
        self.assertNotIn("token_hash", list_response.data[0])
        self.assertEqual(detail_response.status_code, 200)
        self.assertNotIn("raw_token", detail_response.data)
        self.assertNotIn("token_hash", detail_response.data)

    def test_other_user_cannot_manage_tokens_for_someone_elses_function(self):
        authenticate_with_jwt(self.client, self.other)

        response = self.create_token_via_api(name="not-yours")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(FunctionInvokeToken.objects.count(), 0)

    def test_admin_can_manage_function_tokens(self):
        authenticate_with_jwt(self.client, self.admin)

        response = self.create_token_via_api(name="admin-created")

        self.assertEqual(response.status_code, 201, response.content)
        token = FunctionInvokeToken.objects.get()
        self.assertEqual(token.created_by, self.admin)

    @patch("apps.functions.views.enqueue_invocation")
    def test_created_token_can_invoke_and_updates_last_used_at(self, enqueue):
        authenticate_with_jwt(self.client, self.owner)
        create_response = self.create_token_via_api(name="invoke-client")
        raw_token = create_response.data["raw_token"]
        self.client.credentials()

        response = self.client.post(
            reverse("function-invoke", args=[self.function.id]),
            data={"event": {"hello": "world"}},
            format="json",
            HTTP_X_FUNCTION_TOKEN=raw_token,
        )

        self.assertEqual(response.status_code, 202, response.content)
        token = FunctionInvokeToken.objects.get()
        self.assertIsNotNone(token.last_used_at)
        invocation = Invocation.objects.get()
        self.assertEqual(invocation.invocation_auth_type, InvocationAuthType.FUNCTION_TOKEN)
        self.assertEqual(invocation.invocation_token, token)
        enqueue.assert_called_once()

    @patch("apps.functions.views.enqueue_invocation")
    def test_token_invocation_history_exposes_token_metadata_to_owner(self, enqueue):
        authenticate_with_jwt(self.client, self.owner)
        create_response = self.create_token_via_api(name="partner-client")
        raw_token = create_response.data["raw_token"]
        token = FunctionInvokeToken.objects.get()
        self.client.credentials()
        invoke_response = self.client.post(
            reverse("function-invoke", args=[self.function.id]),
            data={"event": {"hello": "token"}},
            format="json",
            HTTP_X_FUNCTION_TOKEN=raw_token,
        )
        authenticate_with_jwt(self.client, self.owner)

        history_response = self.client.get(
            reverse("function-invocations", args=[self.function.id])
        )

        self.assertEqual(invoke_response.status_code, 202, invoke_response.content)
        self.assertEqual(history_response.status_code, 200, history_response.content)
        self.assertEqual(history_response.data[0]["invocation_auth_type"], InvocationAuthType.FUNCTION_TOKEN)
        self.assertEqual(history_response.data[0]["invocation_token"], token.id)
        self.assertEqual(history_response.data[0]["invocation_token_name"], "partner-client")
        self.assertEqual(history_response.data[0]["invocation_token_prefix"], token.prefix)
        enqueue.assert_called_once()

    @patch("apps.functions.views.enqueue_invocation")
    def test_revoked_token_cannot_invoke(self, enqueue):
        authenticate_with_jwt(self.client, self.owner)
        create_response = self.create_token_via_api(name="revoked-client")
        raw_token = create_response.data["raw_token"]
        token = FunctionInvokeToken.objects.get()
        revoke_response = self.client.post(self.token_revoke_url(token))
        self.client.credentials()

        invoke_response = self.client.post(
            reverse("function-invoke", args=[self.function.id]),
            data={"event": {}},
            format="json",
            HTTP_X_FUNCTION_TOKEN=raw_token,
        )

        token.refresh_from_db()
        self.assertEqual(revoke_response.status_code, 200)
        self.assertFalse(token.is_active)
        self.assertIsNotNone(token.revoked_at)
        self.assertEqual(invoke_response.status_code, 403)
        enqueue.assert_not_called()

    @patch("apps.functions.views.enqueue_invocation")
    def test_rotated_token_invalidates_old_secret_and_returns_new_secret(self, enqueue):
        authenticate_with_jwt(self.client, self.owner)
        create_response = self.create_token_via_api(name="rotating-client")
        old_raw_token = create_response.data["raw_token"]
        token = FunctionInvokeToken.objects.get()
        rotate_response = self.client.post(self.token_rotate_url(token), data={}, format="json")
        new_raw_token = rotate_response.data["raw_token"]
        self.client.credentials()

        old_response = self.client.post(
            reverse("function-invoke", args=[self.function.id]),
            data={"event": {}},
            format="json",
            HTTP_X_FUNCTION_TOKEN=old_raw_token,
        )
        new_response = self.client.post(
            reverse("function-invoke", args=[self.function.id]),
            data={"event": {}},
            format="json",
            HTTP_X_FUNCTION_TOKEN=new_raw_token,
        )

        self.assertEqual(rotate_response.status_code, 200)
        self.assertNotEqual(old_raw_token, new_raw_token)
        self.assertEqual(old_response.status_code, 403)
        self.assertEqual(new_response.status_code, 202)
        enqueue.assert_called_once()

    @patch("apps.functions.views.enqueue_invocation")
    def test_expired_token_cannot_invoke(self, enqueue):
        _, raw_token = FunctionInvokeToken.create_token(
            function=self.function,
            name="expired-client",
            created_by=self.owner,
            expires_at=timezone.now() - timezone.timedelta(minutes=1),
        )

        response = self.client.post(
            reverse("function-invoke", args=[self.function.id]),
            data={"event": {}},
            format="json",
            HTTP_X_FUNCTION_TOKEN=raw_token,
        )

        self.assertEqual(response.status_code, 403)
        enqueue.assert_not_called()

    def test_cannot_create_token_with_past_expiry(self):
        authenticate_with_jwt(self.client, self.owner)

        response = self.create_token_via_api(
            name="already-expired",
            expires_at=(timezone.now() - timezone.timedelta(minutes=1)).isoformat(),
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("expires_at", response.data)

    def test_cannot_reactivate_expired_token(self):
        authenticate_with_jwt(self.client, self.owner)
        token, _ = FunctionInvokeToken.create_token(
            function=self.function,
            name="inactive-expired",
            created_by=self.owner,
            expires_at=timezone.now() - timezone.timedelta(minutes=1),
        )
        token.is_active = False
        token.revoked_at = timezone.now()
        token.save(update_fields=["is_active", "revoked_at", "updated_at"])

        response = self.client.patch(
            self.token_detail_url(token),
            data={"is_active": True},
            format="json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("is_active", response.data)

    def test_delete_soft_revokes_token(self):
        authenticate_with_jwt(self.client, self.owner)
        token, _ = FunctionInvokeToken.create_token(
            function=self.function,
            name="delete-client",
            created_by=self.owner,
        )

        response = self.client.delete(self.token_detail_url(token))

        token.refresh_from_db()
        self.assertEqual(response.status_code, 204)
        self.assertFalse(token.is_active)
        self.assertIsNotNone(token.revoked_at)

    def test_active_token_names_must_be_unique_per_function(self):
        authenticate_with_jwt(self.client, self.owner)
        first = self.create_token_via_api(name="duplicate-client")
        second = self.create_token_via_api(name="Duplicate-Client")

        self.assertEqual(first.status_code, 201)
        self.assertEqual(second.status_code, 400)
        self.assertIn("name", second.data)

    @override_settings(MAX_ACTIVE_INVOKE_TOKENS_PER_FUNCTION=1)
    def test_max_active_token_limit_is_enforced(self):
        authenticate_with_jwt(self.client, self.owner)
        first = self.create_token_via_api(name="first-client")
        second = self.create_token_via_api(name="second-client")

        self.assertEqual(first.status_code, 201)
        self.assertEqual(second.status_code, 400)
        self.assertIn("tokens", second.data)

    def test_patch_can_rename_expire_and_deactivate_token(self):
        authenticate_with_jwt(self.client, self.owner)
        token, _ = FunctionInvokeToken.create_token(
            function=self.function,
            name="old-name",
            created_by=self.owner,
        )
        expires_at = timezone.now() + timezone.timedelta(days=1)

        response = self.client.patch(
            self.token_detail_url(token),
            data={
                "name": "new-name",
                "expires_at": expires_at.isoformat(),
                "is_active": False,
            },
            format="json",
        )

        token.refresh_from_db()
        self.assertEqual(response.status_code, 200, response.content)
        self.assertEqual(token.name, "new-name")
        self.assertFalse(token.is_active)
        self.assertIsNotNone(token.revoked_at)
        self.assertIsNotNone(token.expires_at)

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
