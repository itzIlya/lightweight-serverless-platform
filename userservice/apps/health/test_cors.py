from django.test import TestCase, override_settings


@override_settings(
    CORS_ALLOWED_ORIGINS=["http://localhost:5173"],
    CORS_ALLOW_ALL_ORIGINS=False,
)
class UserserviceCorsTests(TestCase):
    def test_preflight_allows_frontend_auth_headers(self):
        response = self.client.options(
            "/api/auth/token/",
            HTTP_ORIGIN="http://localhost:5173",
            HTTP_ACCESS_CONTROL_REQUEST_METHOD="POST",
            HTTP_ACCESS_CONTROL_REQUEST_HEADERS="authorization,content-type",
        )

        self.assertEqual(response.status_code, 204)
        self.assertEqual(
            response["Access-Control-Allow-Origin"],
            "http://localhost:5173",
        )
        self.assertIn("authorization", response["Access-Control-Allow-Headers"])

    def test_disallowed_origin_does_not_get_cors_headers(self):
        response = self.client.get("/health/", HTTP_ORIGIN="https://example.test")

        self.assertEqual(response.status_code, 200)
        self.assertNotIn("Access-Control-Allow-Origin", response)
