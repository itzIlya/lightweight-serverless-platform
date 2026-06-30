from __future__ import annotations

import json
import logging
import os
import socket
import threading
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

import redis

from orchestrator_state import V2JobStateStore, V2JobStatus
from orchestrator_workers import WorkerOperationalStateStore
from scheduler import choose_worker, workers_with_queue_lengths


logger = logging.getLogger("production-orchestrator")


DISPATCH_TO_STREAM_SCRIPT = r"""
if redis.call('EXISTS', KEYS[1]) == 0 then
    return {'missing', '', '0', ''}
end
local status = redis.call('HGET', KEYS[1], 'status') or ''
if status ~= 'queued' then
    return {'invalid_state', status, '0', ''}
end
local available = tonumber(redis.call('HGET', KEYS[1], 'available_at_ms') or '0')
if available > tonumber(ARGV[4]) then
    return {'not_available', status, '0', ''}
end
local attempt = redis.call('HINCRBY', KEYS[1], 'dispatch_attempt', 1)
local image_ref = ''
if ARGV[5] ~= '' then
    image_ref = ARGV[5] .. '-d' .. tostring(attempt)
end
redis.call('HSET', KEYS[1],
    'status', 'dispatched',
    'assigned_worker', ARGV[1],
    'worker_stream', KEYS[3],
    'effective_image_ref', image_ref,
    'lease_expires_at_ms', ARGV[6],
    'updated_at_ms', ARGV[4])
local stream_id = redis.call('XADD', KEYS[3], '*',
    'job_id', ARGV[2],
    'dispatch_attempt', tostring(attempt),
    'job_type', ARGV[3])
redis.call('HSET', KEYS[1], 'delivery_stream_id', stream_id)
redis.call('ZREM', KEYS[2], ARGV[2])
return {'ok', 'dispatched', tostring(attempt), stream_id}
"""


EMIT_PROJECTION_SCRIPT = r"""
local existing = redis.call('HGET', KEYS[1], ARGV[1])
if existing then
    return existing
end
local stream_id = redis.call('XADD', KEYS[2], '*',
    'event_type', ARGV[2],
    'job_id', ARGV[3],
    'payload', ARGV[4])
redis.call('HSET', KEYS[1], ARGV[1], stream_id)
return stream_id
"""


