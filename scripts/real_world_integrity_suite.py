from __future__ import annotations

import argparse
import concurrent.futures
import json
import mimetypes
import subprocess
import tempfile
import time
import uuid
import zipfile
from pathlib import Path
from urllib import error, request


TERMINAL_BUILD_STATES = {"built", "failed", "cancelled"}
TERMINAL_INVOCATION_STATES = {"succeeded", "failed", "timeout", "cancelled"}


class IntegrityError(RuntimeError):
    pass


def make_bundle(path: Path, *, marker: str, sleep_seconds: float = 0.0) -> None:
    handler = f"""
import json
import os
import time


def main(event, context):
    sleep_seconds = float(event.get("sleep_seconds", {sleep_seconds!r}))
    if sleep_seconds:
        time.sleep(sleep_seconds)

    input_summaries = []
    input_files_json = os.environ.get("FUNCTION_INPUT_FILES_JSON", "[]")
    try:
        input_files = json.loads(input_files_json)
    except Exception:
        input_files = []
    for item in input_files:
        path = item.get("path")
        if path and os.path.exists(path):
            with open(path, "rb") as handle:
                input_summaries.append({{
                    "name": item.get("original_name") or item.get("name"),
                    "size": len(handle.read()),
                }})

    output_dir = os.environ.get("FUNCTION_OUTPUT_DIR")
    if output_dir:
        with open(os.path.join(output_dir, "report.txt"), "w", encoding="utf-8") as handle:
            handle.write("{marker} report for " + str(event.get("name", "anon")))
        with open(os.path.join(output_dir, "extra.txt"), "w", encoding="utf-8") as handle:
            handle.write("this file is intentionally undeclared")

    print("stdout marker={marker}")
    return {{
        "marker": "{marker}",
        "name": event.get("name"),
        "index": event.get("index"),
        "input_summaries": input_summaries,
        "request_id": context.get("request_id"),
    }}
""".strip()
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("handler.py", handler + "\n")
        archive.writestr("requirements.txt", "")
        archive.writestr("config.json", "{}")


