from __future__ import annotations

from dataclasses import dataclass
import json
import time


class V2JobStatus:
    QUEUED = "queued"
    DISPATCHED = "dispatched"
    RUNNING = "running"
    FINALIZING = "finalizing"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"
    DEAD_LETTERED = "dead_lettered"

    TERMINAL = {SUCCEEDED, FAILED, CANCELLED, DEAD_LETTERED}


@dataclass(frozen=True)
class TransitionResult:
    accepted: bool
    code: str
    status: str
    dispatch_attempt: int | None = None
    idempotent: bool = False


CREATE_JOB_SCRIPT = r"""
if redis.call('EXISTS', KEYS[1]) == 1 then
    return {'exists', redis.call('HGET', KEYS[1], 'status') or ''}
end
redis.call('HSET', KEYS[1],
    'job_id', ARGV[1],
    'job_type', ARGV[2],
    'coordination_version', '2',
    'status', 'queued',
    'dispatch_attempt', '0',
    'recovery_count', '0',
    'available_at_ms', ARGV[3],
    'created_at_ms', ARGV[4],
    'updated_at_ms', ARGV[4])
return {'ok', 'queued', '0'}
"""


DISPATCH_SCRIPT = r"""
if redis.call('EXISTS', KEYS[1]) == 0 then
    return {'missing', ''}
end
local status = redis.call('HGET', KEYS[1], 'status') or ''
if status ~= 'queued' then
    return {'invalid_state', status}
end
local available = tonumber(redis.call('HGET', KEYS[1], 'available_at_ms') or '0')
if available > tonumber(ARGV[3]) then
    return {'not_available', status}
end
local attempt = redis.call('HINCRBY', KEYS[1], 'dispatch_attempt', 1)
redis.call('HSET', KEYS[1],
    'status', 'dispatched',
    'assigned_worker', ARGV[1],
    'worker_queue', ARGV[2],
    'updated_at_ms', ARGV[3])
return {'ok', 'dispatched', tostring(attempt)}
"""


CLAIM_SCRIPT = r"""
if redis.call('EXISTS', KEYS[1]) == 0 then
    return {'missing', ''}
end
local status = redis.call('HGET', KEYS[1], 'status') or ''
if status == 'succeeded' or status == 'failed' or status == 'cancelled' or status == 'dead_lettered' then
    return {'terminal', status}
end
local worker = redis.call('HGET', KEYS[1], 'assigned_worker') or ''
local attempt = tonumber(redis.call('HGET', KEYS[1], 'dispatch_attempt') or '0')
if worker ~= ARGV[1] or attempt ~= tonumber(ARGV[2]) then
    return {'stale', status, tostring(attempt)}
end
if status == 'running' then
    return {'already', status, tostring(attempt)}
end
if status ~= 'dispatched' then
    return {'invalid_state', status, tostring(attempt)}
end
redis.call('HSET', KEYS[1],
    'status', 'running',
    'lease_expires_at_ms', ARGV[3],
    'updated_at_ms', ARGV[4])
return {'ok', 'running', tostring(attempt)}
"""


RENEW_LEASE_SCRIPT = r"""
if redis.call('EXISTS', KEYS[1]) == 0 then
    return {'missing', ''}
end
local status = redis.call('HGET', KEYS[1], 'status') or ''
local worker = redis.call('HGET', KEYS[1], 'assigned_worker') or ''
local attempt = tonumber(redis.call('HGET', KEYS[1], 'dispatch_attempt') or '0')
if status ~= 'running' then
    return {'invalid_state', status, tostring(attempt)}
end
if worker ~= ARGV[1] or attempt ~= tonumber(ARGV[2]) then
    return {'stale', status, tostring(attempt)}
end
redis.call('HSET', KEYS[1],
    'lease_expires_at_ms', ARGV[3],
    'updated_at_ms', ARGV[4])
return {'ok', status, tostring(attempt)}
"""


BEGIN_FINALIZATION_SCRIPT = r"""
if redis.call('EXISTS', KEYS[1]) == 0 then
    return {'missing', ''}
end
local status = redis.call('HGET', KEYS[1], 'status') or ''
local attempt = tonumber(redis.call('HGET', KEYS[1], 'dispatch_attempt') or '0')
if status == 'finalizing' then
    local completion = redis.call('HGET', KEYS[1], 'completion_id') or ''
    if completion == ARGV[3] then
        return {'already', status, tostring(attempt)}
    end
    return {'completion_conflict', status, tostring(attempt)}
end
if status == 'succeeded' or status == 'failed' or status == 'cancelled' or status == 'dead_lettered' then
    return {'terminal', status, tostring(attempt)}
end
if status ~= 'running' then
    return {'invalid_state', status, tostring(attempt)}
end
local worker = redis.call('HGET', KEYS[1], 'assigned_worker') or ''
if worker ~= ARGV[1] or attempt ~= tonumber(ARGV[2]) then
    return {'stale', status, tostring(attempt)}
end
redis.call('HSET', KEYS[1],
    'status', 'finalizing',
    'completion_id', ARGV[3],
    'completion_payload', ARGV[4],
    'updated_at_ms', ARGV[5])
redis.call('HDEL', KEYS[1], 'lease_expires_at_ms')
return {'ok', 'finalizing', tostring(attempt)}
"""