class ProductionOrchestrator:
    def __init__(
        self,
        redis_client,
        *,
        event_stream: str = "orchestrator:events",
        event_group: str = "orchestrator-v2-production",
        consumer_name: str | None = None,
        projection_stream: str = "orchestrator:v2:projections",
        ready_key: str = "orchestrator:v2:ready",
        lease_key: str = "orchestrator:v2:job-leases",
        orphan_stream: str = "orchestrator:v2:orphan-images",
        lease_ttl_ms: int = 30_000,
        state_prefix: str = "orchestrator:v2:job",
        worker_store=None,
    ):
        self.redis = redis_client
        self.event_stream = event_stream
        self.event_group = event_group
        self.consumer_name = consumer_name or socket.gethostname()
        self.projection_stream = projection_stream
        self.ready_key = ready_key
        self.lease_key = lease_key
        self.orphan_stream = orphan_stream
        self.lease_ttl_ms = int(lease_ttl_ms)
        self.state = V2JobStateStore(redis_client, key_prefix=state_prefix)
        self.workers = worker_store or WorkerOperationalStateStore(redis_client)
        self.round_robin_state: dict[str, int] = {}
        self.recent_invocations: dict[str, dict] = {}
        self.local_invocation_loads: dict[str, list[float]] = {}

    def ensure_event_group(self) -> None:
        try:
            self.redis.xgroup_create(
                self.event_stream,
                self.event_group,
                id="0-0",
                mkstream=True,
            )
        except redis.ResponseError as exc:
            if "BUSYGROUP" not in str(exc):
                raise

    def process_creation_event(self, stream_id: str, fields: dict) -> bool:
        if fields.get("event_type") != "job.created":
            return False
        event = json.loads(fields["payload"])
        if int(event.get("coordination_version", 1)) != 2:
            return False
        job_id = str(event["job_id"])
        available_at_ms = timestamp_ms(event.get("available_at"))
        self.state.create_job(
            job_id,
            event["job_type"],
            available_at_ms=available_at_ms,
        )
        self.redis.hset(
            self.state.key(job_id),
            mapping={
                "payload": json.dumps(
                    event.get("payload") or {},
                    separators=(",", ":"),
                    sort_keys=True,
                ),
                "source_event_id": fields.get("event_id", ""),
                "source_stream_id": stream_id,
                "max_recovery_attempts": int(event.get("max_recovery_attempts", 3)),
            },
        )
        self.redis.zadd(self.ready_key, {job_id: available_at_ms})
        return True

    def consume_events_once(self, *, block_ms: int = 1, count: int = 20) -> int:
        batches = self.redis.xreadgroup(
            self.event_group,
            self.consumer_name,
            {self.event_stream: ">"},
            count=count,
            block=block_ms,
        )
        processed = 0
        for _, messages in batches:
            for stream_id, fields in messages:
                self.process_creation_event(stream_id, fields)
                self.redis.xack(self.event_stream, self.event_group, stream_id)
                processed += 1
        return processed

    def reclaim_events_once(self, *, min_idle_ms: int = 30_000, count: int = 20) -> int:
        response = self.redis.xautoclaim(
            self.event_stream,
            self.event_group,
            self.consumer_name,
            min_idle_ms,
            "0-0",
            count=count,
        )
        messages = response[1] if len(response) > 1 else []
        for stream_id, fields in messages:
            self.process_creation_event(stream_id, fields)
            self.redis.xack(self.event_stream, self.event_group, stream_id)
        return len(messages)

    def dispatch_ready_once(self, *, now_ms: int | None = None, limit: int = 20) -> int:
        now_ms = current_ms(now_ms)
        job_ids = self.redis.zrangebyscore(self.ready_key, "-inf", now_ms, start=0, num=limit)
        workers = workers_with_queue_lengths(
            self.workers.list_online_workers(now_ms=now_ms),
            self.redis,
        )
        dispatched = 0
        for job_id in job_ids:
            job = self.state.get_job(job_id)
            payload = job.get("payload") or {}
            choice = choose_worker(
                workers,
                {"payload": payload},
                recent_invocations=self.recent_invocations,
                local_invocation_loads=self.local_invocation_loads,
                round_robin_state=self.round_robin_state,
            )
            if choice is None:
                continue
            worker_stream = self.worker_stream(choice["name"], job["job_type"])
            response = self.redis.eval(
                DISPATCH_TO_STREAM_SCRIPT,
                3,
                self.state.key(job_id),
                self.ready_key,
                worker_stream,
                choice["name"],
                job_id,
                job["job_type"],
                now_ms,
                payload.get("image_ref", "") if job["job_type"] == "build" else "",
                now_ms + self.lease_ttl_ms,
            )
            if text(response[0]) == "ok":
                self.ensure_worker_group(worker_stream)
                self.redis.zadd(self.lease_key, {job_id: now_ms + self.lease_ttl_ms})
                dispatched += 1
                self.emit_projection(job_id, "job.dispatched")
        return dispatched

    def claim_job(
        self,
        job_id: str,
        *,
        worker_name: str,
        dispatch_attempt: int,
        now_ms: int | None = None,
    ) -> dict:
        now_ms = current_ms(now_ms)
        result = self.state.claim(
            job_id,
            worker_name=worker_name,
            dispatch_attempt=dispatch_attempt,
            lease_expires_at_ms=now_ms + self.lease_ttl_ms,
            now_ms=now_ms,
        )
        if not result.accepted:
            return transition_payload(result, claimed=False)
        self.redis.zadd(self.lease_key, {job_id: now_ms + self.lease_ttl_ms})
        self.emit_projection(job_id, "job.running")
        job = self.state.get_job(job_id)
        payload = dict(job.get("payload") or {})
        payload.update(
            {
                "job_id": job_id,
                "dispatch_attempt": result.dispatch_attempt,
                "assigned_worker": worker_name,
            }
        )
        if job.get("effective_image_ref"):
            payload["image_ref"] = job["effective_image_ref"]
        return {
            **transition_payload(result, claimed=True),
            "lease_expires_at_ms": now_ms + self.lease_ttl_ms,
            "payload": payload,
        }

    def renew_lease(
        self,
        job_id: str,
        *,
        worker_name: str,
        dispatch_attempt: int,
        now_ms: int | None = None,
    ) -> dict:
        now_ms = current_ms(now_ms)
        expires = now_ms + self.lease_ttl_ms
        result = self.state.renew_lease(
            job_id,
            worker_name=worker_name,
            dispatch_attempt=dispatch_attempt,
            lease_expires_at_ms=expires,
            now_ms=now_ms,
        )
        if result.accepted:
            self.redis.zadd(self.lease_key, {job_id: expires})
        return {**transition_payload(result), "lease_expires_at_ms": expires}

    def complete_job(
        self,
        job_id: str,
        *,
        worker_name: str,
        dispatch_attempt: int,
        completion_id: str,
        status: str,
        completion_payload: dict,
        artifact_commit_id: str = "",
        now_ms: int | None = None,
    ) -> dict:
        now_ms = current_ms(now_ms)
        begun = self.state.begin_finalization(
            job_id,
            worker_name=worker_name,
            dispatch_attempt=dispatch_attempt,
            completion_id=completion_id,
            completion_payload=completion_payload,
            now_ms=now_ms,
        )
        if not begun.accepted and begun.code != "terminal":
            return transition_payload(begun, completed=False)
        finished = self.state.finish_finalization(
            job_id,
            completion_id=completion_id,
            terminal_status=status,
            artifact_commit_id=artifact_commit_id,
            now_ms=now_ms,
        )
        if finished.accepted:
            self.redis.zrem(self.lease_key, job_id)
            self.ack_delivery(self.state.get_job(job_id))
            self.emit_projection(job_id, f"job.{status}")
        return transition_payload(finished, completed=finished.accepted)

    def recover_expired_once(self, *, now_ms: int | None = None, limit: int = 20) -> int:
        now_ms = current_ms(now_ms)
        job_ids = self.redis.zrangebyscore(self.lease_key, "-inf", now_ms, start=0, num=limit)
        recovered = 0
        for job_id in job_ids:
            job = self.state.get_job(job_id)
            if job.get("status") not in {V2JobStatus.DISPATCHED, V2JobStatus.RUNNING}:
                self.redis.zrem(self.lease_key, job_id)
                continue
            attempt = int(job["dispatch_attempt"])
            max_recoveries = int(job.get("max_recovery_attempts", 3))
            if int(job.get("recovery_count", 0)) >= max_recoveries:
                result = self.state.dead_letter(
                    job_id,
                    dispatch_attempt=attempt,
                    reason=f"Exceeded {max_recoveries} V2 recovery attempt(s).",
                    now_ms=now_ms,
                )
                if result.accepted:
                    self.ack_delivery(job)
                    self.redis.zrem(self.lease_key, job_id)
                    self.emit_orphan(job, attempt)
                    self.emit_projection(job_id, "job.dead_lettered")
                    recovered += 1
                continue
            result = self.state.requeue(
                job_id,
                dispatch_attempt=attempt,
                available_at_ms=now_ms,
                reason="V2 worker lease expired.",
                now_ms=now_ms,
            )
            if not result.accepted:
                continue
            self.ack_delivery(job)
            self.redis.zrem(self.lease_key, job_id)
            self.redis.zadd(self.ready_key, {job_id: now_ms})
            self.emit_orphan(job, attempt)
            self.emit_projection(job_id, "job.requeued")
            recovered += 1
        return recovered

    def emit_projection(self, job_id: str, event_type: str) -> str:
        job = self.state.get_job(job_id)
        marker = f"projection:{event_type}:{job.get('dispatch_attempt', 0)}"
        payload = json.dumps(job, separators=(",", ":"), sort_keys=True)
        return text(
            self.redis.eval(
                EMIT_PROJECTION_SCRIPT,
                2,
                self.state.key(job_id),
                self.projection_stream,
                marker,
                event_type,
                job_id,
                payload,
            )
        )

    @staticmethod
    def worker_stream(worker_name: str, job_type: str) -> str:
        suffix = "builds" if job_type == "build" else "invocations"
        return f"worker:{worker_name}:v2:{suffix}"

    def ensure_worker_group(self, stream: str) -> None:
        try:
            self.redis.xgroup_create(stream, "v2-workers", id="0-0", mkstream=True)
        except redis.ResponseError as exc:
            if "BUSYGROUP" not in str(exc):
                raise

    def ack_delivery(self, job: dict) -> None:
        stream = job.get("worker_stream")
        stream_id = job.get("delivery_stream_id")
        if not stream or not stream_id:
            return
        try:
            self.redis.xack(stream, "v2-workers", stream_id)
        except redis.ResponseError as exc:
            if "NOGROUP" not in str(exc):
                raise

    def emit_orphan(self, job: dict, dispatch_attempt: int) -> None:
        if job.get("job_type") == "build" and job.get("effective_image_ref"):
            self.redis.xadd(
                self.orphan_stream,
                {
                    "job_id": job["job_id"],
                    "dispatch_attempt": dispatch_attempt,
                    "image_ref": job["effective_image_ref"],
                },
            )


