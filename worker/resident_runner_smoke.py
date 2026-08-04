from __future__ import annotations

import json
from pathlib import Path
import tempfile
import uuid
import zipfile

from builder import DockerBuilder
from executor import DockerExecutor


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
                "    return {",
                "        'ok': True,",
                "        'index': event.get('index'),",
                "        'request_id': context.get('request_id'),",
                "    }",
                "",
            ]
        ),
        encoding="utf-8",
    )
    with zipfile.ZipFile(path / "source.zip", "w") as archive:
        for item in source.rglob("*"):
            if item.is_file():
                archive.write(item, item.relative_to(source).as_posix())


def main() -> None:
    image_ref = f"localhost:5000/functions/resident-smoke-{uuid.uuid4().hex[:8]}:v1"
    with tempfile.TemporaryDirectory(prefix="resident-smoke-") as root:
        root_path = Path(root)
        make_bundle(root_path)
        DockerBuilder().build(
            {"image_ref": image_ref, "runtime": "python3.13"},
            root_path / "source.zip",
        )

        executor = DockerExecutor(warm_enabled=True)
        job = {
            "request_id": "warm-smoke-1",
            "function_version_id": "resident-smoke",
            "image_ref": image_ref,
            "handler": "handler.main",
            "config": {"memory_mb": 128, "timeout_seconds": 15},
            "event": {"index": 1, "sleep_seconds": 0},
            "declared_output_files": [],
            "invocation_output_max_total_size_mb": 10,
        }
        first = executor.run(job)
        second = executor.run({**job, "request_id": "warm-smoke-2"})
        print(
            json.dumps(
                {
                    "image_ref": image_ref,
                    "first": {
                        "status": first.status,
                        "cold_start": first.cold_start,
                        "duration_ms": first.duration_ms,
                        "timings": first.timing_ms,
                        "result": first.result,
                    },
                    "second": {
                        "status": second.status,
                        "cold_start": second.cold_start,
                        "duration_ms": second.duration_ms,
                        "timings": second.timing_ms,
                        "result": second.result,
                    },
                },
                indent=2,
                sort_keys=True,
            )
        )


if __name__ == "__main__":
    main()
