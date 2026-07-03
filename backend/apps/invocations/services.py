from __future__ import annotations

import json
import hashlib
from pathlib import PurePosixPath
from typing import Iterable
import uuid

from django.conf import settings
from django.core.files.base import File
from django.db import transaction
from django.utils import timezone
from django.utils.text import get_valid_filename

from .models import (
    Invocation,
    InvocationInputFile,
    InvocationOutputFile,
    InvocationStagedCompletion,
    StagedCompletionStatus,
)


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
    from apps.jobs.models import JobType
    from apps.jobs.services import (
        coordination_version_for_job,
        create_invocation_job_record,
    )

    payload = build_invocation_job(invocation)
    coordination_version = coordination_version_for_job(
        JobType.INVOCATION,
        invocation.request_id,
        function_id=invocation.function_version.function_id,
        invoke_access=invocation.function_version.function.invoke_access,
    )
    job = create_invocation_job_record(
        invocation,
        payload,
        coordination_version=coordination_version,
    )
    if job.coordination_version == 1:
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
        staged_completion__isnull=True,
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


def store_staged_invocation_output_file(
    *,
    invocation: Invocation,
    job_id,
    dispatch_attempt: int,
    completion_id: str,
    uploaded_file,
    original_path: str,
    checksum_sha256: str,
    position: int = 0,
) -> InvocationOutputFile:
    from apps.jobs.models import CoordinationVersion, Job

    job = Job.objects.filter(
        job_id=job_id,
        invocation=invocation,
        coordination_version=CoordinationVersion.V2,
    ).first()
    if job is None:
        raise ValueError("Staged output does not match a V2 invocation job.")
    if dispatch_attempt < 1:
        raise ValueError("dispatch_attempt must be positive.")

    normalized_path = normalize_output_name(original_path)
    digest = uploaded_file_sha256(uploaded_file)
    if checksum_sha256.lower() != digest:
        raise ValueError("Output checksum does not match the uploaded file.")

    with transaction.atomic():
        completion, created = InvocationStagedCompletion.objects.select_for_update().get_or_create(
            completion_id=completion_id,
            defaults={
                "invocation": invocation,
                "job_id": job.job_id,
                "dispatch_attempt": dispatch_attempt,
            },
        )
        if not created and (
            completion.invocation_id != invocation.id
            or completion.job_id != job.job_id
            or completion.dispatch_attempt != dispatch_attempt
        ):
            raise ValueError("completion_id belongs to a different invocation attempt.")
        if completion.status != StagedCompletionStatus.STAGED:
            raise ValueError("Completion no longer accepts staged output files.")

        existing = completion.output_files.filter(original_path=normalized_path).first()
        if existing is not None and existing.checksum_sha256 == digest:
            return existing

        validate_staged_output_limits(
            invocation,
            completion,
            normalized_path=normalized_path,
            size=int(getattr(uploaded_file, "size", 0) or 0),
            replacing=existing,
        )
        if existing is None:
            existing = InvocationOutputFile(
                invocation=invocation,
                staged_completion=completion,
                status=StagedCompletionStatus.STAGED,
                original_path=normalized_path,
            )
        elif existing.file:
            existing.file.delete(save=False)
        existing.safe_name = get_valid_filename(normalized_path) or "output"
        existing.content_type = getattr(uploaded_file, "content_type", "") or ""
        existing.size_bytes = int(getattr(uploaded_file, "size", 0) or 0)
        existing.position = position
        existing.checksum_sha256 = digest
        existing.save()
        existing.file.save(existing.safe_name, File(uploaded_file), save=True)
        return existing