def timestamp_ms(value: str | None) -> int:
    if not value:
        return 0
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return int(parsed.timestamp() * 1000)


def current_ms(value: int | None = None) -> int:
    return int(time.time() * 1000) if value is None else int(value)


def text(value) -> str:
    return value.decode("utf-8") if isinstance(value, bytes) else str(value)


def transition_payload(result, **extra) -> dict:
    return {
        "accepted": result.accepted,
        "code": result.code,
        "status": result.status,
        "dispatch_attempt": result.dispatch_attempt,
        "idempotent": result.idempotent,
        **extra,
    }


class OrchestratorRequestHandler(BaseHTTPRequestHandler):
    orchestrator: ProductionOrchestrator
    internal_token: str

    def do_GET(self):
        if self.path == "/health/":
            return self.respond(200, {"status": "ok"})
        return self.respond(404, {"detail": "Not found."})

    def do_POST(self):
        if self.headers.get("X-Internal-Token", "") != self.internal_token:
            return self.respond(401, {"detail": "Unauthorized."})
        parts = urlparse(self.path).path.strip("/").split("/")
        if len(parts) != 4 or parts[:2] != ["v2", "jobs"]:
            return self.respond(404, {"detail": "Not found."})
        job_id, operation = parts[2], parts[3]
        body = self.read_json()
        try:
            if operation == "claim":
                result = self.orchestrator.claim_job(job_id, **body)
            elif operation == "renew":
                result = self.orchestrator.renew_lease(job_id, **body)
            elif operation == "complete":
                result = self.orchestrator.complete_job(job_id, **body)
            else:
                return self.respond(404, {"detail": "Not found."})
        except (KeyError, TypeError, ValueError) as exc:
            return self.respond(400, {"detail": str(exc)})
        return self.respond(200, result)

    def read_json(self) -> dict:
        length = int(self.headers.get("Content-Length", "0"))
        return json.loads(self.rfile.read(length) or b"{}")

    def respond(self, status: int, payload: dict):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        logger.info("orchestrator api " + format, *args)


