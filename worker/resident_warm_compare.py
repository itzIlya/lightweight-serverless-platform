from __future__ import annotations

import json
import statistics
import tempfile
import uuid
from pathlib import Path
import argparse
from typing import Any
import zipfile

from builder import DockerBuilder
from executor import DockerExecutor


def median(values: list[int]) -> int | None:
    if not values:
        return None
    return int(statistics.median(values))


def summarize(runs: list[dict[str, Any]]) -> dict[str, Any]:
    durations = [run["duration_ms"] for run in runs]
    executor_durations = [run["timing_ms"].get("executor_duration_ms", 0) for run in runs]
    wall_durations = [
        run["timing_ms"].get("executor_wall_with_cleanup_ms", run["duration_ms"])
        for run in runs
    ]
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
    image_ref = f"localhost:5000/functions/resident-compare-{uuid.uuid4().hex[:8]}:v1"
    with tempfile.TemporaryDirectory(prefix="resident-compare-") as root:
        root_path = Path(root)
        make_bundle(root_path)
        DockerBuilder().build(
            {"image_ref": image_ref, "runtime": "python3.13"},
            root_path / "source.zip",
        )
    return image_ref


def run_series(
    *,
    image_ref: str,
    mode: str,
    pattern: dict[str, Any],
    count: int,
) -> list[dict[str, Any]]:
    executor = DockerExecutor(warm_enabled=True)
    executor.warm_resident_runner_enabled = mode == "resident"
    runs: list[dict[str, Any]] = []
    try:
        for index in range(count):
            request_id = f"{mode}-{pattern['name']}-{uuid.uuid4().hex[:10]}"
            job = {
                "request_id": request_id,
                "function_version_id": f"{mode}-{pattern['name']}",
                "image_ref": image_ref,
                "handler": "handler.main",
                "config": {"memory_mb": 128, "timeout_seconds": 20},
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
            result = executor.run(job)
            runs.append(
                {
                    "request_id": request_id,
                    "status": result.status,
                    "cold_start": result.cold_start,
                    "duration_ms": result.duration_ms,
                    "timing_ms": result.timing_ms,
                    "result": result.result,
                }
            )
    finally:
        if executor.warm_pool is not None:
            executor.warm_pool.close()
    return runs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-json", type=Path)
    parser.add_argument("--brief", action="store_true")
    args = parser.parse_args()
    image_ref = build_image()
    patterns = [
        {"name": "noop", "sleep_seconds": 0, "write_output": False},
        {"name": "sleep1", "sleep_seconds": 1, "write_output": False},
        {"name": "output", "sleep_seconds": 0, "write_output": True},
    ]
    count = 6
    output: dict[str, Any] = {
        "image_ref": image_ref,
        "count": count,
        "patterns": {},
    }
    for pattern in patterns:
        old_runs = run_series(image_ref=image_ref, mode="old", pattern=pattern, count=count)
        new_runs = run_series(image_ref=image_ref, mode="resident", pattern=pattern, count=count)
        old_steady = old_runs[1:] if len(old_runs) > 1 else old_runs
        new_steady = new_runs[1:] if len(new_runs) > 1 else new_runs
        old_summary = summarize(old_steady)
        new_summary = summarize(new_steady)
        old_duration_median = old_summary["duration_ms"]["median"]
        new_duration_median = new_summary["duration_ms"]["median"]
        old_wall_median = old_summary["wall_ms"]["median"]
        new_wall_median = new_summary["wall_ms"]["median"]
        duration_speedup = None
        wall_speedup = None
        if old_duration_median and new_duration_median:
            duration_speedup = round(old_duration_median / new_duration_median, 2)
        if old_wall_median and new_wall_median:
            wall_speedup = round(old_wall_median / new_wall_median, 2)
        output["patterns"][pattern["name"]] = {
            "pattern": pattern,
            "old": {
                "all_runs": summarize(old_runs),
                "steady_state": old_summary,
                "runs": old_runs,
            },
            "resident": {
                "all_runs": summarize(new_runs),
                "steady_state": new_summary,
                "runs": new_runs,
            },
            "duration_speedup_x": duration_speedup,
            "speedup_x": wall_speedup,
            "wall_speedup_x": wall_speedup,
        }
    rendered = json.dumps(output, indent=2, sort_keys=True)
    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(rendered, encoding="utf-8")
    if args.brief:
        for name, data in output["patterns"].items():
            old = data["old"]["steady_state"]
            new = data["resident"]["steady_state"]
            print(
                f"{name}: old={old['duration_ms']['median']} ms "
                f"resident={new['duration_ms']['median']} ms "
                f"duration_speedup={data['duration_speedup_x']}x "
                f"old_wall={old['wall_ms']['median']} ms "
                f"resident_wall={new['wall_ms']['median']} ms "
                f"wall_speedup={data['wall_speedup_x']}x "
                f"old_exec={old['warm_runner_exec_ms']['median']} ms "
                f"resident_exec={new['warm_runner_exec_ms']['median']} ms "
                f"old_export={old['docker_export_copy_ms']['median']} ms "
                f"resident_export={new['docker_export_copy_ms']['median']} ms"
            )
        return
    print(rendered)


if __name__ == "__main__":
    main()
