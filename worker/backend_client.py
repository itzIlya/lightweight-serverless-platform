from __future__ import annotations

import json
from pathlib import Path
import shutil
from urllib import error, request


class BackendReportError(RuntimeError):
    pass


class BackendClient:
    def __init__(self, base_url: str, token: str, timeout_seconds: int = 10) -> None:
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.timeout_seconds = timeout_seconds

    def report_invocation(self, request_id: str, payload: dict) -> dict:
        url = f"{self.base_url}/api/internal/invocations/{request_id}/report/"
        return self._json_request(url, payload)

    def list_invocation_inputs(self, request_id: str) -> dict:
        url = f"{self.base_url}/api/internal/invocations/{request_id}/inputs/"
        return self._get_json(url)

    def download_invocation_input(
        self,
        request_id: str,
        file_id: int,
        destination: Path,
    ) -> None:
        url = (
            f"{self.base_url}/api/internal/invocations/{request_id}/"
            f"inputs/{file_id}/download/"
        )
        http_request = request.Request(
            url,
            method="GET",
            headers={"X-Internal-Token": self.token},
        )
        try:
            with request.urlopen(
                http_request,
                timeout=self.timeout_seconds,
            ) as response:
                with destination.open("wb") as output:
                    shutil.copyfileobj(response, output)
        except error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise BackendReportError(
                f"input download failed with HTTP {exc.code}: {body}"
            ) from exc
        except error.URLError as exc:
            raise BackendReportError(f"input download failed: {exc}") from exc

    def report_build(self, build_request_id: str, payload: dict) -> dict:
        url = f"{self.base_url}/api/internal/builds/{build_request_id}/report/"
        return self._json_request(url, payload)

    def register_worker(self, payload: dict) -> dict:
        url = f"{self.base_url}/api/internal/workers/register/"
        return self._post_json(url, payload)

    def heartbeat_worker(self, payload: dict) -> dict:
        url = f"{self.base_url}/api/internal/workers/heartbeat/"
        return self._json_request(url, payload)

    def get_job(self, job_id: str) -> dict:
        url = f"{self.base_url}/api/internal/scheduler/jobs/{job_id}/"
        return self._get_json(url)

    def claim_job(self, job_id: str, payload: dict) -> dict:
        url = f"{self.base_url}/api/internal/jobs/{job_id}/claim/"
        return self._post_json(url, payload)

    def acquire_build_lease(self, build_request_id: str, payload: dict) -> dict:
        url = (
            f"{self.base_url}/api/internal/builds/{build_request_id}/"
            "lease/acquire/"
        )
        return self._post_json(url, payload)

    def release_build_lease(self, build_request_id: str, payload: dict) -> dict:
        url = (
            f"{self.base_url}/api/internal/builds/{build_request_id}/"
            "lease/release/"
        )
        return self._post_json(url, payload)

    def get_build_state(self, build_request_id: str) -> dict:
        url = f"{self.base_url}/api/internal/builds/{build_request_id}/state/"
        return self._get_json(url)

    def is_build_cancel_requested(self, build_request_id: str) -> bool:
        state = self.get_build_state(build_request_id)
        return state.get("status") in {"cancelling", "cancelled"} or bool(
            state.get("cancel_requested_at")
        )

    def download_build_source(
        self,
        build_request_id: str,
        destination: Path,
    ) -> None:
        url = f"{self.base_url}/api/internal/builds/{build_request_id}/source/"
        http_request = request.Request(
            url,
            method="GET",
            headers={"X-Internal-Token": self.token},
        )
        try:
            with request.urlopen(
                http_request,
                timeout=self.timeout_seconds,
            ) as response:
                with destination.open("wb") as output:
                    shutil.copyfileobj(response, output)
        except error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise BackendReportError(
                f"source download failed with HTTP {exc.code}: {body}"
            ) from exc
        except error.URLError as exc:
            raise BackendReportError(f"source download failed: {exc}") from exc

    def _json_request(self, url: str, payload: dict) -> dict:
        data = json.dumps(payload).encode("utf-8")
        http_request = request.Request(
            url,
            data=data,
            method="PATCH",
            headers={
                "Content-Type": "application/json",
                "X-Internal-Token": self.token,
            },
        )

        try:
            with request.urlopen(http_request, timeout=self.timeout_seconds) as response:
                body = response.read().decode("utf-8")
                return json.loads(body) if body else {}
        except error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise BackendReportError(
                f"backend report failed with HTTP {exc.code}: {body}"
            ) from exc
        except error.URLError as exc:
            raise BackendReportError(f"backend report failed: {exc}") from exc

    def _post_json(self, url: str, payload: dict) -> dict:
        data = json.dumps(payload).encode("utf-8")
        http_request = request.Request(
            url,
            data=data,
            method="POST",
            headers={
                "Content-Type": "application/json",
                "X-Internal-Token": self.token,
            },
        )

        try:
            with request.urlopen(http_request, timeout=self.timeout_seconds) as response:
                body = response.read().decode("utf-8")
                return json.loads(body) if body else {}
        except error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise BackendReportError(
                f"backend request failed with HTTP {exc.code}: {body}"
            ) from exc
        except error.URLError as exc:
            raise BackendReportError(f"backend request failed: {exc}") from exc

    def _get_json(self, url: str) -> dict:
        http_request = request.Request(
            url,
            method="GET",
            headers={"X-Internal-Token": self.token},
        )
        try:
            with request.urlopen(http_request, timeout=self.timeout_seconds) as response:
                body = response.read().decode("utf-8")
                return json.loads(body) if body else {}
        except error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise BackendReportError(
                f"backend request failed with HTTP {exc.code}: {body}"
            ) from exc
        except error.URLError as exc:
            raise BackendReportError(f"backend request failed: {exc}") from exc
