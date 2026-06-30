from __future__ import annotations

import argparse
import concurrent.futures
import json
import mimetypes
import statistics
import tempfile
import time
import uuid
import zipfile
from pathlib import Path
from urllib import error, request


TERMINAL_BUILD_STATES = {"built", "failed", "cancelled"}
TERMINAL_INVOCATION_STATES = {"succeeded", "failed", "timeout", "cancelled"}


class WorkloadError(RuntimeError):
    pass


def make_sleep_bundle(path: Path) -> None:
    handler = """
import time


def main(event, context):
    sleep_seconds = float(event.get("sleep_seconds", 1))
    index = event.get("index")
    started = time.time()
    time.sleep(sleep_seconds)
    finished = time.time()
    return {
        "index": index,
        "slept_seconds": sleep_seconds,
        "elapsed_seconds": round(finished - started, 3),
        "request_id": context.get("request_id"),
    }
""".strip()
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("handler.py", handler + "\n")
        archive.writestr("requirements.txt", "")
        archive.writestr("config.json", "{}")


def open_json(req: request.Request, expected: set[int]) -> dict:
    try:
        with request.urlopen(req, timeout=45) as response:
            raw = response.read().decode("utf-8")
            if response.status not in expected:
                raise WorkloadError(
                    f"{req.full_url} returned {response.status}: {raw}"
                )
            return json.loads(raw) if raw else {}
    except error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        raise WorkloadError(f"{req.full_url} returned HTTP {exc.code}: {raw}") from exc
    except error.URLError as exc:
        raise WorkloadError(f"{req.full_url} failed: {exc}") from exc


def json_request(
    method: str,
    url: str,
    payload: dict | None = None,
    *,
    token: str | None = None,
    expected: set[int] | None = None,
) -> dict:
    expected = expected or {200, 201, 202}
    data = None
    headers = {"Accept": "application/json"}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return open_json(request.Request(url, data=data, method=method, headers=headers), expected)


def multipart_request(
    method: str,
    url: str,
    *,
    fields: dict[str, str],
    files: dict[str, Path],
    token: str,
    expected: set[int] | None = None,
) -> dict:
    expected = expected or {200, 201, 202}
    boundary = f"----serverless-workload-{uuid.uuid4().hex}"
    body = bytearray()

    def add_line(value: bytes = b"") -> None:
        body.extend(value)
        body.extend(b"\r\n")

    for name, value in fields.items():
        add_line(f"--{boundary}".encode())
        add_line(f'Content-Disposition: form-data; name="{name}"'.encode())
        add_line()
        add_line(str(value).encode("utf-8"))

    for name, path in files.items():
        content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        add_line(f"--{boundary}".encode())
        add_line(
            (
                f'Content-Disposition: form-data; name="{name}"; '
                f'filename="{path.name}"'
            ).encode()
        )
        add_line(f"Content-Type: {content_type}".encode())
        add_line()
        body.extend(path.read_bytes())
        body.extend(b"\r\n")

    add_line(f"--{boundary}--".encode())
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
        "Content-Type": f"multipart/form-data; boundary={boundary}",
    }
    req = request.Request(url, data=bytes(body), method=method, headers=headers)
    return open_json(req, expected)


def poll_until(
    *,
    label: str,
    fetch,
    status_field: str,
    terminal_states: set[str],
    success_state: str,
    timeout_seconds: int,
    interval_seconds: float,
) -> dict:
    deadline = time.monotonic() + timeout_seconds
    last = {}
    while time.monotonic() < deadline:
        last = fetch()
        state = last.get(status_field)
        print(f"{label}: {state}")
        if state in terminal_states:
            if state != success_state:
                raise WorkloadError(
                    f"{label} ended as {state}: {json.dumps(last, indent=2)}"
                )
            return last
        time.sleep(interval_seconds)
    raise WorkloadError(
        f"{label} did not finish within {timeout_seconds}s. "
        f"Last response: {json.dumps(last, indent=2)}"
    )


def submit_invocation(base_url: str, token: str, function_id: int, index: int, sleep_seconds: float) -> dict:
    submitted_at = time.monotonic()
    invocation = json_request(
        "POST",
        f"{base_url}/api/functions/{function_id}/invoke/",
        {
            "version": "v1",
            "event": {
                "index": index,
                "sleep_seconds": sleep_seconds,
            },
        },
        token=token,
        expected={202},
    )
    invocation["client_submit_elapsed_seconds"] = round(time.monotonic() - submitted_at, 3)
    return invocation


def poll_invocation(base_url: str, token: str, invocation_id: int, timeout_seconds: int) -> dict:
    return poll_until(
        label=f"   invocation {invocation_id}",
        fetch=lambda: json_request(
            "GET",
            f"{base_url}/api/invocations/{invocation_id}/",
            token=token,
        ),
        status_field="status",
        terminal_states=TERMINAL_INVOCATION_STATES,
        success_state="succeeded",
        timeout_seconds=timeout_seconds,
        interval_seconds=1,
    )