FINISH_FINALIZATION_SCRIPT = r"""
if redis.call('EXISTS', KEYS[1]) == 0 then
    return {'missing', ''}
end
local status = redis.call('HGET', KEYS[1], 'status') or ''
local attempt = tonumber(redis.call('HGET', KEYS[1], 'dispatch_attempt') or '0')
local completion = redis.call('HGET', KEYS[1], 'completion_id') or ''
if status == ARGV[2] and completion == ARGV[1] then
    return {'already', status, tostring(attempt)}
end
if status ~= 'finalizing' then
    return {'invalid_state', status, tostring(attempt)}
end
if completion ~= ARGV[1] then
    return {'completion_conflict', status, tostring(attempt)}
end
if ARGV[2] == 'succeeded' and ARGV[3] == '' then
    return {'missing_artifact_commit', status, tostring(attempt)}
end
redis.call('HSET', KEYS[1],
    'status', ARGV[2],
    'artifact_commit_id', ARGV[3],
    'finished_at_ms', ARGV[4],
    'updated_at_ms', ARGV[4])
return {'ok', ARGV[2], tostring(attempt)}
"""


REQUEUE_SCRIPT = r"""
if redis.call('EXISTS', KEYS[1]) == 0 then
    return {'missing', ''}
end
local status = redis.call('HGET', KEYS[1], 'status') or ''
local attempt = tonumber(redis.call('HGET', KEYS[1], 'dispatch_attempt') or '0')
if status == 'succeeded' or status == 'failed' or status == 'cancelled' or status == 'dead_lettered' then
    return {'terminal', status, tostring(attempt)}
end
if attempt ~= tonumber(ARGV[1]) then
    return {'stale', status, tostring(attempt)}
end
local recovery = redis.call('HINCRBY', KEYS[1], 'recovery_count', 1)
redis.call('HSET', KEYS[1],
    'status', 'queued',
    'available_at_ms', ARGV[2],
    'last_error', ARGV[3],
    'updated_at_ms', ARGV[4])
redis.call('HDEL', KEYS[1],
    'assigned_worker', 'worker_queue', 'lease_expires_at_ms',
    'completion_id', 'completion_payload', 'artifact_commit_id')
return {'ok', 'queued', tostring(attempt), tostring(recovery)}
"""


TERMINATE_SCRIPT = r"""
if redis.call('EXISTS', KEYS[1]) == 0 then
    return {'missing', ''}
end
local status = redis.call('HGET', KEYS[1], 'status') or ''
local attempt = tonumber(redis.call('HGET', KEYS[1], 'dispatch_attempt') or '0')
if status == ARGV[2] then
    return {'already', status, tostring(attempt)}
end
if status == 'succeeded' or status == 'failed' or status == 'cancelled' or status == 'dead_lettered' then
    return {'terminal', status, tostring(attempt)}
end
if ARGV[1] ~= '' and attempt ~= tonumber(ARGV[1]) then
    return {'stale', status, tostring(attempt)}
end
redis.call('HSET', KEYS[1],
    'status', ARGV[2],
    'last_error', ARGV[3],
    'finished_at_ms', ARGV[4],
    'updated_at_ms', ARGV[4])
redis.call('HDEL', KEYS[1], 'lease_expires_at_ms')
return {'ok', ARGV[2], tostring(attempt)}
"""