def validate_staged_output_limits(
    invocation,
    completion,
    *,
    normalized_path: str,
    size: int,
    replacing=None,
) -> None:
    version = invocation.function_version
    if normalized_path not in set(version.declared_output_files or []):
        raise ValueError(f"Output file is not declared: {normalized_path}")
    max_files = int(version.invocation_output_max_files or 0)
    max_file_size = int(version.invocation_output_max_file_size_mb or 0) * 1024 * 1024
    max_total_size = int(version.invocation_output_max_total_size_mb or 0) * 1024 * 1024
    if size > max_file_size:
        raise ValueError(
            f"Output file exceeds the maximum size of {version.invocation_output_max_file_size_mb} MB."
        )
    others = completion.output_files.exclude(pk=getattr(replacing, "pk", None))
    if others.count() + 1 > max_files:
        raise ValueError(f"Invocation accepts at most {max_files} output file(s).")
    if sum(others.values_list("size_bytes", flat=True)) + size > max_total_size:
        raise ValueError(
            f"Invocation output files exceed the total size limit of {version.invocation_output_max_total_size_mb} MB."
        )


def uploaded_file_sha256(uploaded_file) -> str:
    digest = hashlib.sha256()
    try:
        uploaded_file.seek(0)
    except Exception:
        pass
    chunks = uploaded_file.chunks() if hasattr(uploaded_file, "chunks") else iter(lambda: uploaded_file.read(64 * 1024), b"")
    for chunk in chunks:
        digest.update(chunk)
    try:
        uploaded_file.seek(0)
    except Exception:
        pass
    return digest.hexdigest()


def commit_staged_invocation_completion(
    *,
    invocation: Invocation,
    job_id,
    dispatch_attempt: int,
    completion_id: str,
    terminal_status: str,
    completion_payload: dict,
    output_manifest: list,
) -> InvocationStagedCompletion:
    from apps.jobs.models import CoordinationVersion, Job

    with transaction.atomic():
        job = Job.objects.select_for_update().filter(
            job_id=job_id,
            invocation=invocation,
            coordination_version=CoordinationVersion.V2,
        ).first()
        if job is None:
            raise ValueError("Completion does not match a V2 invocation job.")
        completion, created = InvocationStagedCompletion.objects.select_for_update().get_or_create(
            completion_id=completion_id,
            defaults={
                "invocation": invocation,
                "job_id": job.job_id,
                "dispatch_attempt": dispatch_attempt,
            },
        )
        if not created and (
            completion.invocation_id != invocation.id
            or completion.job_id != job.job_id
            or completion.dispatch_attempt != dispatch_attempt
        ):
            raise ValueError("completion_id belongs to a different invocation attempt.")
        if completion.status == StagedCompletionStatus.COMMITTED:
            return completion
        if completion.status != StagedCompletionStatus.STAGED:
            raise ValueError("Staged completion has expired.")

        files = list(completion.output_files.order_by("position", "id"))
        verify_output_manifest(files, output_manifest)
        completion.terminal_status = terminal_status
        completion.result = completion_payload.get("result") or {}
        completion.stdout = completion_payload.get("stdout", "")
        completion.stderr = completion_payload.get("stderr", "")
        completion.exit_code = completion_payload.get("exit_code")
        completion.cold_start = bool(completion_payload.get("cold_start", False))
        completion.error_message = completion_payload.get("error_message", "")
        completion.duration_ms = completion_payload.get("duration_ms")
        completion.output_manifest = output_manifest
        completion.artifact_commit_id = completion.artifact_commit_id or uuid.uuid4()
        completion.status = StagedCompletionStatus.COMMITTED
        completion.committed_at = timezone.now()
        completion.save()
        completion.output_files.update(status=StagedCompletionStatus.COMMITTED)
        return completion


def verify_output_manifest(files, manifest: list) -> None:
    expected = {
        item.original_path: {
            "size_bytes": item.size_bytes,
            "checksum_sha256": item.checksum_sha256,
        }
        for item in files
    }
    supplied = {
        str(item.get("original_path", "")): {
            "size_bytes": int(item.get("size_bytes", -1)),
            "checksum_sha256": str(item.get("checksum_sha256", "")).lower(),
        }
        for item in manifest
    }
    if supplied != expected:
        raise ValueError("Output manifest does not match staged files.")
