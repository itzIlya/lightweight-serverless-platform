from __future__ import annotations

import json
from urllib import error, request


class BackendError(RuntimeError):
    pass


class BackendClient:
    def __init__(self, base_url: str, token: str, timeout_seconds: int = 10) -> None:
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.timeout_seconds = timeout_seconds

    def get_job(self, job_id: str) -> dict:
        url = f"{self.base_url}/api/internal/scheduler/jobs/{job_id}/"
        return self._get_json(url)

    def list_workers(self) -> list[dict]:
        url = f"{self.base_url}/api/internal/scheduler/workers/"
        return self._get_json(url)

    def dispatch_job(self, job_id: str, *, worker_name: str, queue_name: str) -> dict:
        url = f"{self.base_url}/api/internal/scheduler/jobs/{job_id}/dispatch/"
        return self._post_json(
            url,
            {
                "worker_name": worker_name,
                "queue_name": queue_name,
            },
        )

    def requeue_job(
        self,
        job_id: str,
        *,
        worker_name: str,
        reason: str,
        recovery: bool = False,
    ) -> dict:
        url = f"{self.base_url}/api/internal/scheduler/jobs/{job_id}/requeue/"
        return self._post_json(
            url,
            {
                "worker_name": worker_name,
                "reason": reason,
                "recovery": recovery,
            },
        )

    def expire_stale_workers(self, *, stale_after_seconds: int) -> dict:
        url = f"{self.base_url}/api/internal/scheduler/workers/expire-stale/"
        return self._post_json(
            url,
            {
                "stale_after_seconds": stale_after_seconds,
            },
        )

    def _get_json(self, url: str):
        http_request = request.Request(
            url,
            method="GET",
            headers={"X-Internal-Token": self.token},
        )
        return self._open_json(http_request)

    def _post_json(self, url: str, payload: dict):
        http_request = request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            method="POST",
            headers={
                "Content-Type": "application/json",
                "X-Internal-Token": self.token,
            },
        )
        return self._open_json(http_request)

    def _open_json(self, http_request):
        try:
            with request.urlopen(
                http_request,
                timeout=self.timeout_seconds,
            ) as response:
                body = response.read().decode("utf-8")
                return json.loads(body) if body else {}
        except error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise BackendError(
                f"backend request failed with HTTP {exc.code}: {body}"
            ) from exc
        except error.URLError as exc:
            raise BackendError(f"backend request failed: {exc}") from exc
