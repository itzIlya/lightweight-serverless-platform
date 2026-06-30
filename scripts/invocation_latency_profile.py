from __future__ import annotations

import argparse
import concurrent.futures
from collections import defaultdict
from datetime import datetime
import json
from pathlib import Path
import re
import statistics
import subprocess
import tempfile
import time
import uuid
import zipfile

from concurrent_invocation_workload import (
    TERMINAL_BUILD_STATES,
    TERMINAL_INVOCATION_STATES,
    json_request,
    multipart_request,
    poll_until,
)


WORKER_TIMING_RE = re.compile(
    r"invocation worker timing request_id=(?P<request_id>[0-9a-f-]+) "
    r"timings=(?P<timings>\{.*\})"
)


def make_profile_bundle(path: Path) -> None:
    handler = """
import time


def main(event, context):
    sleep_seconds = float(event.get("sleep_seconds", 0))
    index = event.get("index")
    started = time.perf_counter()
    if sleep_seconds > 0:
        time.sleep(sleep_seconds)
    finished = time.perf_counter()
    return {
        "index": index,
        "sleep_seconds": sleep_seconds,
        "user_code_elapsed_ms": int((finished - started) * 1000),
        "request_id": context.get("request_id"),
    }
""".strip()
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("handler.py", handler + "\n")
        archive.writestr("requirements.txt", "")
        archive.writestr("config.json", "{}")


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def delta_ms(start: str | None, end: str | None) -> int | None:
    start_dt = parse_datetime(start)
    end_dt = parse_datetime(end)
    if start_dt is None or end_dt is None:
        return None
    return int((end_dt - start_dt).total_seconds() * 1000)


def create_and_build_function(base_url: str, token: str, suffix: str) -> dict:
    function = json_request(
        "POST",
        f"{base_url}/api/functions/",
        {
            "name": f"Invocation Profile {suffix}",
            "description": "Invocation latency profiling function.",
            "invoke_access": "private",
        },
        token=token,
        expected={201},
    )
    function_id = function["id"]

    with tempfile.TemporaryDirectory(prefix="serverless-profile-") as tmp:
        bundle_path = Path(tmp) / "function.zip"
        make_profile_bundle(bundle_path)
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
                        "timeout_seconds": 20,
                    }
                ),
                "declared_output_files": json.dumps([]),
            },
            files={"source_bundle": bundle_path},
            token=token,
            expected={201},
        )

    version_id = version["id"]
    json_request(
        "POST",
        f"{base_url}/api/versions/{version_id}/build/",
        token=token,
        expected={200, 202},
    )
    built_version = poll_until(
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
    return {
        "function": function,
        "version": built_version,
    }


def submit_invocation(
    base_url: str,
    token: str,
    function_id: int,
    *,
    index: int,
    sleep_seconds: float,
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
            },
        },
        token=token,
        expected={202},
    )
    invocation["client_submit_ms"] = int((time.monotonic() - started) * 1000)
    return invocation


def poll_invocation(base_url: str, token: str, invocation: dict) -> dict:
    started = time.monotonic()
    final = poll_until(
        label=f"   invocation {invocation['id']}",
        fetch=lambda: json_request(
            "GET",
            f"{base_url}/api/invocations/{invocation['id']}/",
            token=token,
        ),
        status_field="status",
        terminal_states=TERMINAL_INVOCATION_STATES,
        success_state="succeeded",
        timeout_seconds=180,
        interval_seconds=0.5,
    )
    final["client_submit_ms"] = invocation["client_submit_ms"]
    final["client_poll_until_terminal_ms"] = int((time.monotonic() - started) * 1000)
    final["queue_to_started_ms"] = delta_ms(final.get("queued_at"), final.get("started_at"))
    final["started_to_finished_ms"] = delta_ms(
        final.get("started_at"),
        final.get("finished_at"),
    )
    final["queued_to_finished_ms"] = delta_ms(
        final.get("queued_at"),
        final.get("finished_at"),
    )
    final["user_code_elapsed_ms"] = (final.get("result") or {}).get(
        "user_code_elapsed_ms"
    )
    if isinstance(final.get("duration_ms"), int) and isinstance(
        final.get("user_code_elapsed_ms"),
        int,
    ):
        final["worker_overhead_vs_user_code_ms"] = (
            final["duration_ms"] - final["user_code_elapsed_ms"]
        )
    return final


def run_scenario(
    base_url: str,
    token: str,
    function_id: int,
    *,
    name: str,
    count: int,
    sleep_seconds: float,
    concurrency: int,
) -> dict:
    print(
        f"Scenario {name}: count={count} sleep={sleep_seconds}s concurrency={concurrency}"
    )
    scenario_started = time.monotonic()
    if concurrency == 1:
        final = []
        for index in range(count):
            invocation = submit_invocation(
                base_url,
                token,
                function_id,
                index=index,
                sleep_seconds=sleep_seconds,
            )
            final.append(poll_invocation(base_url, token, invocation))
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
            submitted = list(
                pool.map(
                    lambda index: submit_invocation(
                        base_url,
                        token,
                        function_id,
                        index=index,
                        sleep_seconds=sleep_seconds,
                    ),
                    range(count),
                )
            )
        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
            final = list(
                pool.map(
                    lambda invocation: poll_invocation(base_url, token, invocation),
                    submitted,
                )
            )

    return {
        "name": name,
        "count": count,
        "sleep_seconds": sleep_seconds,
        "concurrency": concurrency,
        "client_wall_ms": int((time.monotonic() - scenario_started) * 1000),
        "invocations": final,
    }


