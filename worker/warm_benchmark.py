from __future__ import annotations

import argparse
from datetime import UTC, datetime
import json
import statistics
import uuid
from pathlib import Path
from typing import Any

from executor import DockerExecutor


def percentile(values: list[int], ratio: float) -> int | None:
    if not values:
        return None
    ordered = sorted(values)
    index = min(len(ordered) - 1, round((len(ordered) - 1) * ratio))
    return ordered[index]


def summarize_values(values: list[int]) -> dict[str, int] | None:
    if not values:
        return None
    return {
        "min": min(values),
        "median": int(statistics.median(values)),
        "p90": percentile(values, 0.9),
        "max": max(values),
    }


def summarize_runs(runs: list[dict[str, Any]]) -> dict[str, Any]:
    timing_fields = sorted(
        {
            field
            for run in runs
            for field, value in run["timing_ms"].items()
            if isinstance(value, int) and not isinstance(value, bool)
        }
    )
    return {
        "count": len(runs),
        "statuses": sorted({run["status"] for run in runs}),
        "cold_starts": sum(1 for run in runs if run["cold_start"]),
        "warm_reuses": sum(
            1 for run in runs if run["timing_ms"].get("warm_container_reused") == 1
        ),
        "duration_ms": summarize_values([run["duration_ms"] for run in runs]),
        "timing_ms": {
            field: summarize_values(
                [
                    run["timing_ms"][field]
                    for run in runs
                    if isinstance(run["timing_ms"].get(field), int)
                    and not isinstance(run["timing_ms"].get(field), bool)
                ]
            )
            for field in timing_fields
        },
    }


def detect_profile_image(executor: DockerExecutor) -> str:
    candidates = [
        tag
        for image in executor.docker_client.images.list()
        for tag in image.tags or []
        if "localhost:5000/functions/invocation-profile-" in tag
    ]
    if not candidates:
        candidates = [
            tag
            for image in executor.docker_client.images.list()
            for tag in image.tags or []
            if "localhost:5000/functions/smoke-echo-" in tag
        ]
    if not candidates:
        raise RuntimeError("No local invocation-profile or smoke-echo image found.")
    return sorted(candidates)[-1]


def run_once(
    executor: DockerExecutor,
    *,
    image_ref: str,
    function_version_id: str,
    handler: str,
    sleep_seconds: float,
    index: int,
) -> dict[str, Any]:
    request_id = f"warm-bench-{uuid.uuid4().hex[:12]}"
    result = executor.run(
        {
            "request_id": request_id,
            "function_version_id": function_version_id,
            "image_ref": image_ref,
            "handler": handler,
            "config": {"memory_mb": 128, "timeout_seconds": 20},
            "event": {
                "index": index,
                "sleep_seconds": sleep_seconds,
            },
            "declared_output_files": [],
            "invocation_output_max_total_size_mb": 10,
        }
    )
    return {
        "request_id": request_id,
        "status": result.status,
        "cold_start": result.cold_start,
        "duration_ms": result.duration_ms,
        "timing_ms": result.timing_ms,
        "result": result.result,
        "error_message": result.error_message,
    }


def run_mode(
    *,
    mode: str,
    image_ref: str,
    function_version_id: str,
    handler: str,
    sleep_seconds: float,
    count: int,
) -> list[dict[str, Any]]:
    executor = DockerExecutor(warm_enabled=(mode == "warm"))
    runs: list[dict[str, Any]] = []
    try:
        for index in range(count):
            runs.append(
                run_once(
                    executor,
                    image_ref=image_ref,
                    function_version_id=function_version_id,
                    handler=handler,
                    sleep_seconds=sleep_seconds,
                    index=index,
                )
            )
    finally:
        if executor.warm_pool is not None:
            executor.warm_pool.close()
    return runs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--image-ref")
    parser.add_argument("--handler", default="handler.main")
    parser.add_argument("--count", type=int, default=6)
    parser.add_argument("--sleep-seconds", type=float, default=0.0)
    parser.add_argument("--output-json", type=Path)
    args = parser.parse_args()

    probe = DockerExecutor(warm_enabled=False)
    image_ref = args.image_ref or detect_profile_image(probe)
    function_version_id = f"bench-{uuid.uuid4().hex[:8]}"
    cold_runs = run_mode(
        mode="cold",
        image_ref=image_ref,
        function_version_id=function_version_id,
        handler=args.handler,
        sleep_seconds=args.sleep_seconds,
        count=args.count,
    )
    warm_runs = run_mode(
        mode="warm",
        image_ref=image_ref,
        function_version_id=function_version_id,
        handler=args.handler,
        sleep_seconds=args.sleep_seconds,
        count=args.count,
    )
    output = {
        "created_at": datetime.now(UTC).isoformat(),
        "image_ref": image_ref,
        "handler": args.handler,
        "count": args.count,
        "sleep_seconds": args.sleep_seconds,
        "cold": {
            "runs": cold_runs,
            "summary": summarize_runs(cold_runs),
        },
        "warm": {
            "runs": warm_runs,
            "summary": summarize_runs(warm_runs),
            "steady_state_summary": summarize_runs(warm_runs[1:]),
        },
    }
    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(json.dumps(output["cold"]["summary"], indent=2))
    print(json.dumps(output["warm"]["summary"], indent=2))
    print(json.dumps(output["warm"]["steady_state_summary"], indent=2))


if __name__ == "__main__":
    main()
