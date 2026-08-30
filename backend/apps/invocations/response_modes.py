from __future__ import annotations

from rest_framework.exceptions import ValidationError

from .models import Invocation, InvocationStatus
from .v2_reads import serialize_invocation_for_read


SIMPLE_RESPONSE_MODE = "simple"
ADVANCED_RESPONSE_MODE = "advanced"
SUPPORTED_RESPONSE_MODES = {SIMPLE_RESPONSE_MODE, ADVANCED_RESPONSE_MODE}


def response_mode_from_request(request, *, allow_body: bool = False) -> str:
    raw_mode = request.query_params.get("response_mode")
    if raw_mode is None and allow_body:
        raw_mode = request.data.get("response_mode")
    mode = str(raw_mode or SIMPLE_RESPONSE_MODE).strip().lower()
    if mode not in SUPPORTED_RESPONSE_MODES:
        raise ValidationError(
            {"response_mode": "Use either 'simple' or 'advanced'."}
        )
    return mode


def serialize_invocation_response(invocation: Invocation, *, mode: str) -> dict:
    return serialize_invocation_data(serialize_invocation_for_read(invocation), mode=mode)


def serialize_invocation_data(data: dict, *, mode: str) -> dict:
    if mode == ADVANCED_RESPONSE_MODE:
        return dict(data)
    if mode != SIMPLE_RESPONSE_MODE:
        raise ValidationError(
            {"response_mode": "Use either 'simple' or 'advanced'."}
        )
    return _simple_invocation_data(dict(data))


def _simple_invocation_data(data: dict) -> dict:
    status = str(data.get("status") or "")
    if not data.get("is_terminal"):
        return {
            "id": data.get("id"),
            "request_id": data.get("request_id"),
            "status": status,
            "poll_after_seconds": data.get("poll_after_seconds") or 1,
            "links": {"self": _simple_self_link(data)},
        }

    if status == InvocationStatus.SUCCEEDED:
        return {
            "result": data.get("result") or {},
            "output_files": _simple_output_files(data),
        }

    return {
        "error": {
            "status": status or InvocationStatus.FAILED,
            "message": _failure_message(data),
        },
        "output_files": _simple_output_files(data),
    }


def _simple_self_link(data: dict) -> str:
    path = (data.get("links") or {}).get("self") or f"/api/invocations/{data.get('id')}/"
    separator = "&" if "?" in path else "?"
    return f"{path}{separator}response_mode=simple"


def _simple_output_files(data: dict) -> list[dict]:
    files = []
    for output_file in data.get("output_files") or []:
        output_id = output_file.get("id")
        invocation_id = data.get("id")
        files.append(
            {
                "path": output_file.get("original_path") or output_file.get("safe_name"),
                "size_bytes": output_file.get("size_bytes"),
                "content_type": output_file.get("content_type") or "",
                "download_url": (
                    f"/api/invocations/{invocation_id}/outputs/{output_id}/download/"
                    if invocation_id and output_id
                    else ""
                ),
            }
        )
    return files


def _failure_message(data: dict) -> str:
    message = str(data.get("error_message") or "").strip()
    if message:
        return message
    return "Function execution failed."
