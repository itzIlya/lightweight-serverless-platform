from __future__ import annotations

import argparse
import concurrent.futures
import json
import statistics
import tempfile
import time
import uuid
from pathlib import Path
from typing import Any
import zipfile

from builder import DockerBuilder
from executor import DockerExecutor


def median(values: list[int]) -> int | None:
    if not values:
        return None
    return int(statistics.median(values))


def percentile(values: list[int], ratio: float) -> int | None:
    if not values:
        return None
    ordered = sorted(values)
    index = min(len(ordered) - 1, round((len(ordered) - 1) * ratio))
    return ordered[index]


def summarize(runs: list[dict[str, Any]]) -> dict[str, Any]:
    durations = [run["duration_ms"] for run in runs]
    wall_durations = [
        run["timing_ms"].get("executor_wall_with_cleanup_ms", run["duration_ms"])
        for run in runs
    ]
    executor_durations = [run["timing_ms"].get("executor_duration_ms", 0) for run in runs]
    warm_execs = [run["timing_ms"].get("warm_runner_exec_ms", 0) for run in runs]
    docker_exports = [run["timing_ms"].get("docker_export_copy_ms", 0) for run in runs]
    input_copies = [run["timing_ms"].get("docker_input_copy_ms", 0) for run in runs]
    resident_prepares = [run["timing_ms"].get("warm_runner_prepare_ms", 0) for run in runs]
    return {
        "count": len(runs),
        "cold_starts": sum(1 for run in runs if run["cold_start"]),
        "duration_ms": {
            "median": median(durations),
            "min": min(durations) if durations else None,
            "max": max(durations) if durations else None,
        },
        "executor_duration_ms": {
            "median": median(executor_durations),
            "min": min(executor_durations) if executor_durations else None,
            "max": max(executor_durations) if executor_durations else None,
        },
        "wall_ms": {
            "median": median(wall_durations),
            "min": min(wall_durations) if wall_durations else None,
            "max": max(wall_durations) if wall_durations else None,
        },
        "warm_runner_exec_ms": {
            "median": median(warm_execs),
            "min": min(warm_execs) if warm_execs else None,
            "max": max(warm_execs) if warm_execs else None,
        },
        "docker_export_copy_ms": {
            "median": median(docker_exports),
            "min": min(docker_exports) if docker_exports else None,
            "max": max(docker_exports) if docker_exports else None,
        },
        "docker_input_copy_ms": {
            "median": median(input_copies),
            "min": min(input_copies) if input_copies else None,
            "max": max(input_copies) if input_copies else None,
        },
        "warm_runner_prepare_ms": {
            "median": median(resident_prepares),
            "min": min(resident_prepares) if resident_prepares else None,
            "max": max(resident_prepares) if resident_prepares else None,
        },
        "wall_p90_ms": percentile(wall_durations, 0.9),
    }


def make_bundle(path: Path) -> None:
    source = path / "bundle"
    source.mkdir()
    (source / "requirements.txt").write_text("", encoding="utf-8")
    (source / "handler.py").write_text(
        "\n".join(
            [
                "import time",
                "",
                "def main(event, context):",
                "    time.sleep(float(event.get('sleep_seconds', 0)))",
                "    payload = {",
                "        'ok': True,",
                "        'index': event.get('index'),",
                "        'request_id': context.get('request_id'),",
                "        'sleep_seconds': event.get('sleep_seconds', 0),",
                "    }",
                "    if event.get('write_output'):",
                "        with open('/sandbox/output/report.txt', 'w', encoding='utf-8') as handle:",
                "            handle.write('report:' + str(event.get('index')))",
                "    return payload",
                "",
            ]
        ),
        encoding="utf-8",
    )
    with zipfile.ZipFile(path / "source.zip", "w") as archive:
        for item in source.rglob("*"):
            if item.is_file():
                archive.write(item, item.relative_to(source).as_posix())


def build_image() -> str:
    image_ref = f"localhost:5000/functions/resident-concurrent-{uuid.uuid4().hex[:8]}:v1"
    with tempfile.TemporaryDirectory(prefix="resident-concurrent-") as root:
        root_path = Path(root)
        make_bundle(root_path)
        DockerBuilder().build(
            {"image_ref": image_ref, "runtime": "python3.13"},
            root_path / "source.zip",
        )
    return image_ref


