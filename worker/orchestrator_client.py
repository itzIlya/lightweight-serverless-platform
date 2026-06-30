from __future__ import annotations

import json
import time
from urllib import error, request


class OrchestratorError(RuntimeError):
    pass


class OrchestratorClient:
    def __init__(
        self,
        base_url: str,
        token: str,
        *,
        timeout_seconds: int = 10,
        retries: int = 2,
    ):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.timeout_seconds = timeout_seconds
        self.retries = retries

    def claim_job(self, job_id: str, payload: dict) -> dict:
        return self._post(f"/v2/jobs/{job_id}/claim", payload)

    def renew_lease(self, job_id: str, payload: dict) -> dict:
        return self._post(f"/v2/jobs/{job_id}/renew", payload)

    def complete_job(self, job_id: str, payload: dict) -> dict:
        return self._post(f"/v2/jobs/{job_id}/complete", payload)

    def _post(self, path: str, payload: dict) -> dict:
        body = json.dumps(payload).encode("utf-8")
        last_error = None
        for retry in range(self.retries + 1):
            http_request = request.Request(
                f"{self.base_url}{path}",
                data=body,
                method="POST",
                headers={
                    "Content-Type": "application/json",
                    "X-Internal-Token": self.token,
                },
            )
            try:
                with request.urlopen(http_request, timeout=self.timeout_seconds) as response:
                    return json.loads(response.read().decode("utf-8") or "{}")
            except error.HTTPError as exc:
                detail = exc.read().decode("utf-8", errors="replace")
                raise OrchestratorError(
                    f"orchestrator returned HTTP {exc.code}: {detail}"
                ) from exc
            except (error.URLError, OSError) as exc:
                last_error = exc
                if retry < self.retries:
                    time.sleep(0.1 * (retry + 1))
        raise OrchestratorError(f"orchestrator request failed: {last_error}")