class V2JobStateStore:
    """Atomic Redis state machine shared by shadow and production V2 paths."""

    def __init__(self, redis_client, *, key_prefix: str = "orchestrator:v2:job"):
        self.redis = redis_client
        self.key_prefix = key_prefix.rstrip(":")

    def key(self, job_id: str) -> str:
        return f"{self.key_prefix}:{job_id}"

    def create_job(
        self,
        job_id: str,
        job_type: str,
        *,
        available_at_ms: int = 0,
        now_ms: int | None = None,
    ) -> TransitionResult:
        now_ms = _now_ms(now_ms)
        return self._run(
            CREATE_JOB_SCRIPT,
            job_id,
            job_id,
            job_type,
            available_at_ms,
            now_ms,
        )

    def dispatch(
        self,
        job_id: str,
        *,
        worker_name: str,
        queue_name: str,
        now_ms: int | None = None,
    ) -> TransitionResult:
        return self._run(
            DISPATCH_SCRIPT,
            job_id,
            worker_name,
            queue_name,
            _now_ms(now_ms),
        )

    def claim(
        self,
        job_id: str,
        *,
        worker_name: str,
        dispatch_attempt: int,
        lease_expires_at_ms: int,
        now_ms: int | None = None,
    ) -> TransitionResult:
        return self._run(
            CLAIM_SCRIPT,
            job_id,
            worker_name,
            dispatch_attempt,
            lease_expires_at_ms,
            _now_ms(now_ms),
        )

    def renew_lease(
        self,
        job_id: str,
        *,
        worker_name: str,
        dispatch_attempt: int,
        lease_expires_at_ms: int,
        now_ms: int | None = None,
    ) -> TransitionResult:
        return self._run(
            RENEW_LEASE_SCRIPT,
            job_id,
            worker_name,
            dispatch_attempt,
            lease_expires_at_ms,
            _now_ms(now_ms),
        )

    def begin_finalization(
        self,
        job_id: str,
        *,
        worker_name: str,
        dispatch_attempt: int,
        completion_id: str,
        completion_payload: dict,
        now_ms: int | None = None,
    ) -> TransitionResult:
        return self._run(
            BEGIN_FINALIZATION_SCRIPT,
            job_id,
            worker_name,
            dispatch_attempt,
            completion_id,
            json.dumps(completion_payload, separators=(",", ":"), sort_keys=True),
            _now_ms(now_ms),
        )

    def finish_finalization(
        self,
        job_id: str,
        *,
        completion_id: str,
        terminal_status: str,
        artifact_commit_id: str = "",
        now_ms: int | None = None,
    ) -> TransitionResult:
        if terminal_status not in {V2JobStatus.SUCCEEDED, V2JobStatus.FAILED}:
            raise ValueError("Finalization must end as succeeded or failed.")
        return self._run(
            FINISH_FINALIZATION_SCRIPT,
            job_id,
            completion_id,
            terminal_status,
            artifact_commit_id,
            _now_ms(now_ms),
        )

    def requeue(
        self,
        job_id: str,
        *,
        dispatch_attempt: int,
        available_at_ms: int,
        reason: str,
        now_ms: int | None = None,
    ) -> TransitionResult:
        return self._run(
            REQUEUE_SCRIPT,
            job_id,
            dispatch_attempt,
            available_at_ms,
            reason,
            _now_ms(now_ms),
        )

    def cancel(
        self,
        job_id: str,
        *,
        reason: str,
        dispatch_attempt: int | None = None,
        now_ms: int | None = None,
    ) -> TransitionResult:
        return self._terminate(
            job_id,
            V2JobStatus.CANCELLED,
            reason,
            dispatch_attempt,
            now_ms,
        )

    def dead_letter(
        self,
        job_id: str,
        *,
        reason: str,
        dispatch_attempt: int,
        now_ms: int | None = None,
    ) -> TransitionResult:
        return self._terminate(
            job_id,
            V2JobStatus.DEAD_LETTERED,
            reason,
            dispatch_attempt,
            now_ms,
        )

    def get_job(self, job_id: str) -> dict:
        values = self.redis.hgetall(self.key(job_id))
        normalized = {_text(key): _text(value) for key, value in values.items()}
        for field in {
            "coordination_version",
            "dispatch_attempt",
            "recovery_count",
            "max_recovery_attempts",
            "available_at_ms",
            "created_at_ms",
            "updated_at_ms",
            "lease_expires_at_ms",
            "finished_at_ms",
        }:
            if field in normalized:
                normalized[field] = int(normalized[field])
        if "completion_payload" in normalized:
            normalized["completion_payload"] = json.loads(
                normalized["completion_payload"]
            )
        if "payload" in normalized:
            normalized["payload"] = json.loads(normalized["payload"])
        return normalized

    def delete_job(self, job_id: str) -> int:
        return int(self.redis.delete(self.key(job_id)))

    def _terminate(
        self,
        job_id: str,
        terminal_status: str,
        reason: str,
        dispatch_attempt: int | None,
        now_ms: int | None,
    ) -> TransitionResult:
        return self._run(
            TERMINATE_SCRIPT,
            job_id,
            "" if dispatch_attempt is None else dispatch_attempt,
            terminal_status,
            reason,
            _now_ms(now_ms),
        )

    def _run(self, script: str, job_id: str, *args) -> TransitionResult:
        response = self.redis.eval(script, 1, self.key(job_id), *args)
        values = [_text(value) for value in response]
        code = values[0]
        status = values[1] if len(values) > 1 else ""
        attempt = None
        if len(values) > 2 and values[2] not in {"", None}:
            attempt = int(values[2])
        return TransitionResult(
            accepted=code in {"ok", "already"},
            code=code,
            status=status,
            dispatch_attempt=attempt,
            idempotent=code in {"already", "exists"},
        )


def _now_ms(value: int | None) -> int:
    if value is not None:
        return int(value)
    return int(time.time() * 1000)


def _text(value) -> str:
    if isinstance(value, bytes):
        return value.decode("utf-8")
    return str(value)