def serve_api(orchestrator: ProductionOrchestrator, host: str, port: int, token: str):
    handler = type(
        "ConfiguredOrchestratorHandler",
        (OrchestratorRequestHandler,),
        {"orchestrator": orchestrator, "internal_token": token},
    )
    server = ThreadingHTTPServer((host, port), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    client = redis.Redis.from_url(
        os.getenv("REDIS_URL", "redis://localhost:6379/0"),
        decode_responses=True,
    )
    orchestrator = ProductionOrchestrator(
        client,
        lease_ttl_ms=int(os.getenv("ORCHESTRATOR_JOB_LEASE_SECONDS", "30")) * 1000,
    )
    orchestrator.ensure_event_group()
    serve_api(
        orchestrator,
        "0.0.0.0",
        int(os.getenv("ORCHESTRATOR_PORT", "8010")),
        os.getenv("WORKER_SHARED_SECRET", "change-me"),
    )
    logger.info("production V2 orchestrator started")
    while True:
        try:
            orchestrator.reclaim_events_once()
            orchestrator.consume_events_once(block_ms=100)
            orchestrator.recover_expired_once()
            orchestrator.dispatch_ready_once()
        except Exception:
            logger.exception("production orchestrator cycle failed")
            time.sleep(1)


if __name__ == "__main__":
    main()
