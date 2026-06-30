from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import time
import uuid

from concurrent_invocation_workload import json_request
from invocation_latency_profile import (
    collect_worker_timings,
    create_and_build_function,
    run_scenario,
    summarize_scenario,
    summarize_worker_timings,
)


DEFAULT_CONCURRENCY_LEVELS = (1, 2, 4, 8, 12)


def run(
    base_url: str,
    output_json: Path,
    *,
    count: int,
    sleep_seconds: float,
    cooldown_seconds: float,
    concurrency_levels: tuple[int, ...],
) -> dict:
    base_url = base_url.rstrip("/")
    suffix = uuid.uuid4().hex[:8]
    username = f"sweep_{suffix}"
    password = "StrongerPass123!"

    print("1. Register sweep user")
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

    print("2. Create and build one instrumented function")
    created = create_and_build_function(base_url, token, suffix)
    function_id = created["function"]["id"]

    scenarios = []
    print("3. Run concurrency sweep")
    for position, concurrency in enumerate(concurrency_levels):
        if position and cooldown_seconds > 0:
            print(
                f"   cooldown {cooldown_seconds:g}s before concurrency {concurrency}"
            )
            time.sleep(cooldown_seconds)
        scenarios.append(
            run_scenario(
                base_url,
                token,
                function_id,
                name=f"concurrency_{concurrency}",
                count=count,
                sleep_seconds=sleep_seconds,
                concurrency=concurrency,
            )
        )

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
        "created_at": datetime.now(timezone.utc).isoformat(),
        "base_url": base_url,
        "username": username,
        "function_id": function_id,
        "version_id": created["version"]["id"],
        "image_ref": created["version"].get("image_ref"),
        "count_per_level": count,
        "sleep_seconds": sleep_seconds,
        "cooldown_seconds": cooldown_seconds,
        "concurrency_levels": list(concurrency_levels),
        "scenarios": scenarios,
        "scenario_summary": {
            scenario["name"]: summarize_scenario(scenario)
            for scenario in scenarios
        },
        "worker_timing_summary": summarize_worker_timings(scenarios),
        "worker_timing_collection": (
            "ok" if "_error" not in worker_timings else worker_timings["_error"]
        ),
    }

    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(json.dumps(output["scenario_summary"], indent=2))
    print(json.dumps(output["worker_timing_summary"], indent=2))
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument(
        "--output-json",
        type=Path,
        default=Path("docs/invocation_concurrency_sweep_latest.json"),
    )
    parser.add_argument("--count", type=int, default=12)
    parser.add_argument("--sleep-seconds", type=float, default=1.0)
    parser.add_argument("--cooldown-seconds", type=float, default=11.0)
    parser.add_argument(
        "--levels",
        default=",".join(str(level) for level in DEFAULT_CONCURRENCY_LEVELS),
        help="Comma-separated concurrency levels in execution order.",
    )
    args = parser.parse_args()
    concurrency_levels = tuple(
        int(value.strip()) for value in args.levels.split(",") if value.strip()
    )
    if not concurrency_levels or any(level <= 0 for level in concurrency_levels):
        parser.error("--levels must contain positive integers")
    run(
        args.base_url,
        args.output_json,
        count=args.count,
        sleep_seconds=args.sleep_seconds,
        cooldown_seconds=args.cooldown_seconds,
        concurrency_levels=concurrency_levels,
    )


if __name__ == "__main__":
    main()
