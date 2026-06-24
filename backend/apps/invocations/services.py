from __future__ import annotations

import json
from typing import Iterable

from django.conf import settings
from django.core.files.base import File
from django.utils.text import get_valid_filename

from .models import Invocation, InvocationInputFile


def build_invocation_job(invocation: Invocation) -> dict:
    function_version = invocation.function_version
    function = function_version.function
    return {
        "type": "function.invoke",
        "invocation_id": invocation.id,
        "request_id": str(invocation.request_id),
        "function_id": function.id,
        "function_slug": function.slug,
        "function_version_id": function_version.id,
        "version": function_version.version,
        "runtime": function_version.runtime,
        "handler": function_version.handler,
        "image_ref": function_version.image_ref,
        "config": function_version.config,
        "event": invocation.event,
        "queued_at": invocation.queued_at.isoformat(),
    }


def enqueue_invocation(invocation: Invocation) -> dict:
    import redis
    from apps.jobs.services import create_invocation_job_record

    payload = build_invocation_job(invocation)
    job = create_invocation_job_record(invocation, payload)
    client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)
    client.rpush(settings.SCHEDULER_QUEUE_NAME, str(job.job_id))
    return payload


def normalize_input_mime_types(mime_types) -> list[str]:
    if not mime_types:
        return []
    return [str(item).strip().lower() for item in mime_types if str(item).strip()]


def validate_invocation_files(function_version, uploaded_files: Iterable) -> None:
    files = list(uploaded_files)
    allowed_types = normalize_input_mime_types(
        function_version.invocation_input_mime_types
    )
    max_files = int(function_version.invocation_input_max_files or 0)
    max_size_bytes = int(function_version.invocation_input_max_size_mb or 0) * 1024 * 1024

    if not files:
        return
    if not allowed_types:
        raise ValueError("Function version does not allow invocation files.")
    if len(files) > max_files:
        raise ValueError(
            f"Function version accepts at most {max_files} input file(s)."
        )

    for uploaded_file in files:
        content_type = (getattr(uploaded_file, "content_type", "") or "").lower()
        if content_type not in allowed_types:
            raise ValueError(
                "Unsupported input file type: "
                f"{content_type or 'unknown'}"
            )
        if max_size_bytes and getattr(uploaded_file, "size", 0) > max_size_bytes:
            raise ValueError(
                f"Input file exceeds the maximum size of {function_version.invocation_input_max_size_mb} MB."
            )


def store_invocation_files(
    invocation: Invocation,
    uploaded_files: Iterable,
    field_name: str = "files",
) -> list[InvocationInputFile]:
    stored = []
    for position, uploaded_file in enumerate(uploaded_files):
        original_name = get_valid_filename(uploaded_file.name) or "input"
        record = InvocationInputFile.objects.create(
            invocation=invocation,
            position=position,
            field_name=field_name,
            original_name=original_name,
            content_type=getattr(uploaded_file, "content_type", "") or "",
            size_bytes=getattr(uploaded_file, "size", 0) or 0,
        )
        record.file.save(original_name, File(uploaded_file), save=True)
        stored.append(record)
    return stored
