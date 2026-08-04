from __future__ import annotations

import argparse
import concurrent.futures
from datetime import UTC, datetime
import json
import mimetypes
from pathlib import Path
import re
import statistics
import subprocess
import tempfile
import time
import uuid
import zipfile
from urllib import error, request


TERMINAL_BUILD_STATES = {"built", "failed", "cancelled"}
TERMINAL_INVOCATION_STATES = {"succeeded", "failed", "timeout", "cancelled"}
WORKER_TIMING_RE = re.compile(
    r"(?P<container>\S+)\s+\|\s+.*invocation worker timing "
    r"request_id=(?P<request_id>[0-9a-f-]+) timings=(?P<timings>\{.*\})"
)


class BenchmarkError(RuntimeError):
    pass


def percentile(values: list[int], ratio: float) -> int | None:
    if not values:
        return None
    ordered = sorted(values)
    index = min(len(ordered) - 1, round((len(ordered) - 1) * ratio))
    return ordered[index]


def summarize_values(values: list[int]) -> dict | None:
    if not values:
        return None
    return {
        "min": min(values),
        "median": int(statistics.median(values)),
        "p90": percentile(values, 0.9),
        "max": max(values),
    }


def make_benchmark_bundle(path: Path, *, label: str) -> None:
    handler = f"""
import time

MODULE_LABEL = {label!r}


def main(event, context):
    sleep_seconds = float(event.get("sleep_seconds", 0))
    index = event.get("index")
    started = time.time()
    if sleep_seconds:
        time.sleep(sleep_seconds)
    finished = time.time()
    return {{
        "label": MODULE_LABEL,
        "index": index,
        "sleep_seconds": sleep_seconds,
        "elapsed_seconds": round(finished - started, 4),
        "request_id": context.get("request_id"),
    }}
""".strip()
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("handler.py", handler + "\n")
        archive.writestr("requirements.txt", "")
        archive.writestr("config.json", "{}")


def open_json(req: request.Request, expected: set[int]) -> dict:
    try:
        with request.urlopen(req, timeout=60) as response:
            raw = response.read().decode("utf-8")
            if response.status not in expected:
                raise BenchmarkError(
                    f"{req.full_url} returned {response.status}: {raw}"
                )
            return json.loads(raw) if raw else {}
    except error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        raise BenchmarkError(f"{req.full_url} returned HTTP {exc.code}: {raw}") from exc
    except error.URLError as exc:
        raise BenchmarkError(f"{req.full_url} failed: {exc}") from exc


def json_request(
    method: str,
    url: str,
    payload: dict | None = None,
    *,
    token: str | None = None,
    expected: set[int] | None = None,
) -> dict:
    expected = expected or {200, 201, 202}
    headers = {"Accept": "application/json"}
    data = None
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
    boundary = f"----serverless-warm-bench-{uuid.uuid4().hex}"
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
    return open_json(
        request.Request(url, data=bytes(body), method=method, headers=headers),
        expected,
    )


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
                raise BenchmarkError(
                    f"{label} ended as {state}: {json.dumps(last, indent=2)}"
                )
            return last
        time.sleep(interval_seconds)
    raise BenchmarkError(
        f"{label} did not finish within {timeout_seconds}s. "
        f"Last response: {json.dumps(last, indent=2)}"
    )


