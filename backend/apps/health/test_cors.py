from django.test import TestCase, override_settings


@override_settings(
    CORS_ALLOWED_ORIGINS=["http://localhost:5173"],
    CORS_ALLOW_ALL_ORIGINS=False,
)
class BackendCorsTests(TestCase):
    def test_preflight_allows_frontend_auth_headers(self):
        response = self.client.options(
            "/api/functions/",
            HTTP_ORIGIN="http://localhost:5173",
            HTTP_ACCESS_CONTROL_REQUEST_METHOD="POST",
            HTTP_ACCESS_CONTROL_REQUEST_HEADERS=(
                "authorization,content-type,x-function-token,x-invocation-read-token"
            ),
        )

        self.assertEqual(response.status_code, 204)
        self.assertEqual(
            response["Access-Control-Allow-Origin"],
            "http://localhost:5173",
        )
        self.assertIn("authorization", response["Access-Control-Allow-Headers"])
        self.assertIn("x-function-token", response["Access-Control-Allow-Headers"])
        self.assertIn(
            "x-invocation-read-token",
            response["Access-Control-Allow-Headers"],
        )

    def test_allowed_origin_gets_cors_headers_on_normal_response(self):
        response = self.client.get("/health/", HTTP_ORIGIN="http://localhost:5173")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response["Access-Control-Allow-Origin"],
            "http://localhost:5173",
        )
        self.assertIn("content-disposition", response["Access-Control-Expose-Headers"])

    def test_disallowed_origin_does_not_get_cors_headers(self):
        response = self.client.get("/health/", HTTP_ORIGIN="https://example.test")

        self.assertEqual(response.status_code, 200)
        self.assertNotIn("Access-Control-Allow-Origin", response)
