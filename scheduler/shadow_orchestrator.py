from __future__ import annotations

import json
import logging
import os
import socket
import time
from datetime import datetime, timezone

import redis

from backend_client import BackendClient
from orchestrator_state import V2JobStateStore
from orchestrator_workers import WorkerOperationalStateStore
from scheduler import (
    choose_worker,
    remember_local_invocation_dispatch,
    remember_local_warm_reservation,
    remember_recent_invocation_route,
    worker_queue_for_job,
    workers_with_queue_lengths,
)


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("shadow-orchestrator")


def timestamp_ms(value: str | None) -> int:
    if not value:
        return 0
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return int(parsed.timestamp() * 1000)


class ShadowOrchestrator:
    """Observe V1 events and model V2 decisions without production authority."""

    def __init__(
        self,
        redis_client,
        backend,
        *,
        stream_name: str = "orchestrator:events",
        group_name: str = "orchestrator-shadow-v1",
        consumer_name: str | None = None,
        state_prefix: str = "orchestrator:v2:shadow:job",
        decision_prefix: str = "orchestrator:v2:shadow:decision",
        worker_store=None,
    ):
        self.redis = redis_client
        self.backend = backend
        self.stream_name = stream_name
        self.group_name = group_name
        self.consumer_name = consumer_name or socket.gethostname()
        self.state = V2JobStateStore(redis_client, key_prefix=state_prefix)
        self.worker_store = worker_store or WorkerOperationalStateStore(redis_client)
        self.decision_prefix = decision_prefix.rstrip(":")
        self.round_robin_state: dict[str, int] = {}
        self.local_invocation_loads: dict[str, list[float]] = {}
        self.local_warm_reservations: dict[str, list[float]] = {}
        self.local_recent_invocation_routes: dict[str, dict] = {}

    def ensure_group(self) -> None:
        try:
            self.redis.xgroup_create(
                self.stream_name,
                self.group_name,
                id="0-0",
                mkstream=True,
            )
        except redis.ResponseError as exc:
            if "BUSYGROUP" not in str(exc):
                raise

    def decision_key(self, job_id: str) -> str:
        return f"{self.decision_prefix}:{job_id}"

    def process_event(
        self,
        stream_id: str,
        fields: dict,
        *,
        now_ms: int | None = None,
    ) -> dict:
        if fields.get("event_type") != "job.created":
            return {"decision": "ignored", "stream_id": stream_id}

        event_payload = json.loads(fields["payload"])
        job_id = str(event_payload["job_id"])
        existing = self.redis.hgetall(self.decision_key(job_id))
        if existing:
            return existing

        now_ms = int(time.time() * 1000) if now_ms is None else int(now_ms)
        available_at_ms = timestamp_ms(event_payload.get("available_at"))
        self.state.create_job(
            job_id,
            event_payload["job_type"],
            available_at_ms=available_at_ms,
            now_ms=now_ms,
        )

        job = {
            "job_id": job_id,
            "type": event_payload["job_type"],
            "status": event_payload.get("status", "queued"),
            "available_at": event_payload.get("available_at"),
            "payload": event_payload.get("payload") or {},
        }
        workers = workers_with_queue_lengths(
            self.worker_store.list_online_workers(now_ms=now_ms),
            self.redis,
        )
        worker = choose_worker(
            workers,
            job,
            local_invocation_loads=self.local_invocation_loads,
            local_warm_reservations=self.local_warm_reservations,
            local_recent_invocation_routes=self.local_recent_invocation_routes,
            round_robin_state=self.round_robin_state,
        )

        queue_name = ""
        selected_worker = ""
        if worker is None:
            decision = "no_worker"
            shadow_status = "queued"
        else:
            selected_worker = worker["name"]
            queue_name = worker_queue_for_job(worker, job)
            transition = self.state.dispatch(
                job_id,
                worker_name=selected_worker,
                queue_name=queue_name,
                now_ms=now_ms,
            )
            decision = "dispatch" if transition.accepted else transition.code
            shadow_status = transition.status
            if transition.accepted:
                remember_local_warm_reservation(
                    job,
                    worker,
                    local_warm_reservations=self.local_warm_reservations,
                    local_load_ttl_seconds=10.0,
                )
                remember_local_invocation_dispatch(
                    job,
                    worker,
                    local_invocation_loads=self.local_invocation_loads,
                    local_load_ttl_seconds=10.0,
                )
                remember_recent_invocation_route(
                    job,
                    worker,
                    local_recent_invocation_routes=self.local_recent_invocation_routes,
                    local_load_ttl_seconds=10.0,
                )

        comparison = {
            "event_id": str(fields.get("event_id", "")),
            "stream_id": str(stream_id),
            "job_id": job_id,
            "job_type": event_payload["job_type"],
            "v1_coordination_version": str(
                event_payload.get("coordination_version", "")
            ),
            "v1_status": str(event_payload.get("status", "")),
            "shadow_status": shadow_status,
            "decision": decision,
            "selected_worker": selected_worker,
            "queue_name": queue_name,
            "compared_at_ms": str(now_ms),
        }
        self.redis.hset(self.decision_key(job_id), mapping=comparison)
        return comparison

    def run_once(self, *, block_ms: int = 1000, count: int = 20) -> int:
        batches = self.redis.xreadgroup(
            self.group_name,
            self.consumer_name,
            {self.stream_name: ">"},
            count=count,
            block=block_ms,
        )
        processed = 0
        for _, messages in batches:
            for stream_id, fields in messages:
                self.process_event(stream_id, fields)
                self.redis.xack(self.stream_name, self.group_name, stream_id)
                processed += 1
        return processed


def main() -> None:
    client = redis.Redis.from_url(
        os.getenv("REDIS_URL", "redis://localhost:6379/0"),
        decode_responses=True,
    )
    backend = BackendClient(
        os.getenv("BACKEND_BASE_URL", "http://localhost:8000"),
        os.getenv("WORKER_SHARED_SECRET", "change-me"),
    )
    orchestrator = ShadowOrchestrator(
        client,
        backend,
        stream_name=os.getenv("ORCHESTRATOR_EVENT_STREAM", "orchestrator:events"),
        group_name=os.getenv("ORCHESTRATOR_SHADOW_GROUP", "orchestrator-shadow-v1"),
    )
    orchestrator.ensure_group()
    logger.info("shadow orchestrator started stream=%s", orchestrator.stream_name)
    while True:
        try:
            orchestrator.run_once()
        except Exception:
            logger.exception("shadow orchestrator cycle failed")
            time.sleep(1)


if __name__ == "__main__":
    main()