def docker_compose(*args: str, timeout: int = 180) -> str:
    try:
        result = subprocess.run(
            ["docker", "compose", *args],
            check=True,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.CalledProcessError as exc:
        if args and args[0] == "logs" and exc.stdout:
            return exc.stdout
        detail = exc.stderr or exc.stdout or str(exc)
        raise BenchmarkError(
            f"docker compose {' '.join(args)} failed: {detail}"
        ) from exc
    return result.stdout


def wait_for_health(base_url: str, timeout_seconds: int = 90) -> None:
    deadline = time.monotonic() + timeout_seconds
    while time.monotonic() < deadline:
        try:
            json_request("GET", f"{base_url.rstrip('/')}/health/", expected={200})
            return
        except Exception:
            time.sleep(1)
    raise BenchmarkError("backend health check did not pass")


def register_user(base_url: str) -> str:
    suffix = uuid.uuid4().hex[:8]
    username = f"warmbench_{suffix}"
    response = json_request(
        "POST",
        f"{base_url}/api/auth/register/",
        {
            "username": username,
            "email": f"{username}@example.com",
            "password": "StrongerPass123!",
        },
        expected={201},
    )
    return response["access"]


def create_and_build_function(
    base_url: str,
    token: str,
    *,
    label: str,
    timeout_seconds: int,
) -> dict:
    suffix = uuid.uuid4().hex[:8]
    function = json_request(
        "POST",
        f"{base_url}/api/functions/",
        {
            "name": f"Warm Bench {label} {suffix}",
            "description": "Warm container routing benchmark function.",
            "invoke_access": "private",
        },
        token=token,
        expected={201},
    )
    with tempfile.TemporaryDirectory(prefix="serverless-warm-bench-") as tmp:
        bundle_path = Path(tmp) / "function.zip"
        make_benchmark_bundle(bundle_path, label=label)
        version = multipart_request(
            "POST",
            f"{base_url}/api/functions/{function['id']}/versions/",
            fields={
                "version": "v1",
                "runtime": "python3.13",
                "handler": "handler.main",
                "config": json.dumps(
                    {
                        "memory_mb": 128,
                        "timeout_seconds": timeout_seconds,
                    }
                ),
                "declared_output_files": json.dumps([]),
                "invocation_output_max_total_size_mb": "10",
            },
            files={"source_bundle": bundle_path},
            token=token,
            expected={201},
        )
    json_request(
        "POST",
        f"{base_url}/api/versions/{version['id']}/build/",
        token=token,
        expected={200, 202},
    )
    version = poll_until(
        label=f"   build {label}",
        fetch=lambda: json_request(
            "GET",
            f"{base_url}/api/versions/{version['id']}/",
            token=token,
        ),
        status_field="build_status",
        terminal_states=TERMINAL_BUILD_STATES,
        success_state="built",
        timeout_seconds=240,
        interval_seconds=3,
    )
    return {
        "function": function,
        "version": version,
    }


def submit_invocation(
    base_url: str,
    token: str,
    *,
    function_id: int,
    index: int,
    sleep_seconds: float,
    scenario: str,
) -> dict:
    started = time.monotonic()
    invocation = json_request(
        "POST",
        f"{base_url}/api/functions/{function_id}/invoke/",
        {
            "version": "v1",
            "event": {
                "index": index,
                "sleep_seconds": sleep_seconds,
                "scenario": scenario,
            },
        },
        token=token,
        expected={202},
    )
    invocation["client_submit_ms"] = int((time.monotonic() - started) * 1000)
    invocation["scenario"] = scenario
    invocation["index"] = index
    return invocation


def poll_invocation(
    base_url: str,
    token: str,
    invocation: dict,
    timeout_seconds: int,
) -> dict:
    started = time.monotonic()
    completed = poll_until(
        label=f"   {invocation['scenario']} invocation {invocation['id']}",
        fetch=lambda: json_request(
            "GET",
            f"{base_url}/api/invocations/{invocation['id']}/",
            token=token,
        ),
        status_field="status",
        terminal_states=TERMINAL_INVOCATION_STATES,
        success_state="succeeded",
        timeout_seconds=timeout_seconds,
        interval_seconds=0.5,
    )
    completed.update(
        {
            "client_submit_ms": invocation["client_submit_ms"],
            "client_poll_ms": int((time.monotonic() - started) * 1000),
            "scenario": invocation["scenario"],
            "index": invocation["index"],
        }
    )
    return completed


def run_invocation_batch(
    base_url: str,
    token: str,
    *,
    function_id: int,
    scenario: str,
    count: int,
    concurrency: int,
    sleep_seconds: float,
) -> dict:
    print(f"Running scenario {scenario}: count={count} concurrency={concurrency}")
    started = time.monotonic()
    submitted: list[dict] = []
    if concurrency == 1:
        for index in range(count):
            submitted.append(
                submit_invocation(
                    base_url,
                    token,
                    function_id=function_id,
                    index=index,
                    sleep_seconds=sleep_seconds,
                    scenario=scenario,
                )
            )
            completed = poll_invocation(
                base_url,
                token,
                submitted[-1],
                timeout_seconds=120,
            )
            submitted[-1]["completed"] = completed
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
            submitted = list(
                pool.map(
                    lambda index: submit_invocation(
                        base_url,
                        token,
                        function_id=function_id,
                        index=index,
                        sleep_seconds=sleep_seconds,
                        scenario=scenario,
                    ),
                    range(count),
                )
            )
        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
            completed_items = list(
                pool.map(
                    lambda item: poll_invocation(
                        base_url,
                        token,
                        item,
                        timeout_seconds=180,
                    ),
                    submitted,
                )
            )
        for item, completed in zip(submitted, completed_items):
            item["completed"] = completed

    completed = [item["completed"] for item in submitted]
    return {
        "name": scenario,
        "count": count,
        "concurrency": concurrency,
        "sleep_seconds": sleep_seconds,
        "wall_ms": int((time.monotonic() - started) * 1000),
        "invocations": completed,
    }


def collect_worker_timings(request_ids: set[str]) -> dict[str, dict]:
    logs = docker_compose("logs", "--no-color", "--tail=500", "worker", timeout=60)
    timings: dict[str, dict] = {}
    for line in logs.splitlines():
        match = WORKER_TIMING_RE.search(line)
        if not match:
            continue
        request_id = match.group("request_id")
        if request_id not in request_ids:
            continue
        timing = json.loads(match.group("timings"))
        timing["worker_container"] = match.group("container")
        timings[request_id] = timing
    return timings


def collect_job_metadata(invocation_ids: list[int]) -> dict[str, dict]:
    if not invocation_ids:
        return {}
    ids = ",".join(str(value) for value in invocation_ids)
    code = (
        "import json;"
        "from apps.jobs.models import Job;"
        f"rows=Job.objects.filter(invocation_id__in=[{ids}]).values("
        "'invocation_id','status','payload','coordination_version','dispatch_attempts');"
        "print(json.dumps({str(r['invocation_id']):r for r in rows},default=str))"
    )
    output = docker_compose(
        "exec",
        "-T",
        "backend",
        "python",
        "manage.py",
        "shell",
        "-c",
        code,
        timeout=60,
    )
    return json.loads(output.strip().splitlines()[-1])


def collect_worker_warm_inventory() -> list[dict]:
    code = (
        "import json,os,redis;"
        "r=redis.Redis.from_url(os.getenv('REDIS_URL','redis://redis:6379/0'),"
        "decode_responses=True);"
        "keys=sorted(r.scan_iter('orchestrator:v2:worker:*'));"
        "out=[];"
        "\nfor k in keys:\n"
        "    if k.endswith('worker-leases'):\n"
        "        continue\n"
        "    h=r.hgetall(k)\n"
        "    if h:\n"
        "        meta=json.loads(h.get('metadata') or '{}')\n"
        "        out.append({'name':h.get('name'),'status':h.get('status'),"
        "'metadata':meta})\n"
        "print(json.dumps(out))"
    )
    output = docker_compose(
        "exec",
        "-T",
        "worker",
        "python",
        "-c",
        code,
        timeout=60,
    )
    return json.loads(output.strip().splitlines()[-1])


def enrich_scenarios(scenarios: list[dict]) -> None:
    invocations = [item for scenario in scenarios for item in scenario["invocations"]]
    request_ids = {item["request_id"] for item in invocations}
    timings = collect_worker_timings(request_ids)
    metadata = collect_job_metadata([item["id"] for item in invocations])
    for item in invocations:
        item["worker_timing"] = timings.get(item["request_id"], {})
        job = metadata.get(str(item["id"]), {})
        item["job"] = job
        item["assigned_worker"] = (job.get("payload") or {}).get("assigned_worker")


def summarize_scenario(scenario: dict) -> dict:
    invocations = scenario["invocations"]
    durations = [
        item["duration_ms"]
        for item in invocations
        if isinstance(item.get("duration_ms"), int)
    ]
    worker_totals = [
        item.get("worker_timing", {}).get("worker_process_total_ms")
        for item in invocations
        if isinstance(item.get("worker_timing", {}).get("worker_process_total_ms"), int)
    ]
    executor_durations = [
        item.get("worker_timing", {}).get("executor_duration_ms")
        for item in invocations
        if isinstance(item.get("worker_timing", {}).get("executor_duration_ms"), int)
    ]
    warm_reuses = sum(
        1
        for item in invocations
        if item.get("worker_timing", {}).get("warm_container_reused") == 1
    )
    cold_starts = sum(1 for item in invocations if item.get("cold_start"))
    worker_counts: dict[str, int] = {}
    for item in invocations:
        worker = item.get("assigned_worker") or item.get("worker_timing", {}).get(
            "worker_container",
            "",
        )
        worker_counts[worker] = worker_counts.get(worker, 0) + 1
    return {
        "count": len(invocations),
        "statuses": sorted({item["status"] for item in invocations}),
        "wall_ms": scenario["wall_ms"],
        "duration_ms": summarize_values(durations),
        "worker_process_total_ms": summarize_values(worker_totals),
        "executor_duration_ms": summarize_values(executor_durations),
        "warm_reuses": warm_reuses,
        "cold_starts": cold_starts,
        "worker_counts": worker_counts,
    }


def run(base_url: str, *, output_json: Path | None) -> dict:
    base_url = base_url.rstrip("/")
    wait_for_health(base_url)
    token = register_user(base_url)

    first = create_and_build_function(
        base_url,
        token,
        label="hot",
        timeout_seconds=20,
    )
    second = create_and_build_function(
        base_url,
        token,
        label="cold",
        timeout_seconds=20,
    )

    scenarios = [
        run_invocation_batch(
            base_url,
            token,
            function_id=first["function"]["id"],
            scenario="hot_sequential",
            count=6,
            concurrency=1,
            sleep_seconds=0,
        ),
        run_invocation_batch(
            base_url,
            token,
            function_id=second["function"]["id"],
            scenario="cold_pressure",
            count=3,
            concurrency=1,
            sleep_seconds=0,
        ),
        run_invocation_batch(
            base_url,
            token,
            function_id=first["function"]["id"],
            scenario="hot_after_pressure",
            count=4,
            concurrency=1,
            sleep_seconds=0,
        ),
        run_invocation_batch(
            base_url,
            token,
            function_id=first["function"]["id"],
            scenario="hot_burst",
            count=6,
            concurrency=3,
            sleep_seconds=0,
        ),
    ]
    enrich_scenarios(scenarios)
    summary = {
        "created_at": datetime.now(UTC).isoformat(),
        "base_url": base_url,
        "functions": {
            "hot": {
                "function_id": first["function"]["id"],
                "version_id": first["version"]["id"],
                "image_ref": first["version"]["image_ref"],
            },
            "cold": {
                "function_id": second["function"]["id"],
                "version_id": second["version"]["id"],
                "image_ref": second["version"]["image_ref"],
            },
        },
        "scenarios": scenarios,
        "scenario_summary": {
            scenario["name"]: summarize_scenario(scenario) for scenario in scenarios
        },
        "worker_warm_inventory": collect_worker_warm_inventory(),
    }
    if output_json is not None:
        output_json.parent.mkdir(parents=True, exist_ok=True)
        output_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary["scenario_summary"], indent=2))
    print(json.dumps(summary["worker_warm_inventory"], indent=2))
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument("--output-json", type=Path)
    args = parser.parse_args()
    run(args.base_url, output_json=args.output_json)


if __name__ == "__main__":
    main()
