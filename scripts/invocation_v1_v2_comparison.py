from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import time
import uuid

from invocation_latency_profile import (
    WORKER_TIMING_RE,
    collect_worker_timings,
    create_and_build_function,
    json_request,
    run_scenario,
    summarize_scenario,
    summarize_worker_timings,
)


FINALIZER_TIMING_RE = re.compile(
    r"invocation finalizer timing request_id=(?P<request_id>[0-9a-f-]+) "
    r"timings=(?P<timings>\{.*\})"
)
PROJECTOR_TIMING_RE = re.compile(
    r"invocation projector timing request_id=(?P<request_id>[0-9a-f-]+) "
    r"event_type=(?P<event_type>\S+) timings=(?P<timings>\{.*\})"
)


def docker_compose(*args: str, env: dict | None = None, timeout: int = 180) -> str:
    result = subprocess.run(
        ["docker", "compose", *args],
        check=True,
        capture_output=True,
        text=True,
        env=env,
        timeout=timeout,
    )
    return result.stdout


def configure_protocol(base_url: str, protocol: str) -> None:
    env = os.environ.copy()
    env.update(
        {
            "V2_BUILD_PILOT_ENABLED": "false",
            "V2_INVOCATION_PILOT_ENABLED": "true" if protocol == "v2" else "false",
            "V2_INVOCATION_ROLLOUT_PERCENT": "100",
            "V2_CUTOVER_STAGE": "private",
            "V1_JOB_CREATION_ENABLED": "true",
            "V1_COORDINATION_ENDPOINTS_ENABLED": "true",
        }
    )
    docker_compose("up", "-d", "--force-recreate", "backend", env=env)
    deadline = time.monotonic() + 90
    while time.monotonic() < deadline:
        try:
            json_request("GET", f"{base_url}/health/", expected={200})
            return
        except Exception:
            pass
        time.sleep(1)
    raise RuntimeError(f"backend did not become healthy for protocol={protocol}")


def login(base_url: str, username: str, password: str) -> str:
    response = json_request(
        "POST",
        f"{base_url}/api/auth/token/",
        {"username": username, "password": password},
        expected={200},
    )
    return response["access"]


def register(base_url: str, username: str, password: str) -> str:
    response = json_request(
        "POST",
        f"{base_url}/api/auth/register/",
        {
            "username": username,
            "email": f"{username}@example.com",
            "password": password,
        },
        expected={201},
    )
    return response["access"]


def orchestrator_metrics() -> dict:
    code = (
        "import json,os,urllib.request;"
        "r=urllib.request.Request('http://orchestrator:8010/metrics/',"
        "headers={'X-Internal-Token':os.getenv('WORKER_SHARED_SECRET','change-me')});"
        "print(json.dumps(json.load(urllib.request.urlopen(r,timeout=10))))"
    )
    output = docker_compose("exec", "-T", "worker", "python", "-c", code)
    return json.loads(output.strip().splitlines()[-1])


def job_metadata(invocation_ids: list[int]) -> dict[str, dict]:
    ids = ",".join(str(value) for value in invocation_ids)
    code = (
        "import json;"
        "from apps.jobs.models import Job;"
        f"rows=Job.objects.filter(invocation_id__in=[{ids}]).values("
        "'invocation_id','coordination_version','dispatch_attempts','recovery_count',"
        "'payload','status');"
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
    )
    return json.loads(output.strip().splitlines()[-1])


def collect_service_timings(request_ids: set[str]) -> tuple[dict, dict]:
    finalizer_logs = docker_compose(
        "logs", "--no-color", "invocation-finalizer", timeout=60
    )
    projector_logs = docker_compose(
        "logs", "--no-color", "orchestrator-projector", timeout=60
    )
    finalizer = {}
    projector = {}
    for line in finalizer_logs.splitlines():
        match = FINALIZER_TIMING_RE.search(line)
        if match and match.group("request_id") in request_ids:
            finalizer[match.group("request_id")] = json.loads(match.group("timings"))
    for line in projector_logs.splitlines():
        match = PROJECTOR_TIMING_RE.search(line)
        if not match or match.group("request_id") not in request_ids:
            continue
        if match.group("event_type") in {"job.succeeded", "job.failed"}:
            projector[match.group("request_id")] = json.loads(
                match.group("timings")
            )
    return finalizer, projector


