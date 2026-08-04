from django.test import TestCase


class BackendMetricsTests(TestCase):
    def test_metrics_endpoint_returns_prometheus_text(self):
        response = self.client.get("/metrics/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.headers["Content-Type"],
            "text/plain; version=0.0.4; charset=utf-8",
        )
        body = response.content.decode()
        self.assertIn("serverless_backend_up 1", body)
        self.assertIn("serverless_functions_total", body)
        self.assertIn("serverless_outbox_unpublished_total", body)
