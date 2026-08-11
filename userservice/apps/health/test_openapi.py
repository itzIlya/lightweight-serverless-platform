from django.test import TestCase


class UserserviceOpenAPITests(TestCase):
    def test_openapi_schema_is_public_and_documents_auth_contract(self):
        response = self.client.get("/api/schema/")

        self.assertEqual(response.status_code, 200)
        schema = response.json()
        self.assertEqual(schema["openapi"], "3.0.3")
        self.assertIn("/api/auth/register/", schema["paths"])
        self.assertIn("/api/auth/token/refresh/", schema["paths"])
        self.assertIn("/api/auth/logout/", schema["paths"])
        self.assertIn("/api/auth/jwks/", schema["paths"])
        self.assertIn("BearerAuth", schema["components"]["securitySchemes"])

    def test_swagger_docs_page_points_to_schema(self):
        response = self.client.get("/api/docs/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "/api/schema/")
        self.assertContains(response, "SwaggerUIBundle")
