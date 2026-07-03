from __future__ import annotations

import json
import logging
import os
import socket
import time
from urllib import error, parse, request

import redis


logger = logging.getLogger("invocation-finalizer")


class FinalizationError(RuntimeError):
    pass


class JsonInternalClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.token = token

    def post(self, path: str, payload: dict) -> dict:
        http_request = request.Request(
            f"{self.base_url}{path}",
            data=json.dumps(payload).encode("utf-8"),
            method="POST",
            headers={
                "Content-Type": "application/json",
                "X-Internal-Token": self.token,
            },
        )
        try:
            with request.urlopen(http_request, timeout=10) as response:
                return json.loads(response.read().decode("utf-8") or "{}")
        except (error.HTTPError, error.URLError, OSError) as exc:
            raise FinalizationError(str(exc)) from exc


class InvocationFinalizer:
    def __init__(
        self,
        redis_client,
        backend_client,
        orchestrator_client,
        *,
        stream: str = "orchestrator:v2:finalizations",
        group: str = "invocation-finalizers-v2",
        consumer: str | None = None,
    ):
        self.redis = redis_client
        self.backend = backend_client
        self.orchestrator = orchestrator_client
        self.stream = stream
        self.group = group
        self.consumer = consumer or socket.gethostname()

    def ensure_group(self):
        try:
            self.redis.xgroup_create(self.stream, self.group, id="0-0", mkstream=True)
        except redis.ResponseError as exc:
            if "BUSYGROUP" not in str(exc):
                raise

    def process_message(self, stream_id: str, fields: dict) -> bool:
        finalizer_started = time.monotonic()
        state = json.loads(fields["payload"])
        completion_payload = state.get("completion_payload") or {}
        request_id = completion_payload.get("request_id") or (
            state.get("payload") or {}
        ).get("request_id")
        completion_id = state["completion_id"]
        terminal_status = state.get("completion_status") or completion_payload.get(
            "status",
            "failed",
        )
        commit_started = time.monotonic()
        commit = self.backend.post(
            (
                f"/api/internal/invocations/{request_id}/staged-completions/"
                f"{parse.quote(completion_id, safe='')}/commit/"
            ),
            {
                "job_id": state["job_id"],
                "dispatch_attempt": state["dispatch_attempt"],
                "terminal_status": terminal_status,
                "completion_payload": completion_payload,
                "output_manifest": completion_payload.get("output_manifest") or [],
            },
        )
        backend_commit_ms = int((time.monotonic() - commit_started) * 1000)
        finalize_started = time.monotonic()
        final = self.orchestrator.post(
            f"/v2/jobs/{state['job_id']}/finalize",
            {
                "completion_id": completion_id,
                "status": terminal_status,
                "artifact_commit_id": commit["artifact_commit_id"],
            },
        )
        orchestrator_finalize_ms = int(
            (time.monotonic() - finalize_started) * 1000
        )
        if not final.get("finalized"):
            raise FinalizationError(
                f"orchestrator rejected finalization: {final.get('code', 'unknown')}"
            )
        self.redis.xack(self.stream, self.group, stream_id)
        logger.info(
            "invocation finalizer timing request_id=%s timings=%s",
            request_id,
            json.dumps(
                {
                    "backend_artifact_commit_ms": backend_commit_ms,
                    "orchestrator_finalize_ms": orchestrator_finalize_ms,
                    "finalizer_total_ms": int(
                        (time.monotonic() - finalizer_started) * 1000
                    ),
                },
                sort_keys=True,
            ),
        )
        return True

    def process_once(self, *, block_ms: int = 1000, count: int = 20) -> int:
        batches = self.redis.xreadgroup(
            self.group,
            self.consumer,
            {self.stream: ">"},
            count=count,
            block=block_ms,
        )
        processed = 0
        for _, messages in batches:
            for stream_id, fields in messages:
                self.process_message(stream_id, fields)
                processed += 1
        return processed

    def reclaim_once(self, *, min_idle_ms: int = 30_000, count: int = 20) -> int:
        response = self.redis.xautoclaim(
            self.stream,
            self.group,
            self.consumer,
            min_idle_ms,
            "0-0",
            count=count,
        )
        messages = response[1] if len(response) > 1 else []
        for stream_id, fields in messages:
            self.process_message(stream_id, fields)
        return len(messages)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    redis_client = redis.Redis.from_url(
        os.getenv("REDIS_URL", "redis://localhost:6379/0"),
        decode_responses=True,
    )
    token = os.getenv("WORKER_SHARED_SECRET", "change-me")
    finalizer = InvocationFinalizer(
        redis_client,
        JsonInternalClient(os.getenv("BACKEND_BASE_URL", "http://backend:8000"), token),
        JsonInternalClient(
            os.getenv("ORCHESTRATOR_BASE_URL", "http://orchestrator:8010"),
            token,
        ),
    )
    finalizer.ensure_group()
    while True:
        try:
            finalizer.reclaim_once()
            finalizer.process_once()
        except Exception:
            logger.exception("invocation finalization failed; event remains pending")
            time.sleep(1)


if __name__ == "__main__":
    main()
