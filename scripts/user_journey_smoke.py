from __future__ import annotations

import argparse
import json
import mimetypes
import tempfile
import time
import uuid
import zipfile
from pathlib import Path
from urllib import error, request


TERMINAL_BUILD_STATES = {"built", "failed", "cancelled"}
TERMINAL_INVOCATION_STATES = {"succeeded", "failed", "timeout", "cancelled"}


class SmokeError(RuntimeError):
    pass


def make_function_bundle(path: Path) -> None:
    handler = """
def main(event, context):
    name = event.get("name", "friend")
    numbers = event.get("numbers", [])
    return {
        "message": f"Hello, {name}!",
        "echo": event,
        "sum": sum(numbers),
        "request_id": context.get("request_id"),
    }
""".strip()
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("handler.py", handler + "\n")
        archive.writestr("requirements.txt", "")
        archive.writestr("config.json", "{}")


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

    req = request.Request(url, data=data, method=method, headers=headers)
    return open_json(req, expected)


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
    boundary = f"----serverless-smoke-{uuid.uuid4().hex}"
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


def open_json(req: request.Request, expected: set[int]) -> dict:
    try:
        with request.urlopen(req, timeout=30) as response:
            raw = response.read().decode("utf-8")
            if response.status not in expected:
                raise SmokeError(f"{req.full_url} returned {response.status}: {raw}")
            return json.loads(raw) if raw else {}
    except error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        raise SmokeError(f"{req.full_url} returned HTTP {exc.code}: {raw}") from exc
    except error.URLError as exc:
        raise SmokeError(f"{req.full_url} failed: {exc}") from exc


def poll_until(
    *,
    label: str,
    fetch,
    status_field: str,
    terminal_states: set[str],
    success_state: str,
    timeout_seconds: int,
    interval_seconds: int,
) -> dict:
    deadline = time.monotonic() + timeout_seconds
    last = {}
    while time.monotonic() < deadline:
        last = fetch()
        state = last.get(status_field)
        print(f"{label}: {state}")
        if state in terminal_states:
            if state != success_state:
                raise SmokeError(
                    f"{label} ended as {state}: {json.dumps(last, indent=2)}"
                )
            return last
        time.sleep(interval_seconds)
    raise SmokeError(
        f"{label} did not finish within {timeout_seconds}s. "
        f"Last response: {json.dumps(last, indent=2)}"
    )


def run(base_url: str) -> dict:
    base_url = base_url.rstrip("/")
    suffix = uuid.uuid4().hex[:8]
    username = f"smoke_{suffix}"
    password = "StrongerPass123!"

    print("1. Register user and receive JWT")
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
    print(f"   user={auth['user']['username']} role={auth['user']['role']}")

    print("2. Create function")
    function = json_request(
        "POST",
        f"{base_url}/api/functions/",
        {
            "name": f"Smoke Echo {suffix}",
            "description": "End-to-end smoke test function.",
            "invoke_access": "private",
        },
        token=token,
        expected={201},
    )
    function_id = function["id"]
    print(f"   function_id={function_id} slug={function['slug']}")

    with tempfile.TemporaryDirectory(prefix="serverless-smoke-") as tmp:
        bundle_path = Path(tmp) / "function.zip"
        make_function_bundle(bundle_path)

        print("3. Upload function version")
        version = multipart_request(
            "POST",
            f"{base_url}/api/functions/{function_id}/versions/",
            fields={
                "version": "v1",
                "runtime": "python3.13",
                "handler": "handler.main",
                "config": json.dumps({"memory_mb": 128, "timeout_seconds": 10}),
            },
            files={"source_bundle": bundle_path},
            token=token,
            expected={201},
        )

    version_id = version["id"]
    print(f"   version_id={version_id} build_status={version['build_status']}")

    print("4. Queue build")
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
        timeout_seconds=180,
        interval_seconds=3,
    )
    print(f"   image_ref={version['image_ref']}")

    print("5. Invoke function")
    invocation = json_request(
        "POST",
        f"{base_url}/api/functions/{function_id}/invoke/",
        {
            "version": "v1",
            "event": {
                "name": "Ilya",
                "numbers": [1, 2, 3],
            },
        },
        token=token,
        expected={202},
    )
    invocation_id = invocation["id"]
    print(f"   invocation_id={invocation_id} request_id={invocation['request_id']}")

    invocation = poll_until(
        label="   invocation",
        fetch=lambda: json_request(
            "GET",
            f"{base_url}/api/invocations/{invocation_id}/",
            token=token,
        ),
        status_field="status",
        terminal_states=TERMINAL_INVOCATION_STATES,
        success_state="succeeded",
        timeout_seconds=120,
        interval_seconds=2,
    )

    expected_result = {
        "message": "Hello, Ilya!",
        "echo": {"name": "Ilya", "numbers": [1, 2, 3]},
        "sum": 6,
    }
    for key, value in expected_result.items():
        if invocation["result"].get(key) != value:
            raise SmokeError(
                f"Unexpected result[{key!r}]: {invocation['result'].get(key)!r}"
            )

    print("6. Final invocation result")
    print(json.dumps(invocation["result"], indent=2))
    return {
        "user": auth["user"],
        "function": function,
        "version": version,
        "invocation": invocation,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run a realistic user journey against the local serverless platform."
    )
    parser.add_argument(
        "--base-url",
        default="http://localhost:8000",
        help="Backend base URL. Default: http://localhost:8000",
    )
    args = parser.parse_args()
    try:
        summary = run(args.base_url)
    except SmokeError as exc:
        raise SystemExit(f"SMOKE TEST FAILED: {exc}") from exc

    print("SMOKE TEST PASSED")
    print(
        json.dumps(
            {
                "function_id": summary["function"]["id"],
                "version_id": summary["version"]["id"],
                "invocation_id": summary["invocation"]["id"],
                "invocation_status": summary["invocation"]["status"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