def open_json(req: request.Request, expected: set[int], *, timeout: int = 45) -> dict | list:
    try:
        with request.urlopen(req, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
            if response.status not in expected:
                raise IntegrityError(
                    f"{req.full_url} returned {response.status}: {raw}"
                )
            return json.loads(raw) if raw else {}
    except error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        raise IntegrityError(f"{req.full_url} returned HTTP {exc.code}: {raw}") from exc
    except error.URLError as exc:
        raise IntegrityError(f"{req.full_url} failed: {exc}") from exc


def json_request(
    method: str,
    url: str,
    payload: dict | None = None,
    *,
    token: str | None = None,
    headers: dict[str, str] | None = None,
    expected: set[int] | None = None,
    timeout: int = 45,
) -> dict | list:
    expected = expected or {200, 201, 202}
    request_headers = {"Accept": "application/json"}
    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        request_headers["Content-Type"] = "application/json"
    if token:
        request_headers["Authorization"] = f"Bearer {token}"
    if headers:
        request_headers.update(headers)
    return open_json(
        request.Request(url, data=data, method=method, headers=request_headers),
        expected,
        timeout=timeout,
    )


def download_bytes(
    url: str,
    *,
    token: str | None = None,
    headers: dict[str, str] | None = None,
    expected: set[int] | None = None,
    timeout: int = 45,
) -> bytes:
    expected = expected or {200}
    request_headers = {}
    if token:
        request_headers["Authorization"] = f"Bearer {token}"
    if headers:
        request_headers.update(headers)
    req = request.Request(url, method="GET", headers=request_headers)
    try:
        with request.urlopen(req, timeout=timeout) as response:
            raw = response.read()
            if response.status not in expected:
                raise IntegrityError(f"{url} returned {response.status}: {raw!r}")
            return raw
    except error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        raise IntegrityError(f"{url} returned HTTP {exc.code}: {raw}") from exc
    except error.URLError as exc:
        raise IntegrityError(f"{url} failed: {exc}") from exc


def multipart_request(
    method: str,
    url: str,
    *,
    fields: dict[str, str],
    files: list[tuple[str, Path, str | None]],
    token: str | None = None,
    headers: dict[str, str] | None = None,
    expected: set[int] | None = None,
    timeout: int = 60,
) -> dict | list:
    expected = expected or {200, 201, 202}
    boundary = f"----serverless-integrity-{uuid.uuid4().hex}"
    body = bytearray()

    def add_line(value: bytes = b"") -> None:
        body.extend(value)
        body.extend(b"\r\n")

    for name, value in fields.items():
        add_line(f"--{boundary}".encode())
        add_line(f'Content-Disposition: form-data; name="{name}"'.encode())
        add_line()
        add_line(str(value).encode("utf-8"))

    for field_name, path, explicit_content_type in files:
        content_type = (
            explicit_content_type
            or mimetypes.guess_type(path.name)[0]
            or "application/octet-stream"
        )
        add_line(f"--{boundary}".encode())
        add_line(
            (
                f'Content-Disposition: form-data; name="{field_name}"; '
                f'filename="{path.name}"'
            ).encode()
        )
        add_line(f"Content-Type: {content_type}".encode())
        add_line()
        body.extend(path.read_bytes())
        body.extend(b"\r\n")

    add_line(f"--{boundary}--".encode())
    request_headers = {
        "Accept": "application/json",
        "Content-Type": f"multipart/form-data; boundary={boundary}",
    }
    if token:
        request_headers["Authorization"] = f"Bearer {token}"
    if headers:
        request_headers.update(headers)
    return open_json(
        request.Request(url, data=bytes(body), method=method, headers=request_headers),
        expected,
        timeout=timeout,
    )


def poll_until(
    *,
    label: str,
    fetch,
    status_field: str,
    terminal_states: set[str],
    success_state: str,
    timeout_seconds: int,
    interval_seconds: float = 1.0,
) -> dict:
    deadline = time.monotonic() + timeout_seconds
    last = {}
    while time.monotonic() < deadline:
        last = fetch()
        state = last.get(status_field)
        print(f"{label}: {state}")
        if state in terminal_states:
            if state != success_state:
                raise IntegrityError(
                    f"{label} ended as {state}: {json.dumps(last, indent=2)}"
                )
            return last
        time.sleep(interval_seconds)
    raise IntegrityError(
        f"{label} did not finish within {timeout_seconds}s. "
        f"Last response: {json.dumps(last, indent=2)}"
    )


def register(base_url: str, prefix: str) -> tuple[dict, str]:
    suffix = uuid.uuid4().hex[:10]
    username = f"{prefix}_{suffix}"
    payload = {
        "username": username,
        "email": f"{username}@example.com",
        "password": "StrongerPass123!",
    }
    auth = json_request("POST", f"{base_url}/api/auth/register/", payload, expected={201})
    return auth, auth["access"]


def create_function(base_url: str, token: str, *, name: str) -> dict:
    return json_request(
        "POST",
        f"{base_url}/api/functions/",
        {
            "name": name,
            "description": "Real-world integrity test function.",
            "invoke_access": "private",
        },
        token=token,
        expected={201},
    )


def upload_version(
    base_url: str,
    token: str,
    function_id: int,
    bundle_path: Path,
    *,
    version: str = "v1",
) -> dict:
    return multipart_request(
        "POST",
        f"{base_url}/api/functions/{function_id}/versions/",
        fields={
            "version": version,
            "runtime": "python3.13",
            "handler": "handler.main",
            "config": json.dumps({"memory_mb": 128, "timeout_seconds": 20}),
            "invocation_input_mime_types": json.dumps(["text/plain"]),
            "invocation_input_max_files": "2",
            "invocation_input_max_size_mb": "1",
            "invocation_input_max_total_size_mb": "1",
            "declared_output_files": json.dumps(["report.txt"]),
            "invocation_output_max_files": "1",
            "invocation_output_max_file_size_mb": "1",
            "invocation_output_max_total_size_mb": "1",
        },
        files=[("source_bundle", bundle_path, "application/zip")],
        token=token,
        expected={201},
    )


def replace_source(base_url: str, token: str, function_id: int, bundle_path: Path) -> dict:
    return multipart_request(
        "POST",
        f"{base_url}/api/functions/{function_id}/source/",
        fields={},
        files=[("source_bundle", bundle_path, "application/zip")],
        token=token,
        expected={202},
    )


def build_and_wait(base_url: str, token: str, version_id: int, *, label: str) -> dict:
    json_request(
        "POST",
        f"{base_url}/api/versions/{version_id}/build/",
        token=token,
        expected={200, 202},
    )
    return poll_until(
        label=label,
        fetch=lambda: json_request(
            "GET",
            f"{base_url}/api/versions/{version_id}/",
            token=token,
        ),
        status_field="build_status",
        terminal_states=TERMINAL_BUILD_STATES,
        success_state="built",
        timeout_seconds=240,
        interval_seconds=2,
    )


def invoke_json(
    base_url: str,
    token: str,
    function_id: int,
    *,
    name: str,
    index: int,
    sleep_seconds: float,
) -> dict:
    return json_request(
        "POST",
        f"{base_url}/api/functions/{function_id}/invoke/",
        {
            "event": {
                "name": name,
                "index": index,
                "sleep_seconds": sleep_seconds,
            }
        },
        token=token,
        expected={202},
    )


def invoke_with_file(
    base_url: str,
    token: str,
    function_id: int,
    input_path: Path,
    *,
    name: str,
) -> dict:
    return multipart_request(
        "POST",
        f"{base_url}/api/functions/{function_id}/invoke/",
        fields={"event": json.dumps({"name": name, "sleep_seconds": 0})},
        files=[("files", input_path, "text/plain")],
        token=token,
        expected={202},
    )


def wait_invocation(base_url: str, token: str, invocation_id: int, *, label: str) -> dict:
    return poll_until(
        label=label,
        fetch=lambda: json_request(
            "GET",
            f"{base_url}/api/invocations/{invocation_id}/",
            token=token,
        ),
        status_field="status",
        terminal_states=TERMINAL_INVOCATION_STATES,
        success_state="succeeded",
        timeout_seconds=180,
        interval_seconds=1,
    )


def download_declared_output(base_url: str, invocation: dict) -> str:
    read_token = invocation.get("read_token")
    outputs = json_request(
        "GET",
        f"{base_url}/api/invocations/{invocation['id']}/outputs/",
        headers={"X-Invocation-Read-Token": read_token},
        expected={200},
    )
    if len(outputs) != 1 or outputs[0]["original_path"] != "report.txt":
        raise IntegrityError(f"Unexpected output list: {json.dumps(outputs, indent=2)}")
    body = download_bytes(
        f"{base_url}/api/invocations/{invocation['id']}/outputs/{outputs[0]['id']}/download/",
        headers={"X-Invocation-Read-Token": read_token},
    )
    return body.decode("utf-8")


def denied_read_with_wrong_token(base_url: str, invocation_id: int) -> int:
    url = f"{base_url}/api/invocations/{invocation_id}/outputs/"
    req = request.Request(
        url,
        method="GET",
        headers={"X-Invocation-Read-Token": "inv_wrong"},
    )
    try:
        with request.urlopen(req, timeout=30) as response:
            return response.status
    except error.HTTPError as exc:
        return exc.code


def docker_compose_exec(args: list[str], *, cwd: Path) -> str:
    completed = subprocess.run(
        ["docker", "compose", "exec", "-T", *args],
        cwd=cwd,
        text=True,
        capture_output=True,
    )
    if completed.returncode != 0:
        raise IntegrityError(
            "docker compose exec failed:\n"
            f"command={completed.args!r}\n"
            f"stdout={completed.stdout}\n"
            f"stderr={completed.stderr}"
        )
    return completed.stdout.strip()


def get_image_rows(cwd: Path, image_refs: list[str]) -> list[dict]:
    literal = repr(image_refs)
    code = (
        "from apps.functions.models import FunctionImage; "
        f"refs={literal}; "
        "import json; "
        "print(json.dumps(list(FunctionImage.objects.filter(image_ref__in=refs)"
        ".order_by('image_ref').values('image_ref','status','reason','deleted_at'))))"
    )
    output = docker_compose_exec(["backend", "python", "manage.py", "shell", "-c", code], cwd=cwd)
    return json.loads(output.splitlines()[-1] or "[]")


def cleanup_images(cwd: Path) -> str:
    return docker_compose_exec(
        [
            "backend",
            "python",
            "manage.py",
            "cleanup_function_images",
            "--registry-base-url",
            "http://registry:5000",
        ],
        cwd=cwd,
    )


def list_workers(base_url: str, token: str) -> dict:
    response = json_request("GET", f"{base_url}/api/workers/", token=token, expected={200, 403})
    if isinstance(response, dict):
        return response
    return {"count": len(response), "workers": response}


def run(
    base_url: str,
    *,
    output_json: Path,
    cwd: Path,
    skip_docker_inspection: bool = False,
) -> dict:
    base_url = base_url.rstrip("/")
    started = time.monotonic()
    auth, token = register(base_url, "integrity")
    username = auth["user"]["username"]
    print(f"registered user={username}")

    function = create_function(
        base_url,
        token,
        name=f"Integrity Function {uuid.uuid4().hex[:8]}",
    )
    function_id = function["id"]
    print(f"created function_id={function_id} slug={function['slug']}")

    with tempfile.TemporaryDirectory(prefix="serverless-integrity-") as tmp_name:
        tmp = Path(tmp_name)
        v1_bundle = tmp / "v1.zip"
        v2_bundle = tmp / "v2.zip"
        input_file = tmp / "input.txt"
        make_bundle(v1_bundle, marker="v1", sleep_seconds=0)
        make_bundle(v2_bundle, marker="v2", sleep_seconds=0)
        input_file.write_text("hello input file", encoding="utf-8")

        version = upload_version(base_url, token, function_id, v1_bundle)
        v1 = build_and_wait(base_url, token, version["id"], label="build v1")
        old_image = v1["image_ref"]
        print(f"v1 built image={old_image}")

        print("submitting concurrent v1 invocations")
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            submitted_v1 = list(
                pool.map(
                    lambda index: invoke_json(
                        base_url,
                        token,
                        function_id,
                        name=f"before-{index}",
                        index=index,
                        sleep_seconds=2,
                    ),
                    range(4),
                )
            )

        print("submitting source replacement while v1 invocations are running")
        replacement = replace_source(base_url, token, function_id, v2_bundle)
        candidate_id = replacement["candidate_version"]["id"]
        function_during_build = json_request(
            "GET",
            f"{base_url}/api/functions/{function_id}/",
            token=token,
            expected={200},
        )
        if function_during_build["active_version"]["id"] != v1["id"]:
            raise IntegrityError("Active version switched before candidate build completed.")
        if not function_during_build["pending_build"]:
            raise IntegrityError("Function detail did not expose pending_build during replacement.")

        v1_during_rebuild = invoke_json(
            base_url,
            token,
            function_id,
            name="during-rebuild",
            index=99,
            sleep_seconds=0,
        )

        v2 = poll_until(
            label="build v2",
            fetch=lambda: json_request(
                "GET",
                f"{base_url}/api/versions/{candidate_id}/",
                token=token,
            ),
            status_field="build_status",
            terminal_states=TERMINAL_BUILD_STATES,
            success_state="built",
            timeout_seconds=240,
            interval_seconds=2,
        )
        new_image = v2["image_ref"]
        print(f"v2 built image={new_image}")

        completed_v1 = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
            completed_v1 = list(
                pool.map(
                    lambda invocation: wait_invocation(
                        base_url,
                        token,
                        invocation["id"],
                        label=f"v1 invocation {invocation['id']}",
                    ),
                    [*submitted_v1, v1_during_rebuild],
                )
            )
        if {item["result"]["marker"] for item in completed_v1} != {"v1"}:
            raise IntegrityError("Some pre-promotion invocations did not run v1.")

        print("invoking after promotion")
        v2_invocations = [
            invoke_json(
                base_url,
                token,
                function_id,
                name=f"after-{index}",
                index=index,
                sleep_seconds=0,
            )
            for index in range(2)
        ]
        file_invocation = invoke_with_file(
            base_url,
            token,
            function_id,
            input_file,
            name="file-call",
        )
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
            completed_v2 = list(
                pool.map(
                    lambda invocation: wait_invocation(
                        base_url,
                        token,
                        invocation["id"],
                        label=f"v2 invocation {invocation['id']}",
                    ),
                    [*v2_invocations, file_invocation],
                )
            )
        if {item["result"]["marker"] for item in completed_v2} != {"v2"}:
            raise IntegrityError("Some post-promotion invocations did not run v2.")
        file_result = next(item for item in completed_v2 if item["id"] == file_invocation["id"])
        if file_result["result"]["input_summaries"] != [{"name": "input.txt", "size": 16}]:
            raise IntegrityError(f"Unexpected input summary: {file_result['result']['input_summaries']}")

        output_body = download_declared_output(base_url, file_invocation)
        if output_body != "v2 report for file-call":
            raise IntegrityError(f"Unexpected downloaded output body: {output_body!r}")
        wrong_token_status = denied_read_with_wrong_token(base_url, file_invocation["id"])
        if wrong_token_status not in {401, 403}:
            raise IntegrityError(f"Wrong read token returned HTTP {wrong_token_status}, expected 401/403.")

        function_invocations = json_request(
            "GET",
            f"{base_url}/api/functions/{function_id}/invocations/",
            token=token,
            expected={200},
        )
        expected_invocation_count = len(completed_v1) + len(completed_v2)
        if len(function_invocations) < expected_invocation_count:
            raise IntegrityError(
                f"Function invocation history too short: {len(function_invocations)}"
            )

    api_summary = {
        "status": "api_workload_passed",
        "username": username,
        "access_token": token,
        "function_id": function_id,
        "old_image": old_image,
        "new_image": new_image,
        "completed_v1_invocations": len(completed_v1),
        "completed_v2_invocations": len(completed_v2),
        "function_invocation_history_count": len(function_invocations),
        "downloaded_output": output_body,
        "wrong_read_token_status": wrong_token_status,
        "wall_seconds": round(time.monotonic() - started, 3),
    }
    if skip_docker_inspection:
        api_summary["status"] = "api_workload_passed_internal_checks_pending"
        output_json.parent.mkdir(parents=True, exist_ok=True)
        output_json.write_text(json.dumps(api_summary, indent=2), encoding="utf-8")
        print(json.dumps(api_summary, indent=2))
        return api_summary

    rows_before_cleanup = get_image_rows(cwd, [old_image, new_image])
    status_by_image = {row["image_ref"]: row["status"] for row in rows_before_cleanup}
    if status_by_image.get(old_image) != "pending_delete":
        raise IntegrityError(f"Old image was not pending_delete: {rows_before_cleanup}")
    if status_by_image.get(new_image) != "active":
        raise IntegrityError(f"New image was not active: {rows_before_cleanup}")

    cleanup_output = cleanup_images(cwd)
    rows_after_cleanup = get_image_rows(cwd, [old_image, new_image])
    status_by_image = {row["image_ref"]: row["status"] for row in rows_after_cleanup}
    if status_by_image.get(old_image) != "deleted":
        raise IntegrityError(f"Old image was not deleted by cleanup: {rows_after_cleanup}")
    if status_by_image.get(new_image) != "active":
        raise IntegrityError(f"Active image changed during cleanup: {rows_after_cleanup}")

    delete_status = request.urlopen(
        request.Request(
            f"{base_url}/api/functions/{function_id}/",
            method="DELETE",
            headers={"Authorization": f"Bearer {token}"},
        ),
        timeout=45,
    ).status
    if delete_status != 204:
        raise IntegrityError(f"Function delete returned HTTP {delete_status}.")
    rows_after_delete = get_image_rows(cwd, [new_image])
    if rows_after_delete[0]["status"] != "pending_delete":
        raise IntegrityError(f"Deleted function image was not pending_delete: {rows_after_delete}")

    summary = {
        **api_summary,
        "status": "passed",
        "image_rows_before_cleanup": rows_before_cleanup,
        "cleanup_output": cleanup_output,
        "image_rows_after_cleanup": rows_after_cleanup,
        "image_rows_after_function_delete": rows_after_delete,
        "wall_seconds": round(time.monotonic() - started, 3),
    }
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run real-world integrity tests for function replacement, artifacts, and image cleanup."
    )
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument(
        "--output-json",
        type=Path,
        default=Path("docs/real_world_integrity_suite_latest.json"),
    )
    parser.add_argument(
        "--skip-docker-inspection",
        action="store_true",
        help="Run API workload only; use shell management commands for image cleanup checks.",
    )
    args = parser.parse_args()
    try:
        run(
            args.base_url,
            output_json=args.output_json,
            cwd=Path(__file__).resolve().parent.parent,
            skip_docker_inspection=args.skip_docker_inspection,
        )
    except IntegrityError as exc:
        raise SystemExit(f"REAL WORLD INTEGRITY SUITE FAILED: {exc}") from exc
    print("REAL WORLD INTEGRITY SUITE PASSED")


if __name__ == "__main__":
    main()