def run_protocol(
    base_url: str,
    token: str,
    function_id: int,
    protocol: str,
) -> dict:
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
    invocations = [item for scenario in scenarios for item in scenario["invocations"]]
    request_ids = {item["request_id"] for item in invocations}
    worker_timings = collect_worker_timings(request_ids)
    finalizer_timings, projector_timings = collect_service_timings(request_ids)
    metadata = job_metadata([item["id"] for item in invocations])
    for invocation in invocations:
        request_id = invocation["request_id"]
        invocation["worker_timing"] = worker_timings.get(request_id, {})
        invocation["finalizer_timing"] = finalizer_timings.get(request_id, {})
        invocation["projector_timing"] = projector_timings.get(request_id, {})
        invocation["job"] = metadata.get(str(invocation["id"]), {})
        result = invocation.get("result") or {}
        invocation["result_matches"] = (
            result.get("index") is not None
            and result.get("sleep_seconds")
            == scenario_for_invocation(scenarios, invocation)["sleep_seconds"]
            and result.get("request_id") == request_id
        )
    return {
        "protocol": protocol,
        "scenarios": scenarios,
        "scenario_summary": {
            scenario["name"]: summarize_scenario(scenario) for scenario in scenarios
        },
        "worker_timing_summary": summarize_worker_timings(scenarios),
        "correctness": {
            "all_succeeded": all(item["status"] == "succeeded" for item in invocations),
            "all_results_match": all(item["result_matches"] for item in invocations),
            "coordination_versions": sorted(
                {item["job"].get("coordination_version") for item in invocations}
            ),
            "recovery_count": sum(
                int(item["job"].get("recovery_count") or 0) for item in invocations
            ),
        },
    }


def scenario_for_invocation(scenarios: list[dict], invocation: dict) -> dict:
    for scenario in scenarios:
        if any(item["id"] == invocation["id"] for item in scenario["invocations"]):
            return scenario
    raise KeyError(invocation["id"])


def metric_delta(before: dict, after: dict) -> dict:
    fields = [
        "terminal_succeeded",
        "terminal_failed",
        "duplicate_dispatches",
        "duplicate_claims",
        "duplicate_completions",
        "duplicate_finalizations",
        "recovery_count",
    ]
    return {field: int(after.get(field, 0)) - int(before.get(field, 0)) for field in fields}


def run(base_url: str, output_json: Path) -> dict:
    base_url = base_url.rstrip("/")
    suffix = uuid.uuid4().hex[:8]
    username = f"protocol_compare_{suffix}"
    password = "StrongerPass123!"
    configure_protocol(base_url, "v1")
    token = register(base_url, username, password)
    created = create_and_build_function(base_url, token, suffix)
    function_id = created["function"]["id"]
    output = {
        "base_url": base_url,
        "username": username,
        "function_id": function_id,
        "version_id": created["version"]["id"],
        "image_ref": created["version"].get("image_ref"),
        "worker_count": 3,
        "runs": {},
    }
    try:
        token = login(base_url, username, password)
        output["runs"]["v1"] = run_protocol(
            base_url, token, function_id, "v1"
        )
        configure_protocol(base_url, "v2")
        token = login(base_url, username, password)
        metrics_before = orchestrator_metrics()
        output["runs"]["v2"] = run_protocol(
            base_url, token, function_id, "v2"
        )
        metrics_after = orchestrator_metrics()
        output["runs"]["v2"]["metrics_before"] = metrics_before
        output["runs"]["v2"]["metrics_after"] = metrics_after
        output["runs"]["v2"]["metrics_delta"] = metric_delta(
            metrics_before,
            metrics_after,
        )
    finally:
        configure_protocol(base_url, "v1")
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(output, indent=2), encoding="utf-8")
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument(
        "--output-json",
        type=Path,
        default=Path("docs/invocation_v1_v2_comparison_2026-07-02.json"),
    )
    args = parser.parse_args()
    output = run(args.base_url, args.output_json)
    print(json.dumps({key: value["scenario_summary"] for key, value in output["runs"].items()}, indent=2))


if __name__ == "__main__":
    main()
