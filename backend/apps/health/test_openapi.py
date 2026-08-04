from django.test import TestCase


class BackendOpenAPITests(TestCase):
    def test_openapi_schema_is_public_and_frontend_focused(self):
        response = self.client.get("/api/schema/")

        self.assertEqual(response.status_code, 200)
        schema = response.json()
        self.assertEqual(schema["openapi"], "3.0.3")
        self.assertIn("/api/functions/{function_id}/invoke/", schema["paths"])
        self.assertIn("/api/invocations/{invocation_id}/download/", schema["paths"])
        self.assertIn("Invocation", schema["components"]["schemas"])
        invocation = schema["components"]["schemas"]["Invocation"]
        self.assertIn("frontend_state", invocation["properties"])
        self.assertIn("can_download", invocation["properties"])

    def test_swagger_docs_page_points_to_schema(self):
        response = self.client.get("/api/docs/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "/api/schema/")
        self.assertContains(response, "SwaggerUIBundle")
