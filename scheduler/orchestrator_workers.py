from __future__ import annotations

import json
import time


RECORD_HEARTBEAT_SCRIPT = r"""
redis.call('HSET', KEYS[1],
    'name', ARGV[1],
    'hostname', ARGV[2],
    'status', ARGV[16],
    'max_concurrency', ARGV[3],
    'max_build_concurrency', ARGV[4],
    'max_invocation_concurrency', ARGV[5],
    'active_jobs', ARGV[6],
    'active_builds', ARGV[7],
    'active_invocations', ARGV[8],
    'queue_name', ARGV[9],
    'invocation_queue_name', ARGV[10],
    'build_queue_name', ARGV[11],
    'processing_queue_name', ARGV[12],
    'metadata', ARGV[13],
    'last_seen_ms', ARGV[14],
    'lease_expires_at_ms', ARGV[15])
if ARGV[16] == 'online' then
    redis.call('ZADD', KEYS[2], ARGV[15], ARGV[1])
else
    redis.call('ZREM', KEYS[2], ARGV[1])
end
return ARGV[15]
"""


EXPIRE_STALE_SCRIPT = r"""
local candidates = redis.call('ZRANGEBYSCORE', KEYS[1], '-inf', ARGV[1])
local expired = {}
for _, name in ipairs(candidates) do
    local worker_key = ARGV[2] .. ':' .. name
    local lease = tonumber(redis.call('HGET', worker_key, 'lease_expires_at_ms') or '0')
    if lease <= tonumber(ARGV[1]) then
        redis.call('HSET', worker_key, 'status', 'offline')
        redis.call('ZREM', KEYS[1], name)
        table.insert(expired, name)
    end
end
return expired
"""


class WorkerOperationalStateStore:
    def __init__(
        self,
        redis_client,
        *,
        key_prefix: str = "orchestrator:v2:worker",
        lease_key: str = "orchestrator:v2:worker-leases",
        lease_ttl_ms: int = 30_000,
    ):
        self.redis = redis_client
        self.key_prefix = key_prefix.rstrip(":")
        self.lease_key = lease_key
        self.lease_ttl_ms = int(lease_ttl_ms)

    def key(self, worker_name: str) -> str:
        return f"{self.key_prefix}:{worker_name}"

    def record_heartbeat(self, payload: dict, *, now_ms: int | None = None) -> int:
        now_ms = _now_ms(now_ms)
        lease_expires_at_ms = now_ms + self.lease_ttl_ms
        metadata = payload.get("metadata") or {}
        return int(
            self.redis.eval(
                RECORD_HEARTBEAT_SCRIPT,
                2,
                self.key(payload["name"]),
                self.lease_key,
                payload["name"],
                payload.get("hostname", ""),
                int(payload.get("max_concurrency", 1)),
                int(payload.get("max_build_concurrency", 1)),
                int(payload.get("max_invocation_concurrency", 1)),
                int(payload.get("active_jobs", 0)),
                int(payload.get("active_builds", 0)),
                int(payload.get("active_invocations", 0)),
                payload.get("queue_name", ""),
                payload.get("invocation_queue_name", ""),
                payload.get("build_queue_name", ""),
                payload.get("processing_queue_name", ""),
                json.dumps(metadata, separators=(",", ":"), sort_keys=True),
                now_ms,
                lease_expires_at_ms,
                payload.get("status", "online"),
            )
        )

    def expire_stale(self, *, now_ms: int | None = None) -> list[str]:
        values = self.redis.eval(
            EXPIRE_STALE_SCRIPT,
            1,
            self.lease_key,
            _now_ms(now_ms),
            self.key_prefix,
        )
        return [_text(value) for value in values]

    def get_worker(self, worker_name: str) -> dict:
        return _normalize_worker(self.redis.hgetall(self.key(worker_name)))

    def list_online_workers(self, *, now_ms: int | None = None) -> list[dict]:
        now_ms = _now_ms(now_ms)
        self.expire_stale(now_ms=now_ms)
        names = self.redis.zrangebyscore(self.lease_key, now_ms + 1, "+inf")
        workers = [self.get_worker(_text(name)) for name in names]
        return sorted(
            [worker for worker in workers if worker.get("status") == "online"],
            key=lambda worker: worker["name"],
        )

    def delete_worker(self, worker_name: str) -> None:
        pipe = self.redis.pipeline()
        pipe.delete(self.key(worker_name))
        pipe.zrem(self.lease_key, worker_name)
        pipe.execute()


def _normalize_worker(values: dict) -> dict:
    normalized = {_text(key): _text(value) for key, value in values.items()}
    for field in {
        "max_concurrency",
        "max_build_concurrency",
        "max_invocation_concurrency",
        "active_jobs",
        "active_builds",
        "active_invocations",
        "last_seen_ms",
        "lease_expires_at_ms",
    }:
        if field in normalized:
            normalized[field] = int(normalized[field])
    metadata = json.loads(normalized.pop("metadata", "{}"))
    metadata.update(
        {
            "active_jobs": normalized.pop("active_jobs", 0),
            "active_builds": normalized.pop("active_builds", 0),
            "active_invocations": normalized.pop("active_invocations", 0),
            "max_invocation_concurrency": normalized.get(
                "max_invocation_concurrency",
                normalized.get("max_concurrency", 1),
            ),
        }
    )
    normalized["metadata"] = metadata
    return normalized


def _now_ms(value: int | None) -> int:
    return int(time.time() * 1000) if value is None else int(value)


def _text(value) -> str:
    return value.decode("utf-8") if isinstance(value, bytes) else str(value)