def run(base_url: str, *, count: int, sleep_seconds: float, output_json: Path | None) -> dict:
    base_url = base_url.rstrip("/")
    suffix = uuid.uuid4().hex[:8]
    username = f"workload_{suffix}"
    password = "StrongerPass123!"

    print("1. Register workload user")
    auth = json_request(
        "POST",
        f"{base_url}/api/auth/register/",
        {
            "username": username,
            "email": f"{username}@example.com",
            "password": password,
        },
        expected={201},
    )
    token = auth["access"]

    print("2. Create private sleep function")
    function = json_request(
        "POST",
        f"{base_url}/api/functions/",
        {
            "name": f"Concurrent Sleep {suffix}",
            "description": "Concurrent invocation workload test.",
            "invoke_access": "private",
        },
        token=token,
        expected={201},
    )
    function_id = function["id"]

    with tempfile.TemporaryDirectory(prefix="serverless-workload-") as tmp:
        bundle_path = Path(tmp) / "function.zip"
        make_sleep_bundle(bundle_path)

        print("3. Upload function version")
        version = multipart_request(
            "POST",
            f"{base_url}/api/functions/{function_id}/versions/",
            fields={
                "version": "v1",
                "runtime": "python3.13",
                "handler": "handler.main",
                "config": json.dumps(
                    {
                        "memory_mb": 128,
                        "timeout_seconds": max(10, int(sleep_seconds) + 8),
                    }
                ),
                "declared_output_files": json.dumps([]),
            },
            files={"source_bundle": bundle_path},
            token=token,
            expected={201},
        )

    version_id = version["id"]
    print("4. Build function image")
    json_request(
        "POST",
        f"{base_url}/api/versions/{version_id}/build/",
        token=token,
        expected={200, 202},
    )
    version = poll_until(
        label="   build",
        fetch=lambda: json_request(
            "GET",
            f"{base_url}/api/versions/{version_id}/",
            token=token,
        ),
        status_field="build_status",
        terminal_states=TERMINAL_BUILD_STATES,
        success_state="built",
        timeout_seconds=240,
        interval_seconds=3,
    )

    print(f"5. Submit {count} invocations concurrently")
    submit_started = time.monotonic()
    with concurrent.futures.ThreadPoolExecutor(max_workers=count) as pool:
        submitted = list(
            pool.map(
                lambda index: submit_invocation(
                    base_url,
                    token,
                    function_id,
                    index,
                    sleep_seconds,
                ),
                range(count),
            )
        )
    submit_elapsed = time.monotonic() - submit_started

    print("6. Poll invocations concurrently")
    poll_started = time.monotonic()
    with concurrent.futures.ThreadPoolExecutor(max_workers=count) as pool:
        completed = list(
            pool.map(
                lambda invocation: poll_invocation(
                    base_url,
                    token,
                    invocation["id"],
                    timeout_seconds=max(120, int(count * sleep_seconds) + 60),
                ),
                submitted,
            )
        )
    wall_elapsed = time.monotonic() - submit_started
    poll_elapsed = time.monotonic() - poll_started

    durations_ms = [
        item.get("duration_ms")
        for item in completed
        if isinstance(item.get("duration_ms"), int)
    ]
    summary = {
        "base_url": base_url,
        "username": username,
        "function_id": function_id,
        "function_slug": function["slug"],
        "version_id": version_id,
        "image_ref": version.get("image_ref"),
        "invocation_count": count,
        "sleep_seconds": sleep_seconds,
        "sequential_sleep_seconds": round(count * sleep_seconds, 3),
        "client_submit_elapsed_seconds": round(submit_elapsed, 3),
        "client_poll_elapsed_seconds": round(poll_elapsed, 3),
        "client_wall_elapsed_seconds": round(wall_elapsed, 3),
        "statuses": sorted({item["status"] for item in completed}),
        "duration_ms_min": min(durations_ms) if durations_ms else None,
        "duration_ms_max": max(durations_ms) if durations_ms else None,
        "duration_ms_median": int(statistics.median(durations_ms)) if durations_ms else None,
        "invocation_ids": [item["id"] for item in completed],
        "request_ids": [item["request_id"] for item in completed],
        "read_token_returned": all(bool(item.get("read_token")) for item in submitted),
    }

    if output_json is not None:
        output_json.parent.mkdir(parents=True, exist_ok=True)
        output_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(json.dumps(summary, indent=2))
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument("--count", type=int, default=12)
    parser.add_argument("--sleep-seconds", type=float, default=3)
    parser.add_argument("--output-json", type=Path)
    args = parser.parse_args()
    run(
        args.base_url,
        count=args.count,
        sleep_seconds=args.sleep_seconds,
        output_json=args.output_json,
    )


if __name__ == "__main__":
    main()
