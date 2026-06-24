import io
import zipfile

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from unittest.mock import patch

from apps.functions.models import Function, FunctionVersion

from .models import Invocation, InvocationInputFile, InvocationStatus


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


class InvocationInputFileTests(APITestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(username="invoker")
        authenticate_with_jwt(self.client, user)
        function = Function.objects.create(owner=user, name="Parser", slug="parser")
        self.version = FunctionVersion.objects.create(
            function=function,
            version="v1",
            source_bundle=function_bundle(),
            image_ref="localhost:5000/functions/parser:v1-v1",
            build_status="built",
            invocation_input_mime_types=["application/pdf"],
            invocation_input_max_files=2,
            invocation_input_max_size_mb=5,
        )

    @patch("apps.functions.views.enqueue_invocation")
    def test_invoke_with_allowed_file_stores_attachment(self, enqueue):
        pdf = SimpleUploadedFile(
            "document.pdf",
            b"%PDF-1.4\n%EOF\n",
            content_type="application/pdf",
        )

        response = self.client.post(
            reverse("function-invoke", args=[self.version.function_id]),
            data={
                "event": '{"mode":"ocr"}',
                "files": pdf,
            },
            format="multipart",
        )

        self.assertEqual(response.status_code, 202)
        self.assertIn("input_files", response.data)
        self.assertEqual(len(response.data["input_files"]), 1)
        invocation = Invocation.objects.get(id=response.data["id"])
        self.assertEqual(invocation.input_files.count(), 1)
        stored = invocation.input_files.first()
        self.assertEqual(stored.original_name, "document.pdf")
        self.assertEqual(stored.content_type, "application/pdf")
        enqueue.assert_called_once()

    @patch("apps.functions.views.enqueue_invocation")
    def test_invoke_rejects_disallowed_file_type(self, enqueue):
        png = SimpleUploadedFile(
            "image.png",
            b"\x89PNG\r\n\x1a\n",
            content_type="image/png",
        )

        response = self.client.post(
            reverse("function-invoke", args=[self.version.function_id]),
            data={
                "event": '{"mode":"ocr"}',
                "files": png,
            },
            format="multipart",
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("files", response.data)
        self.assertEqual(Invocation.objects.count(), 0)
        enqueue.assert_not_called()

    @patch("apps.functions.views.enqueue_invocation")
    def test_worker_internal_endpoints_list_and_download_inputs(self, enqueue):
        pdf = SimpleUploadedFile(
            "document.pdf",
            b"%PDF-1.4\n%EOF\n",
            content_type="application/pdf",
        )
        response = self.client.post(
            reverse("function-invoke", args=[self.version.function_id]),
            data={
                "event": '{"mode":"ocr"}',
                "files": pdf,
            },
            format="multipart",
        )
        invocation = Invocation.objects.get(id=response.data["id"])
        input_file = invocation.input_files.first()

        list_response = self.client.get(
            reverse("list-invocation-inputs", args=[invocation.request_id]),
            HTTP_X_INTERNAL_TOKEN="change-me",
        )
        download_response = self.client.get(
            reverse(
                "download-invocation-input",
                args=[invocation.request_id, input_file.id],
            ),
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(list_response.data[0]["original_name"], "document.pdf")
        self.assertEqual(download_response.status_code, 200)

    def test_internal_input_endpoints_require_shared_secret(self):
        invocation = Invocation.objects.create(
            function_version=self.version,
            event={},
        )
        input_file = InvocationInputFile.objects.create(
            invocation=invocation,
            position=0,
            field_name="files",
            original_name="document.pdf",
            content_type="application/pdf",
            size_bytes=4,
        )

        list_response = self.client.get(
            reverse("list-invocation-inputs", args=[invocation.request_id]),
        )
        download_response = self.client.get(
            reverse(
                "download-invocation-input",
                args=[invocation.request_id, input_file.id],
            ),
        )

        self.assertEqual(list_response.status_code, 401)
        self.assertEqual(download_response.status_code, 401)
