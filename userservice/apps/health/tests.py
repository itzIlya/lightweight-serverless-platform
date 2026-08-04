from django.test import TestCase


class UserserviceMetricsTests(TestCase):
    def test_metrics_endpoint_returns_prometheus_text(self):
        response = self.client.get("/metrics/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.headers["Content-Type"],
            "text/plain; version=0.0.4; charset=utf-8",
        )
        body = response.content.decode()
        self.assertIn("serverless_userservice_up 1", body)
        self.assertIn("serverless_userservice_users_total", body)
        self.assertIn("serverless_userservice_verified_accounts_total", body)