def run_batch(
    *,
    executor: DockerExecutor,
    image_ref: str,
    mode: str,
    pattern: dict[str, Any],
    count: int,
    concurrency: int,
) -> tuple[list[dict[str, Any]], int]:
    started = time.monotonic()

    def run_one(index: int) -> dict[str, Any]:
        request_id = f"{mode}-{pattern['name']}-{uuid.uuid4().hex[:10]}"
        result = executor.run(
            {
                "request_id": request_id,
                "function_version_id": f"{mode}-{pattern['name']}",
                "image_ref": image_ref,
                "handler": "handler.main",
                "config": {"memory_mb": 128, "timeout_seconds": 30},
                "event": {
                    "index": index,
                    "sleep_seconds": pattern["sleep_seconds"],
                    "write_output": pattern["write_output"],
                },
                "declared_output_files": ["report.txt"] if pattern["write_output"] else [],
                "invocation_output_max_files": 1 if pattern["write_output"] else 0,
                "invocation_output_max_file_size_mb": 1,
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
        }

    runs: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
        for item in pool.map(run_one, range(count)):
            runs.append(item)
    return runs, int((time.monotonic() - started) * 1000)


def warm_up(
    *,
    executor: DockerExecutor,
    image_ref: str,
    mode: str,
    pattern: dict[str, Any],
) -> None:
    run_batch(
        executor=executor,
        image_ref=image_ref,
        mode=mode,
        pattern=pattern,
        count=1,
        concurrency=1,
    )


def compare(
    *,
    image_ref: str,
    pattern: dict[str, Any],
    count: int,
    concurrency: int,
) -> dict[str, Any]:
    old_executor = DockerExecutor(warm_enabled=True)
    old_executor.warm_resident_runner_enabled = False
    resident_executor = DockerExecutor(warm_enabled=True)
    resident_executor.warm_resident_runner_enabled = True
    try:
        warm_up(
            executor=old_executor,
            image_ref=image_ref,
            mode="old",
            pattern=pattern,
        )
        warm_up(
            executor=resident_executor,
            image_ref=image_ref,
            mode="resident",
            pattern=pattern,
        )
        old_runs, old_wall_ms = run_batch(
            executor=old_executor,
            image_ref=image_ref,
            mode="old",
            pattern=pattern,
            count=count,
            concurrency=concurrency,
        )
        resident_runs, resident_wall_ms = run_batch(
            executor=resident_executor,
            image_ref=image_ref,
            mode="resident",
            pattern=pattern,
            count=count,
            concurrency=concurrency,
        )
    finally:
        if old_executor.warm_pool is not None:
            old_executor.warm_pool.close()
        if resident_executor.warm_pool is not None:
            resident_executor.warm_pool.close()

    old_summary = summarize(old_runs)
    resident_summary = summarize(resident_runs)
    old_wall_median = old_summary["wall_ms"]["median"]
    resident_wall_median = resident_summary["wall_ms"]["median"]
    wall_speedup = None
    if old_wall_median and resident_wall_median:
        wall_speedup = round(old_wall_median / resident_wall_median, 2)

    return {
        "pattern": pattern,
        "count": count,
        "concurrency": concurrency,
        "old": {
            "summary": old_summary,
            "runs": old_runs,
            "scenario_wall_ms": old_wall_ms,
        },
        "resident": {
            "summary": resident_summary,
            "runs": resident_runs,
            "scenario_wall_ms": resident_wall_ms,
        },
        "wall_speedup_x": wall_speedup,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=12)
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--output-json", type=Path)
    parser.add_argument("--brief", action="store_true")
    args = parser.parse_args()

    image_ref = build_image()
    patterns = [
        {"name": "noop", "sleep_seconds": 0, "write_output": False},
        {"name": "sleep3", "sleep_seconds": 3, "write_output": False},
        {"name": "output", "sleep_seconds": 0, "write_output": True},
    ]

    output: dict[str, Any] = {
        "image_ref": image_ref,
        "count": args.count,
        "concurrency": args.concurrency,
        "patterns": {},
    }
    for pattern in patterns:
        output["patterns"][pattern["name"]] = compare(
            image_ref=image_ref,
            pattern=pattern,
            count=args.count,
            concurrency=args.concurrency,
        )

    rendered = json.dumps(output, indent=2, sort_keys=True)
    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(rendered, encoding="utf-8")

    if args.brief:
        for name, data in output["patterns"].items():
            old = data["old"]["summary"]
            new = data["resident"]["summary"]
            print(
                f"{name}: old_wall_median={old['wall_ms']['median']} ms "
                f"resident_wall_median={new['wall_ms']['median']} ms "
                f"wall_speedup={data['wall_speedup_x']}x "
                f"old_scenario_wall={data['old']['scenario_wall_ms']} ms "
                f"resident_scenario_wall={data['resident']['scenario_wall_ms']} ms "
                f"old_exec_median={old['executor_duration_ms']['median']} ms "
                f"resident_exec_median={new['executor_duration_ms']['median']} ms"
            )
        return

    print(rendered)


if __name__ == "__main__":
    main()
