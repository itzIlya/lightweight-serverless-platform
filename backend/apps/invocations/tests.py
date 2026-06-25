import io
import zipfile

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from unittest.mock import patch

from apps.functions.models import Function, FunctionVersion

from .models import Invocation, InvocationInputFile, InvocationOutputFile, InvocationStatus


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
            invocation_input_max_total_size_mb=10,
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
    def test_invoke_rejects_files_over_combined_input_limit(self, enqueue):
        self.version.invocation_input_max_size_mb = 5
        self.version.invocation_input_max_total_size_mb = 1
        self.version.save()
        first = SimpleUploadedFile(
            "first.pdf",
            b"a" * 700_000,
            content_type="application/pdf",
        )
        second = SimpleUploadedFile(
            "second.pdf",
            b"b" * 700_000,
            content_type="application/pdf",
        )

        response = self.client.post(
            reverse("function-invoke", args=[self.version.function_id]),
            data={
                "event": '{"mode":"ocr"}',
                "files": [first, second],
            },
            format="multipart",
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("total size limit", str(response.data["files"]))
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


class InvocationOutputFileTests(APITestCase):
    def setUp(self):
        self.owner = get_user_model().objects.create_user(username="owner")
        self.other = get_user_model().objects.create_user(username="other")
        authenticate_with_jwt(self.client, self.owner)
        function = Function.objects.create(
            owner=self.owner,
            name="Reporter",
            slug="reporter",
        )
        self.version = FunctionVersion.objects.create(
            function=function,
            version="v1",
            source_bundle=function_bundle(),
            image_ref="localhost:5000/functions/reporter:v1-v1",
            build_status="built",
            declared_output_files=["report.txt"],
            invocation_output_max_files=1,
            invocation_output_max_file_size_mb=1,
            invocation_output_max_total_size_mb=1,
        )
        self.invocation = Invocation.objects.create(
            function_version=self.version,
            event={"name": "Ilya"},
            result={"ok": True},
            status=InvocationStatus.SUCCEEDED,
        )
        self.read_token = self.invocation.issue_read_token()

    def upload_output(self, *, name="report.txt", body=b"hello"):
        return self.client.post(
            reverse("upload-invocation-output", args=[self.invocation.request_id]),
            data={
                "original_path": name,
                "position": "0",
                "file": SimpleUploadedFile(
                    name,
                    body,
                    content_type="text/plain",
                ),
            },
            format="multipart",
            HTTP_X_INTERNAL_TOKEN="change-me",
        )

    def test_internal_worker_upload_stores_declared_output(self):
        response = self.upload_output()

        self.assertEqual(response.status_code, 201)
        output = InvocationOutputFile.objects.get(invocation=self.invocation)
        self.assertEqual(output.original_path, "report.txt")
        self.assertEqual(output.safe_name, "report.txt")
        self.assertEqual(output.size_bytes, 5)

    def test_internal_worker_upload_requires_shared_secret(self):
        response = self.client.post(
            reverse("upload-invocation-output", args=[self.invocation.request_id]),
            data={
                "original_path": "report.txt",
                "file": SimpleUploadedFile(
                    "report.txt",
                    b"hello",
                    content_type="text/plain",
                ),
            },
            format="multipart",
        )

        self.assertEqual(response.status_code, 401)

    def test_internal_worker_upload_rejects_undeclared_output(self):
        response = self.upload_output(name="extra.txt")

        self.assertEqual(response.status_code, 400)
        self.assertIn("not declared", str(response.data["output"]))
        self.assertEqual(InvocationOutputFile.objects.count(), 0)

    def test_internal_worker_upload_rejects_unsafe_output_path(self):
        response = self.upload_output(name="../report.txt")

        self.assertEqual(response.status_code, 400)
        self.assertIn("unsafe", str(response.data["output"]))
        self.assertEqual(InvocationOutputFile.objects.count(), 0)

    def test_internal_worker_upload_enforces_file_size_limit(self):
        response = self.upload_output(body=b"x" * (1024 * 1024 + 1))

        self.assertEqual(response.status_code, 400)
        self.assertIn("maximum size", str(response.data["output"]))
        self.assertEqual(InvocationOutputFile.objects.count(), 0)

    def test_owner_can_list_and_download_outputs(self):
        self.upload_output()
        output = self.invocation.output_files.get()

        list_response = self.client.get(
            reverse("invocation-outputs", args=[self.invocation.id]),
        )
        download_response = self.client.get(
            reverse(
                "invocation-download-output",
                args=[self.invocation.id, output.id],
            ),
        )

        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(list_response.data[0]["original_path"], "report.txt")
        self.assertEqual(download_response.status_code, 200)
        self.assertEqual(b"".join(download_response.streaming_content), b"hello")

    def test_other_user_cannot_list_outputs(self):
        self.upload_output()
        authenticate_with_jwt(self.client, self.other)

        response = self.client.get(
            reverse("invocation-outputs", args=[self.invocation.id]),
        )

        self.assertEqual(response.status_code, 404)

    def test_invocation_read_token_can_read_result_and_outputs(self):
        self.upload_output()
        output = self.invocation.output_files.get()
        self.client.credentials()

        retrieve_response = self.client.get(
            reverse("invocation-detail", args=[self.invocation.id]),
            HTTP_X_INVOCATION_READ_TOKEN=self.read_token,
        )
        list_response = self.client.get(
            reverse("invocation-outputs", args=[self.invocation.id]),
            HTTP_X_INVOCATION_READ_TOKEN=self.read_token,
        )
        download_response = self.client.get(
            reverse(
                "invocation-download-output",
                args=[self.invocation.id, output.id],
            ),
            HTTP_X_INVOCATION_READ_TOKEN=self.read_token,
        )

        self.assertEqual(retrieve_response.status_code, 200)
        self.assertEqual(retrieve_response.data["result"], {"ok": True})
        self.assertNotIn("read_token_hash", retrieve_response.data)
        self.assertNotIn("read_token_prefix", retrieve_response.data)
        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(list_response.data[0]["original_path"], "report.txt")
        self.assertEqual(download_response.status_code, 200)

    def test_wrong_invocation_read_token_is_rejected(self):
        self.upload_output()
        self.client.credentials()

        response = self.client.get(
            reverse("invocation-outputs", args=[self.invocation.id]),
            HTTP_X_INVOCATION_READ_TOKEN="inv_wrong",
        )

        self.assertEqual(response.status_code, 403)