def collect_worker_timings(request_ids: set[str]) -> dict[str, dict]:
    try:
        result = subprocess.run(
            ["docker", "compose", "logs", "--no-color", "worker"],
            check=True,
            capture_output=True,
            text=True,
            timeout=60,
        )
    except (subprocess.SubprocessError, FileNotFoundError) as exc:
        return {"_error": {"detail": str(exc)}}

    timings: dict[str, dict] = {}
    for line in result.stdout.splitlines():
        match = WORKER_TIMING_RE.search(line)
        if not match:
            continue
        request_id = match.group("request_id")
        if request_id not in request_ids:
            continue
        try:
            timings[request_id] = json.loads(match.group("timings"))
        except json.JSONDecodeError:
            continue
    return timings


def summarize_values(values: list[int]) -> dict:
    if not values:
        return {}
    return {
        "min": min(values),
        "median": int(statistics.median(values)),
        "max": max(values),
    }


def summarize_scenario(scenario: dict) -> dict:
    invocations = scenario["invocations"]
    fields = [
        "client_submit_ms",
        "queue_to_started_ms",
        "duration_ms",
        "started_to_finished_ms",
        "queued_to_finished_ms",
        "user_code_elapsed_ms",
        "worker_overhead_vs_user_code_ms",
    ]
    summary = {
        "client_wall_ms": scenario["client_wall_ms"],
        "statuses": sorted({item["status"] for item in invocations}),
    }
    for field in fields:
        summary[field] = summarize_values(
            [item[field] for item in invocations if isinstance(item.get(field), int)]
        )
    return summary


def summarize_worker_timings(scenarios: list[dict]) -> dict:
    by_scenario = {}
    timing_fields = set()
    for scenario in scenarios:
        for invocation in scenario["invocations"]:
            timing_fields.update((invocation.get("worker_timing") or {}).keys())

    for scenario in scenarios:
        by_scenario[scenario["name"]] = {}
        for field in sorted(timing_fields):
            by_scenario[scenario["name"]][field] = summarize_values(
                [
                    invocation["worker_timing"][field]
                    for invocation in scenario["invocations"]
                    if isinstance((invocation.get("worker_timing") or {}).get(field), int)
                ]
            )
    return by_scenario


def run(base_url: str, output_json: Path | None) -> dict:
    base_url = base_url.rstrip("/")
    suffix = uuid.uuid4().hex[:8]
    username = f"profile_{suffix}"
    password = "StrongerPass123!"

    print("1. Register profiling user")
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

    print("2. Create and build profiling function")
    created = create_and_build_function(base_url, token, suffix)
    function_id = created["function"]["id"]

    scenarios = [
        run_scenario(
            base_url,
            token,
            function_id,
            name="noop_sequential",
            count=5,
            sleep_seconds=0,
            concurrency=1,
        ),
        run_scenario(
            base_url,
            token,
            function_id,
            name="one_second_sequential",
            count=5,
            sleep_seconds=1,
            concurrency=1,
        ),
        run_scenario(
            base_url,
            token,
            function_id,
            name="three_second_concurrent",
            count=12,
            sleep_seconds=3,
            concurrency=12,
        ),
    ]

    request_ids = {
        invocation["request_id"]
        for scenario in scenarios
        for invocation in scenario["invocations"]
    }
    worker_timings = collect_worker_timings(request_ids)
    if "_error" not in worker_timings:
        for scenario in scenarios:
            for invocation in scenario["invocations"]:
                invocation["worker_timing"] = worker_timings.get(
                    invocation["request_id"],
                    {},
                )

    output = {
        "base_url": base_url,
        "username": username,
        "function_id": function_id,
        "function_slug": created["function"]["slug"],
        "version_id": created["version"]["id"],
        "image_ref": created["version"].get("image_ref"),
        "scenarios": scenarios,
        "scenario_summary": {
            scenario["name"]: summarize_scenario(scenario) for scenario in scenarios
        },
        "worker_timing_summary": summarize_worker_timings(scenarios),
        "worker_timing_collection": (
            "ok" if "_error" not in worker_timings else worker_timings["_error"]
        ),
    }

    if output_json:
        output_json.parent.mkdir(parents=True, exist_ok=True)
        output_json.write_text(json.dumps(output, indent=2), encoding="utf-8")

    print(json.dumps(output["scenario_summary"], indent=2))
    print(json.dumps(output["worker_timing_summary"], indent=2))
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument("--output-json", type=Path)
    args = parser.parse_args()
    run(args.base_url, args.output_json)


if __name__ == "__main__":
    main()
