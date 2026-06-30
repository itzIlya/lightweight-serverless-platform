from __future__ import annotations

import json

from django.conf import settings
from django.db import transaction
from django.utils import timezone

from .models import OutboxEvent


PUBLISH_EVENT_SCRIPT = """
local existing_stream_id = redis.call('GET', KEYS[2])
if existing_stream_id then
    return existing_stream_id
end

local stream_id = redis.call(
    'XADD', KEYS[1], '*',
    'event_id', ARGV[1],
    'event_type', ARGV[2],
    'aggregate_id', ARGV[3],
    'payload', ARGV[4]
)
redis.call('SET', KEYS[2], stream_id)
return stream_id
"""


def publish_event_to_stream(
    redis_client,
    event: OutboxEvent,
    *,
    stream_name: str | None = None,
) -> str:
    stream = stream_name or settings.ORCHESTRATOR_EVENT_STREAM
    dedupe_key = f"orchestrator:outbox:published:{event.event_id}"
    stream_id = redis_client.eval(
        PUBLISH_EVENT_SCRIPT,
        2,
        stream,
        dedupe_key,
        str(event.event_id),
        event.event_type,
        str(event.aggregate_id),
        json.dumps(event.payload, separators=(",", ":"), sort_keys=True),
    )
    if isinstance(stream_id, bytes):
        return stream_id.decode("utf-8")
    return str(stream_id)


def publish_pending_outbox_events(
    redis_client,
    *,
    batch_size: int = 100,
    stream_name: str | None = None,
) -> dict[str, int]:
    event_ids = list(
        OutboxEvent.objects.filter(published_at__isnull=True)
        .order_by("created_at")
        .values_list("id", flat=True)[:batch_size]
    )
    result = {"published": 0, "failed": 0}

    for event_pk in event_ids:
        with transaction.atomic():
            event = OutboxEvent.objects.select_for_update().get(pk=event_pk)
            if event.published_at is not None:
                continue

            event.publish_attempts += 1
            try:
                stream_id = publish_event_to_stream(
                    redis_client,
                    event,
                    stream_name=stream_name,
                )
            except Exception as exc:
                event.last_error = str(exc)
                event.save(
                    update_fields=["publish_attempts", "last_error", "updated_at"]
                )
                result["failed"] += 1
                continue

            event.published_at = timezone.now()
            event.stream_id = stream_id
            event.last_error = ""
            event.save(
                update_fields=[
                    "publish_attempts",
                    "published_at",
                    "stream_id",
                    "last_error",
                    "updated_at",
                ]
            )
            result["published"] += 1

    return result
