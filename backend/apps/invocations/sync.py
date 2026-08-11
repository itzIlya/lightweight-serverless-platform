from __future__ import annotations

import json
import time
from dataclasses import dataclass

from django.conf import settings

from .models import Invocation
from .v2_reads import serialize_invocation_for_read


@dataclass(frozen=True)
class SyncInvocationWaitResult:
    completed: bool
    data: dict


class SyncInvocationResponseTooLarge(ValueError):
    pass


def wait_for_sync_invocation(
    invocation: Invocation,
    *,
    timeout_seconds: float | None = None,
    poll_interval_seconds: float | None = None,
) -> SyncInvocationWaitResult:
    timeout = float(
        timeout_seconds
        if timeout_seconds is not None
        else settings.SYNC_INVOCATION_TIMEOUT_SECONDS
    )
    poll_interval = float(
        poll_interval_seconds
        if poll_interval_seconds is not None
        else settings.SYNC_INVOCATION_POLL_INTERVAL_SECONDS
    )
    deadline = time.monotonic() + max(timeout, 0.0)

    while True:
        invocation.refresh_from_db()
        data = dict(serialize_invocation_for_read(invocation))
        if data.get("is_terminal") and data.get("result_available"):
            enforce_sync_response_limits(data)
            return SyncInvocationWaitResult(completed=True, data=data)

        remaining = deadline - time.monotonic()
        if remaining <= 0:
            return SyncInvocationWaitResult(completed=False, data=data)
        time.sleep(min(max(poll_interval, 0.01), remaining))


def enforce_sync_response_limits(data: dict) -> None:
    _enforce_json_limit(
        "result",
        data.get("result") or {},
        int(settings.SYNC_INVOCATION_MAX_RESULT_BYTES),
    )
    _enforce_text_limit(
        "stdout",
        data.get("stdout") or "",
        int(settings.SYNC_INVOCATION_MAX_STDOUT_BYTES),
    )
    _enforce_text_limit(
        "stderr",
        data.get("stderr") or "",
        int(settings.SYNC_INVOCATION_MAX_STDERR_BYTES),
    )


def _enforce_json_limit(field: str, value, max_bytes: int) -> None:
    encoded = json.dumps(value, separators=(",", ":"), sort_keys=True).encode("utf-8")
    if len(encoded) > max_bytes:
        raise SyncInvocationResponseTooLarge(
            f"Synchronous invocation {field} exceeds {max_bytes} bytes."
        )


def _enforce_text_limit(field: str, value: str, max_bytes: int) -> None:
    if len(str(value).encode("utf-8")) > max_bytes:
        raise SyncInvocationResponseTooLarge(
            f"Synchronous invocation {field} exceeds {max_bytes} bytes."
        )
