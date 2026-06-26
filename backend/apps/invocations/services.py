from __future__ import annotations

import json
from pathlib import PurePosixPath
from typing import Iterable

from django.conf import settings
from django.core.files.base import File
from django.utils.text import get_valid_filename

from .models import Invocation, InvocationInputFile, InvocationOutputFile


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
        "declared_output_files": function_version.declared_output_files,
        "invocation_output_max_files": function_version.invocation_output_max_files,
        "invocation_output_max_file_size_mb": (
            function_version.invocation_output_max_file_size_mb
        ),
        "invocation_output_max_total_size_mb": (
            function_version.invocation_output_max_total_size_mb
        ),
        "event": invocation.event,
        "queued_at": invocation.queued_at.isoformat(),
    }


def enqueue_invocation(invocation: Invocation) -> dict:
    import redis
    from apps.jobs.services import create_invocation_job_record

    payload = build_invocation_job(invocation)
    job = create_invocation_job_record(invocation, payload)
    client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)
    client.rpush(settings.SCHEDULER_INVOCATION_QUEUE_NAME, str(job.job_id))
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
    max_total_size_bytes = (
        int(function_version.invocation_input_max_total_size_mb or 0) * 1024 * 1024
    )

    if not files:
        return
    if not allowed_types:
        raise ValueError("Function version does not allow invocation files.")
    if len(files) > max_files:
        raise ValueError(
            f"Function version accepts at most {max_files} input file(s)."
        )
    total_size = sum(int(getattr(uploaded_file, "size", 0) or 0) for uploaded_file in files)
    if max_total_size_bytes and total_size > max_total_size_bytes:
        raise ValueError(
            f"Invocation input files exceed the total size limit of {function_version.invocation_input_max_total_size_mb} MB."
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


def normalize_output_name(value: str) -> str:
    name = str(value or "").strip().replace("\\", "/")
    path = PurePosixPath(name)
    if (
        not name
        or path.is_absolute()
        or path.name != name
        or name in {".", ".."}
        or any(part == ".." for part in path.parts)
    ):
        raise ValueError("Output file path is unsafe.")
    if name == "result.json":
        raise ValueError("result.json is reserved for the function result.")
    return name


def store_invocation_output_file(
    *,
    invocation: Invocation,
    uploaded_file,
    original_path: str,
    position: int = 0,
) -> InvocationOutputFile:
    version = invocation.function_version
    normalized_path = normalize_output_name(original_path)
    declared_outputs = set(version.declared_output_files or [])
    if normalized_path not in declared_outputs:
        raise ValueError(f"Output file is not declared: {normalized_path}")

    max_files = int(version.invocation_output_max_files or 0)
    max_file_size = int(version.invocation_output_max_file_size_mb or 0) * 1024 * 1024
    max_total_size = int(version.invocation_output_max_total_size_mb or 0) * 1024 * 1024
    size = int(getattr(uploaded_file, "size", 0) or 0)
    if max_files <= 0:
        raise ValueError("Function version does not allow output files.")
    if size > max_file_size:
        raise ValueError(
            f"Output file exceeds the maximum size of {version.invocation_output_max_file_size_mb} MB."
        )

    existing = InvocationOutputFile.objects.filter(
        invocation=invocation,
        original_path=normalized_path,
    ).first()
    output_count = invocation.output_files.exclude(pk=getattr(existing, "pk", None)).count()
    if output_count + 1 > max_files:
        raise ValueError(f"Invocation accepts at most {max_files} output file(s).")

    total_size = sum(
        invocation.output_files.exclude(pk=getattr(existing, "pk", None)).values_list(
            "size_bytes",
            flat=True,
        )
    )
    if total_size + size > max_total_size:
        raise ValueError(
            f"Invocation output files exceed the total size limit of {version.invocation_output_max_total_size_mb} MB."
        )

    safe_name = get_valid_filename(normalized_path) or "output"
    if existing is None:
        record = InvocationOutputFile.objects.create(
            invocation=invocation,
            original_path=normalized_path,
            safe_name=safe_name,
            content_type=getattr(uploaded_file, "content_type", "") or "",
            size_bytes=size,
            position=position,
        )
    else:
        if existing.file:
            existing.file.delete(save=False)
        existing.safe_name = safe_name
        existing.content_type = getattr(uploaded_file, "content_type", "") or ""
        existing.size_bytes = size
        existing.position = position
        record = existing

    record.file.save(safe_name, File(uploaded_file), save=True)
    return record
