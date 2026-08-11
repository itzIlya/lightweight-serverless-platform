import io
from unittest.mock import patch
import zipfile

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from apps.accounts.models import Account, AccountRole
from apps.invocations.models import Invocation, InvocationAuthType
from apps.invocations.sync import SyncInvocationWaitResult

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


class SyncInvocationTests(APITestCase):
    def setUp(self):
        self.owner = get_user_model().objects.create_user(username="sync-owner")
        Account.objects.create(user=self.owner, role=AccountRole.USER)
        self.function = Function.objects.create(
            owner=self.owner,
            name="Sync Callable",
            slug="sync-callable",
        )
        self.version = FunctionVersion.objects.create(
            function=self.function,
            version="v1",
            source_bundle=function_bundle(),
            image_ref="localhost:5000/functions/sync-callable:v1-v1",
            build_status=BuildStatus.BUILT,
        )
        self.url = f"/api/functions/{self.function.id}/invoke-sync/"

    @patch("apps.functions.views.wait_for_sync_invocation")
    @patch("apps.functions.views.enqueue_invocation")
    def test_owner_can_sync_invoke_and_receive_terminal_result(self, enqueue, wait):
        authenticate_with_jwt(self.client, self.owner)
        wait.return_value = SyncInvocationWaitResult(
            completed=True,
            data={
                "id": 1,
                "status": "succeeded",
                "is_terminal": True,
                "result_available": True,
                "result": {"ok": True},
                "stdout": "done\n",
                "stderr": "",
                "exit_code": 0,
                "links": {"self": "/api/invocations/1/"},
            },
        )

        response = self.client.post(
            self.url,
            data={"event": {"name": "Ilya"}},
            format="json",
        )

        self.assertEqual(response.status_code, 200, response.content)
        self.assertEqual(response.data["result"], {"ok": True})
        self.assertEqual(response.data["stdout"], "done\n")
        self.assertIn("read_token", response.data)
        invocation = Invocation.objects.get()
        self.assertEqual(invocation.event, {"name": "Ilya"})
        self.assertEqual(invocation.invocation_auth_type, InvocationAuthType.OWNER_JWT)
        enqueue.assert_called_once_with(invocation)
        wait.assert_called_once_with(invocation)

    @patch("apps.functions.views.wait_for_sync_invocation")
    @patch("apps.functions.views.enqueue_invocation")
    def test_sync_timeout_returns_accepted_polling_response(self, enqueue, wait):
        authenticate_with_jwt(self.client, self.owner)
        wait.return_value = SyncInvocationWaitResult(
            completed=False,
            data={
                "id": 1,
                "status": "running",
                "is_terminal": False,
                "result_available": False,
                "poll_after_seconds": 1,
                "links": {"self": "/api/invocations/1/"},
            },
        )

        response = self.client.post(self.url, data={"event": {}}, format="json")

        self.assertEqual(response.status_code, 202, response.content)
        self.assertEqual(response.data["status"], "running")
        self.assertEqual(
            response.data["detail"],
            "Invocation is still running. Continue polling.",
        )
        enqueue.assert_called_once()

    @patch("apps.functions.views.wait_for_sync_invocation")
    @patch("apps.functions.views.enqueue_invocation")
    def test_function_token_can_sync_invoke_token_function(self, enqueue, wait):
        self.function.invoke_access = InvokeAccess.TOKEN
        self.function.save(update_fields=["invoke_access", "updated_at"])
        _, raw_token = FunctionInvokeToken.create_token(
            function=self.function,
            name="client",
            created_by=self.owner,
        )
        wait.return_value = SyncInvocationWaitResult(
            completed=True,
            data={
                "id": 1,
                "status": "succeeded",
                "is_terminal": True,
                "result_available": True,
                "result": {},
            },
        )

        response = self.client.post(
            self.url,
            data={"event": {}},
            format="json",
            HTTP_X_FUNCTION_TOKEN=raw_token,
        )

        self.assertEqual(response.status_code, 200, response.content)
        invocation = Invocation.objects.get()
        token = FunctionInvokeToken.objects.get()
        self.assertEqual(invocation.invocation_auth_type, InvocationAuthType.FUNCTION_TOKEN)
        self.assertEqual(invocation.invocation_token, token)
        enqueue.assert_called_once()

    @patch("apps.functions.views.wait_for_sync_invocation")
    @patch("apps.functions.views.enqueue_invocation")
    def test_sync_rejects_declared_output_files(self, enqueue, wait):
        authenticate_with_jwt(self.client, self.owner)
        self.version.declared_output_files = ["report.txt"]
        self.version.save(update_fields=["declared_output_files", "updated_at"])

        response = self.client.post(self.url, data={"event": {}}, format="json")

        self.assertEqual(response.status_code, 400, response.content)
        self.assertIn("without declared output files", str(response.data))
        self.assertEqual(Invocation.objects.count(), 0)
        enqueue.assert_not_called()
        wait.assert_not_called()

    @patch("apps.functions.views.wait_for_sync_invocation")
    @patch("apps.functions.views.enqueue_invocation")
    def test_sync_rejects_input_files(self, enqueue, wait):
        authenticate_with_jwt(self.client, self.owner)
        upload = SimpleUploadedFile("input.txt", b"hello", content_type="text/plain")

        response = self.client.post(
            self.url,
            data={"event": "{}", "input_files": upload},
            format="multipart",
        )

        self.assertEqual(response.status_code, 400, response.content)
        self.assertIn("does not accept input files", str(response.data))
        self.assertEqual(Invocation.objects.count(), 0)
        enqueue.assert_not_called()
        wait.assert_not_called()
