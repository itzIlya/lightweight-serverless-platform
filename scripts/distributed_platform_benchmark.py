from __future__ import annotations

import argparse
import concurrent.futures
from datetime import UTC, datetime
import json
import mimetypes
import random
import re
import statistics
import subprocess
import tempfile
import time
import uuid
import zipfile
from pathlib import Path
from urllib import error, request


TERMINAL_BUILD_STATES = {"built", "failed", "cancelled"}
TERMINAL_INVOCATION_STATES = {"succeeded", "failed", "timeout", "cancelled"}
TIMING_RE = re.compile(
    r"request_id=(?P<request_id>[0-9a-f-]+) timings=(?P<timings>\{.*\})"
)


class BenchmarkError(RuntimeError):
    pass


def percentile(values: list[float], ratio: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    index = min(len(ordered) - 1, round((len(ordered) - 1) * ratio))
    return round(ordered[index], 3)


def summarize(values: list[float]) -> dict:
    if not values:
        return {"count": 0}
    return {
        "count": len(values),
        "min": round(min(values), 3),
        "median": round(statistics.median(values), 3),
        "p90": percentile(values, 0.90),
        "p95": percentile(values, 0.95),
        "max": round(max(values), 3),
    }


def open_json(req: request.Request, expected: set[int]) -> dict:
    retryable_http_statuses = {502, 503, 504}
    last_detail = ""
    for attempt in range(1, 4):
        try:
            with request.urlopen(req, timeout=90) as response:
                raw = response.read().decode("utf-8")
                if response.status not in expected:
                    raise BenchmarkError(f"{req.full_url} returned {response.status}: {raw}")
                return json.loads(raw) if raw else {}
        except error.HTTPError as exc:
            raw = exc.read().decode("utf-8", errors="replace")
            last_detail = f"{req.full_url} returned HTTP {exc.code}: {raw}"
            if exc.code not in retryable_http_statuses:
                raise BenchmarkError(last_detail) from exc
        except error.URLError as exc:
            last_detail = f"{req.full_url} failed: {exc}"
        if attempt < 3:
            time.sleep(attempt)
    raise BenchmarkError(last_detail)


def json_request(
    method: str,
    url: str,
    payload: dict | None = None,
    *,
    token: str | None = None,
    extra_headers: dict[str, str] | None = None,
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
    if extra_headers:
        headers.update(extra_headers)
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
    boundary = f"----serverless-benchmark-{uuid.uuid4().hex}"
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


class RemoteControl:
    def __init__(self, *, key: Path, control_host: str, workers: list[str]) -> None:
        self.key = key
        self.control_host = control_host
        self.workers = workers
        self.known_hosts = key.parent / "known_hosts"

    def ssh_control(self, command: str, timeout: int = 60) -> str:
        return self._run(
            [
                "ssh",
                "-o",
                "BatchMode=yes",
                "-o",
                "StrictHostKeyChecking=accept-new",
                "-o",
                f"UserKnownHostsFile={self.known_hosts}",
                "-i",
                str(self.key),
                f"ubuntu@{self.control_host}",
                command,
            ],
            timeout=timeout,
        )

    def ssh_worker(self, worker: str, command: str, timeout: int = 60) -> str:
        proxy = (
            f"ssh -o BatchMode=yes -o StrictHostKeyChecking=accept-new "
            f"-o UserKnownHostsFile={self.known_hosts} -i {self.key} "
            f"-W %h:%p ubuntu@{self.control_host}"
        )
        return self._run(
            [
                "ssh",
                "-o",
                "BatchMode=yes",
                "-o",
                "StrictHostKeyChecking=accept-new",
                "-o",
                f"UserKnownHostsFile={self.known_hosts}",
                "-o",
                f"ProxyCommand={proxy}",
                "-i",
                str(self.key),
                f"ubuntu@{worker}",
                command,
            ],
            timeout=timeout,
        )

    def set_worker_invocation_concurrency(
        self,
        *,
        invocation_concurrency: int,
        build_concurrency: int = 1,
    ) -> None:
        total_concurrency = invocation_concurrency + build_concurrency
        update_env = f"""
cd /home/ubuntu/serverless-platform-worker
python3 - <<'PY'
from pathlib import Path

path = Path(".env.worker")
updates = {{
    "WORKER_MAX_CONCURRENCY": "{total_concurrency}",
    "WORKER_MAX_INVOCATION_CONCURRENCY": "{invocation_concurrency}",
    "WORKER_MAX_BUILD_CONCURRENCY": "{build_concurrency}",
}}
lines = path.read_text(encoding="utf-8").splitlines()
seen = set()
new_lines = []
for line in lines:
    key = line.split("=", 1)[0] if "=" in line else ""
    if key in updates:
        new_lines.append(f"{{key}}={{updates[key]}}")
        seen.add(key)
    else:
        new_lines.append(line)
for key, value in updates.items():
    if key not in seen:
        new_lines.append(f"{{key}}={{value}}")
path.write_text("\\n".join(new_lines) + "\\n", encoding="utf-8")
PY
docker compose --env-file .env.worker -f docker-compose.worker.yml up -d --force-recreate worker
"""
        for worker in self.workers:
            self.ssh_worker(worker, update_env, timeout=240)

    def wait_for_worker_invocation_concurrency(
        self,
        *,
        invocation_concurrency: int,
        timeout_seconds: int = 120,
    ) -> dict:
        deadline = time.monotonic() + timeout_seconds
        last = {}
        while time.monotonic() < deadline:
            last = self.snapshot()
            workers_online = all(w["status"] == "online" for w in last["workers"])
            configs_match = all(
                int((w.get("metadata") or {}).get("max_invocation_concurrency", 0) or 0)
                == invocation_concurrency
                for w in last["workers"]
            )
            if workers_online and configs_match:
                return last
            time.sleep(2)
        raise BenchmarkError(
            "workers did not publish requested invocation concurrency "
            f"{invocation_concurrency}: {json.dumps(last, indent=2)}"
        )

    def _run(self, args: list[str], *, timeout: int) -> str:
        attempts = 6 if args and args[0] == "ssh" else 1
        last_detail = ""
        for attempt in range(1, attempts + 1):
            try:
                result = subprocess.run(
                    args,
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                )
            except subprocess.TimeoutExpired as exc:
                last_detail = f"command timed out after {timeout}s: {exc}"
            else:
                if result.returncode == 0:
                    return result.stdout
                last_detail = result.stderr.strip() or result.stdout.strip()
            if attempt < attempts:
                time.sleep(min(15, 2 * attempt))
        raise BenchmarkError(last_detail)

    def snapshot(self) -> dict:
        queue_names = [
            "scheduler-pending-invocations",
            "scheduler-pending-builds",
            "worker:worker-1:invocations",
            "worker:worker-2:invocations",
            "worker:worker-1:builds",
            "worker:worker-2:builds",
            "worker:worker-1:processing",
            "worker:worker-2:processing",
        ]
        queue_script = "\n".join(
            [
                f'printf "{name}="; docker compose --env-file .env.control-plane '
                f'-f docker-compose.control-plane.yml exec -T redis redis-cli llen {name}'
                for name in queue_names
            ]
        )
        psql = (
            "workers=$(docker compose --env-file .env.control-plane "
            "-f docker-compose.control-plane.yml exec -T postgres "
            "psql -U serverless -d serverless -Atc "
            "\"select coalesce(json_agg(json_build_object("
            "'name', name, "
            "'status', status, "
            "'metadata', metadata, "
            "'last_seen_at', last_seen_at"
            ")), '[]'::json) from workers_workernode;\"); "
            "active=$(docker compose --env-file .env.control-plane "
            "-f docker-compose.control-plane.yml exec -T postgres "
            "psql -U serverless -d serverless -Atc "
            "\"select count(*) from invocations_invocation "
            "where status in ('queued','running','finalizing');\"); "
            "printf '{\"workers\":%s,\"active_invocations\":%s}\\n' "
            "\"$workers\" \"$active\""
        )
        raw = self.ssh_control(
            "cd /home/ubuntu/serverless-platform-current; "
            f"{queue_script}\n{psql}",
            timeout=120,
        )
        queues = {}
        lines = raw.strip().splitlines()
        for line in lines[:-1]:
            if "=" not in line:
                continue
            name, value = line.split("=", 1)
            try:
                queues[name] = int(value.strip())
            except ValueError:
                queues[name] = value.strip()
        db_json = json.loads(lines[-1])
        return {"queues": queues, **db_json}

    def wait_for_isolation(self, *, timeout_seconds: int = 120) -> dict:
        deadline = time.monotonic() + timeout_seconds
        last = {}
        while time.monotonic() < deadline:
            last = self.snapshot()
            queues_empty = all(value == 0 for value in last["queues"].values())
            workers_online = all(w["status"] == "online" for w in last["workers"])
            metadata_clean = all(
                int((w.get("metadata") or {}).get("active_jobs", 0) or 0) == 0
                and int((w.get("metadata") or {}).get("active_invocations", 0) or 0) == 0
                and int((w.get("metadata") or {}).get("active_builds", 0) or 0) == 0
                for w in last["workers"]
            )
            if (
                queues_empty
                and workers_online
                and metadata_clean
                and int(last["active_invocations"]) == 0
            ):
                return last
            time.sleep(2)
        raise BenchmarkError(f"platform did not become isolated: {json.dumps(last, indent=2)}")

    def collect_worker_timings(self, *, since: datetime) -> dict[str, dict]:
        since_arg = since.isoformat().replace("+00:00", "Z")
        timings: dict[str, dict] = {}
        for worker in self.workers:
            try:
                raw = self.ssh_worker(
                    worker,
                    "cd /home/ubuntu/serverless-platform-worker; "
                    f"docker compose --env-file .env.worker -f docker-compose.worker.yml "
                    f"logs --since {since_arg} worker",
                    timeout=90,
                )
            except BenchmarkError as exc:
                print(f"warning: could not collect worker logs from {worker}: {exc}")
                continue
            for line in raw.splitlines():
                if "invocation worker timing" not in line:
                    continue
                match = TIMING_RE.search(line)
                if not match:
                    continue
                try:
                    timings[match.group("request_id")] = json.loads(match.group("timings"))
                except json.JSONDecodeError:
                    continue
        return timings


def make_bundle(path: Path, *, kind: str) -> None:
    if kind == "tiny":
        handler = """
def main(event, context):
    return {
        "kind": "tiny",
        "index": event.get("index"),
        "value": event.get("value", 1) + 1,
        "request_id": context.get("request_id"),
    }
""".strip()
        requirements = ""
        outputs: list[str] = []
        input_types: list[str] = []
    elif kind == "sleep":
        handler = """
import time


def main(event, context):
    sleep_seconds = float(event.get("sleep_seconds", 1))
    started = time.time()
    time.sleep(sleep_seconds)
    return {
        "kind": "sleep",
        "index": event.get("index"),
        "sleep_seconds": sleep_seconds,
        "elapsed_seconds": round(time.time() - started, 4),
        "request_id": context.get("request_id"),
    }
""".strip()
        requirements = ""
        outputs = []
        input_types = []
    elif kind == "dependency":
        handler = """
import numpy as np


def main(event, context):
    values = np.array(event.get("values", [1, 2, 3, 4]), dtype=float)
    return {
        "kind": "dependency",
        "index": event.get("index"),
        "mean": float(values.mean()),
        "sum": float(values.sum()),
        "request_id": context.get("request_id"),
    }
""".strip()
        requirements = "numpy\n"
        outputs = []
        input_types = []
    elif kind == "output":
        handler = """
import os


def main(event, context):
    output_dir = os.environ["FUNCTION_OUTPUT_DIR"]
    body = f"index={event.get('index')} value={event.get('value', 'ok')}"
    with open(os.path.join(output_dir, "report.txt"), "w", encoding="utf-8") as f:
        f.write(body)
    return {
        "kind": "output",
        "index": event.get("index"),
        "bytes": len(body.encode("utf-8")),
        "request_id": context.get("request_id"),
    }
""".strip()
        requirements = ""
        outputs = ["report.txt"]
        input_types = []
    elif kind == "input_output":
        handler = """
import os


def main(event, context):
    files = context.get("input_files", [])
    total = 0
    names = []
    for item in files:
        names.append(item.get("original_name"))
        with open(item["path"], "rb") as f:
            total += len(f.read())
    output_dir = os.environ["FUNCTION_OUTPUT_DIR"]
    with open(os.path.join(output_dir, "summary.txt"), "w", encoding="utf-8") as f:
        f.write(f"files={len(files)} bytes={total}")
    return {
        "kind": "input_output",
        "index": event.get("index"),
        "file_count": len(files),
        "total_bytes": total,
        "names": names,
        "request_id": context.get("request_id"),
    }
""".strip()
        requirements = ""
        outputs = ["summary.txt"]
        input_types = ["text/plain"]
    else:
        raise BenchmarkError(f"unknown function kind: {kind}")

    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("handler.py", handler + "\n")
        archive.writestr("requirements.txt", requirements)
        archive.writestr("config.json", "{}")
    path.with_suffix(".meta.json").write_text(
        json.dumps({"outputs": outputs, "input_types": input_types}),
        encoding="utf-8",
    )


def poll_until(fetch, *, status_field: str, terminal: set[str], success: str, timeout: int) -> dict:
    deadline = time.monotonic() + timeout
    last = {}
    while time.monotonic() < deadline:
        last = fetch()
        state = last.get(status_field)
        if state in terminal:
            if state != success:
                raise BenchmarkError(json.dumps(last, indent=2))
            return last
        time.sleep(1)
    raise BenchmarkError(f"poll timed out: {json.dumps(last, indent=2)}")


def register_user(base_url: str) -> dict:
    suffix = uuid.uuid4().hex[:8]
    return json_request(
        "POST",
        f"{base_url}/api/auth/register/",
        {
            "username": f"bench_{suffix}",
            "email": f"bench_{suffix}@example.com",
            "password": "StrongerPass123!",
        },
        expected={201},
    )


def refresh_auth(base_url: str, auth: dict) -> dict:
    refreshed = json_request(
        "POST",
        f"{base_url}/api/auth/token/refresh/",
        {"refresh": auth["refresh"]},
        expected={200},
    )
    auth["access"] = refreshed["access"]
    auth["refresh"] = refreshed.get("refresh") or auth["refresh"]
    return auth


def create_build_function(base_url: str, token: str, *, kind: str) -> dict:
    suffix = uuid.uuid4().hex[:8]
    function = json_request(
        "POST",
        f"{base_url}/api/functions/",
        {
            "name": f"Bench {kind} {suffix}",
            "description": f"Distributed benchmark function: {kind}",
            "invoke_access": "private",
        },
        token=token,
        expected={201},
    )
    with tempfile.TemporaryDirectory(prefix=f"serverless-bench-{kind}-") as tmp:
        bundle = Path(tmp) / "function.zip"
        make_bundle(bundle, kind=kind)
        meta = json.loads(bundle.with_suffix(".meta.json").read_text(encoding="utf-8"))
        version = multipart_request(
            "POST",
            f"{base_url}/api/functions/{function['id']}/versions/",
            fields={
                "version": "v1",
                "runtime": "python3.13",
                "handler": "handler.main",
                "config": json.dumps({"memory_mb": 256, "timeout_seconds": 20}),
                "declared_output_files": json.dumps(meta["outputs"]),
                "invocation_input_mime_types": json.dumps(meta["input_types"]),
                "invocation_input_max_files": "1",
                "invocation_input_max_size_mb": "10",
                "invocation_input_max_total_size_mb": "10",
                "invocation_output_max_files": str(max(1, len(meta["outputs"]))),
                "invocation_output_max_file_size_mb": "10",
                "invocation_output_max_total_size_mb": "10",
            },
            files={"source_bundle": bundle},
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
        lambda: json_request("GET", f"{base_url}/api/versions/{version['id']}/", token=token),
        status_field="build_status",
        terminal=TERMINAL_BUILD_STATES,
        success="built",
        timeout=360,
    )
    return {
        "kind": kind,
        "function_id": function["id"],
        "version_id": version["id"],
        "image_ref": version["image_ref"],
        "outputs": meta["outputs"],
        "input_types": meta["input_types"],
    }


def invoke_once(base_url: str, token: str, function: dict, *, index: int) -> dict:
    kind = function["kind"]
    event = {"index": index, "value": index}
    if kind == "sleep":
        event["sleep_seconds"] = 1
    if kind == "dependency":
        event["values"] = [index, index + 1, index + 2]

    submit_started = time.monotonic()
    if kind == "input_output":
        with tempfile.TemporaryDirectory(prefix="serverless-bench-input-") as tmp:
            input_path = Path(tmp) / "input.txt"
            input_path.write_text(f"hello from invocation {index}\n", encoding="utf-8")
            invocation = multipart_request(
                "POST",
                f"{base_url}/api/functions/{function['function_id']}/invoke/?response_mode=advanced",
                fields={"event": json.dumps(event), "version": "v1"},
                files={"input_files": input_path},
                token=token,
                expected={202},
            )
    else:
        invocation = json_request(
            "POST",
            f"{base_url}/api/functions/{function['function_id']}/invoke/?response_mode=advanced",
            {"version": "v1", "event": event},
            token=token,
            expected={202},
        )
    accepted_at = time.monotonic()

    final = poll_until(
        lambda: json_request(
            "GET",
            f"{base_url}/api/invocations/{invocation['id']}/?response_mode=advanced",
            token=token,
        ),
        status_field="status",
        terminal=TERMINAL_INVOCATION_STATES,
        success="succeeded",
        timeout=180,
    )
    terminal_at = time.monotonic()

    output_list_seconds = 0.0
    output_download_seconds = 0.0
    if function["outputs"]:
        output_started = time.monotonic()
        outputs = json_request(
            "GET",
            f"{base_url}/api/invocations/{invocation['id']}/outputs/",
            token=token,
        )
        output_list_seconds = time.monotonic() - output_started
        if outputs:
            download_started = time.monotonic()
            req = request.Request(
                f"{base_url}/api/invocations/{invocation['id']}/outputs/{outputs[0]['id']}/download/",
                method="GET",
                headers={"Authorization": f"Bearer {token}"},
            )
            with request.urlopen(req, timeout=60) as response:
                response.read()
            output_download_seconds = time.monotonic() - download_started

    return {
        "id": invocation["id"],
        "request_id": invocation["request_id"],
        "kind": kind,
        "status": final["status"],
        "worker_name": (final.get("attempts") or [{}])[-1].get("worker_name"),
        "cold_start": final.get("cold_start"),
        "duration_ms": final.get("duration_ms"),
        "accept_seconds": accepted_at - submit_started,
        "terminal_seconds": terminal_at - submit_started,
        "poll_seconds": terminal_at - accepted_at,
        "output_list_seconds": output_list_seconds,
        "output_download_seconds": output_download_seconds,
        "result": final.get("result"),
    }


def run_invocation_batch(
    base_url: str,
    auth: dict,
    functions: dict[str, dict],
    *,
    scenario: str,
    count: int,
    concurrency: int,
    worker_invocation_concurrency: int | None,
    repeat: int,
    plan: list[str],
    remote: RemoteControl,
) -> dict:
    print(
        f"preflight: {scenario} count={count} "
        f"worker_invocation_concurrency={worker_invocation_concurrency or 'fixed'} "
        f"saturation_concurrency={concurrency} repeat={repeat}"
    )
    before = remote.wait_for_isolation()
    refresh_auth(base_url, auth)
    token = auth["access"]
    since = datetime.now(UTC)
    started = time.monotonic()
    results: list[dict] = []
    failures: list[str] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = [
            pool.submit(
                invoke_once,
                base_url,
                token,
                functions[kind],
                index=(repeat * 100000) + index,
            )
            for index, kind in enumerate(plan)
        ]
        for future in concurrent.futures.as_completed(futures):
            try:
                results.append(future.result())
            except Exception as exc:
                failures.append(str(exc))
    wall_seconds = time.monotonic() - started
    after = remote.wait_for_isolation()
    worker_timings = remote.collect_worker_timings(since=since)
    for item in results:
        item["worker_timing_ms"] = worker_timings.get(item["request_id"], {})

    run = {
        "scenario": scenario,
        "count": count,
        "concurrency": concurrency,
        "saturation_concurrency": concurrency,
        "worker_invocation_concurrency": worker_invocation_concurrency,
        "cluster_invocation_capacity": (
            worker_invocation_concurrency * len(remote.workers)
            if worker_invocation_concurrency
            else None
        ),
        "repeat": repeat,
        "wall_seconds": wall_seconds,
        "throughput_per_second": len(results) / wall_seconds if wall_seconds else 0,
        "successes": len(results),
        "failures": failures,
        "before": before,
        "after": after,
        "invocations": sorted(results, key=lambda x: x["id"]),
    }
    print(
        f"done: {scenario} worker_invocation_c={worker_invocation_concurrency or 'fixed'} "
        f"saturation_c={concurrency} r={repeat} "
        f"success={len(results)}/{count} wall={wall_seconds:.2f}s"
    )
    return run


def summarize_run(run: dict) -> dict:
    invocations = run["invocations"]
    timing_keys = sorted(
        {
            key
            for item in invocations
            for key, value in (item.get("worker_timing_ms") or {}).items()
            if isinstance(value, int | float)
        }
    )
    return {
        "scenario": run["scenario"],
        "count": run["count"],
        "concurrency": run["concurrency"],
        "saturation_concurrency": run.get("saturation_concurrency", run["concurrency"]),
        "worker_invocation_concurrency": run.get("worker_invocation_concurrency"),
        "cluster_invocation_capacity": run.get("cluster_invocation_capacity"),
        "repeat": run["repeat"],
        "wall_seconds": round(run["wall_seconds"], 3),
        "throughput_per_second": round(run["throughput_per_second"], 3),
        "successes": run["successes"],
        "failures": len(run["failures"]),
        "terminal_seconds": summarize([i["terminal_seconds"] for i in invocations]),
        "accept_seconds": summarize([i["accept_seconds"] for i in invocations]),
        "output_download_seconds": summarize(
            [i["output_download_seconds"] for i in invocations if i["output_download_seconds"]]
        ),
        "workers": {
            worker: sum(1 for i in invocations if i.get("worker_name") == worker)
            for worker in sorted({i.get("worker_name") for i in invocations if i.get("worker_name")})
        },
        "cold_starts": sum(1 for i in invocations if i.get("cold_start")),
        "worker_timing_ms": {
            key: summarize(
                [
                    float(i["worker_timing_ms"][key])
                    for i in invocations
                    if key in i.get("worker_timing_ms", {})
                ]
            )
            for key in timing_keys
        },
    }


def write_report(path: Path, *, functions: dict, runs: list[dict]) -> None:
    summaries = [summarize_run(run) for run in runs]
    varies_worker_concurrency = any(
        item.get("worker_invocation_concurrency") is not None for item in summaries
    )
    lines = [
        (
            "# Distributed Worker Concurrency Benchmark"
            if varies_worker_concurrency
            else "# Distributed Platform Benchmark"
        ),
        "",
        f"Generated: {datetime.now(UTC).isoformat()}",
        "",
        "## Terminology",
        "",
        "- `Saturation Concurrency` is the number of simultaneous client-side invocation requests this benchmark keeps in flight.",
        "- `Worker Invocation Concurrency` is the `WORKER_MAX_INVOCATION_CONCURRENCY` value configured on each worker.",
        "- `Cluster Invocation Capacity` is worker count multiplied by worker invocation concurrency.",
        (
            "- This report varies worker execution concurrency and saturation concurrency."
            if varies_worker_concurrency
            else "- Worker execution concurrency is configured on each worker with `WORKER_MAX_INVOCATION_CONCURRENCY` and was held constant during these runs."
        ),
        "",
        "## Built Functions",
        "",
    ]
    for function in functions.values():
        lines.append(
            f"- `{function['kind']}`: function `{function['function_id']}`, "
            f"version `{function['version_id']}`, image `{function['image_ref']}`"
        )
    lines.extend(["", "## Run Summary", ""])
    if varies_worker_concurrency:
        lines.append(
            "| Scenario | Count | Worker Invocation Concurrency | Cluster Invocation Capacity | Saturation Concurrency | Repeat | Success | Fail | Wall s | Throughput/s | Median terminal s | P95 terminal s | Workers |"
        )
        lines.append(
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|"
        )
    else:
        lines.append(
            "| Scenario | Count | Saturation Concurrency | Repeat | Success | Fail | Wall s | Throughput/s | Median terminal s | P95 terminal s | Workers |"
        )
        lines.append(
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|"
        )
    for item in summaries:
        terminal = item["terminal_seconds"]
        workers = ", ".join(f"{k}:{v}" for k, v in item["workers"].items())
        if varies_worker_concurrency:
            lines.append(
                f"| {item['scenario']} | {item['count']} | "
                f"{item.get('worker_invocation_concurrency', '')} | "
                f"{item.get('cluster_invocation_capacity', '')} | "
                f"{item['saturation_concurrency']} | {item['repeat']} | "
                f"{item['successes']} | {item['failures']} | "
                f"{item['wall_seconds']} | {item['throughput_per_second']} | "
                f"{terminal.get('median', '')} | {terminal.get('p95', '')} | {workers} |"
            )
        else:
            lines.append(
                f"| {item['scenario']} | {item['count']} | "
                f"{item['saturation_concurrency']} | "
                f"{item['repeat']} | {item['successes']} | {item['failures']} | "
                f"{item['wall_seconds']} | {item['throughput_per_second']} | "
                f"{terminal.get('median', '')} | {terminal.get('p95', '')} | {workers} |"
            )
    lines.extend(["", "## Detailed JSON Summary", "", "```json"])
    lines.append(json.dumps(summaries, indent=2))
    lines.extend(["```", ""])
    path.write_text("\n".join(lines), encoding="utf-8")
    path.with_suffix(".json").write_text(json.dumps(runs, indent=2, default=str), encoding="utf-8")


def build_plans(function_kinds: list[str], *, mixed_counts: list[int] | None = None) -> list[tuple[str, int, list[str]]]:
    plans: list[tuple[str, int, list[str]]] = []
    for kind in function_kinds:
        plans.append((f"single-{kind}", 12, [kind] * 12))
    weights = [
        ("tiny", 60),
        ("sleep", 20),
        ("dependency", 10),
        ("input_output", 10),
    ]
    for count in mixed_counts or [15, 30, 80]:
        plan: list[str] = []
        for kind, percent in weights:
            plan.extend([kind] * round(count * percent / 100))
        while len(plan) < count:
            plan.append("tiny")
        plan = plan[:count]
        random.Random(1000 + count).shuffle(plan)
        plans.append((f"mixed-{count}", count, plan))
    return plans


def main() -> None:
    parser = argparse.ArgumentParser(description="Benchmark the distributed deployment.")
    parser.add_argument("--base-url", default="http://37.32.36.255")
    parser.add_argument("--ssh-key", default="local-ssh-keys/codex_deploy_ed25519")
    parser.add_argument("--control-host", default="37.32.36.255")
    parser.add_argument("--workers", nargs="+", default=["10.42.1.56", "10.42.1.149"])
    parser.add_argument("--repeats", type=int, default=3)
    parser.add_argument(
        "--worker-invocation-concurrency",
        nargs="+",
        type=int,
        default=[],
        help=(
            "Worker execution concurrency values to test. When provided, the script "
            "updates WORKER_MAX_INVOCATION_CONCURRENCY on each worker, restarts the "
            "worker service, and runs the workload matrix for each value."
        ),
    )
    parser.add_argument(
        "--concurrency",
        nargs="+",
        type=int,
        default=[2, 4, 8],
        help=(
            "Saturation/client-side concurrency: number of simultaneous invocation "
            "requests the benchmark keeps in flight. This does not change worker "
            "execution concurrency."
        ),
    )
    parser.add_argument("--single-count", type=int, default=12)
    parser.add_argument(
        "--mixed-counts",
        nargs="+",
        type=int,
        default=[15, 30, 80],
        help="Mixed workload invocation counts to generate.",
    )
    parser.add_argument("--output", default="benchmark-results/distributed-benchmark.md")
    parser.add_argument("--skip-single", action="store_true")
    parser.add_argument("--skip-mixed", action="store_true")
    parser.add_argument(
        "--only-scenarios",
        default="",
        help="Comma-separated scenario names to run, for resuming partial benchmarks.",
    )
    args = parser.parse_args()

    base_url = args.base_url.rstrip("/")
    remote = RemoteControl(
        key=Path(args.ssh_key).resolve(),
        control_host=args.control_host,
        workers=args.workers,
    )
    print("health check")
    json_request("GET", f"{base_url}/health/", expected={200})
    remote.wait_for_isolation()

    print("register benchmark user")
    auth = register_user(base_url)
    token = auth["access"]
    functions = {}
    for kind in ["tiny", "sleep", "dependency", "output", "input_output"]:
        print(f"build function: {kind}")
        functions[kind] = create_build_function(base_url, token, kind=kind)
        remote.wait_for_isolation()
        refresh_auth(base_url, auth)
        token = auth["access"]

    plans: list[tuple[str, int, list[str]]] = []
    if not args.skip_single:
        for kind in functions:
            plans.append((f"single-{kind}", args.single_count, [kind] * args.single_count))
    if not args.skip_mixed:
        for scenario, count, plan in build_plans(list(functions), mixed_counts=args.mixed_counts):
            if scenario.startswith("mixed-"):
                plans.append((scenario, count, plan))
    if args.only_scenarios:
        allowed = {item.strip() for item in args.only_scenarios.split(",") if item.strip()}
        plans = [item for item in plans if item[0] in allowed]

    runs = []
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    worker_concurrency_values = args.worker_invocation_concurrency or [None]
    for worker_invocation_concurrency in worker_concurrency_values:
        if worker_invocation_concurrency is not None:
            print(
                "configure workers: "
                f"WORKER_MAX_INVOCATION_CONCURRENCY={worker_invocation_concurrency}"
            )
            remote.wait_for_isolation()
            remote.set_worker_invocation_concurrency(
                invocation_concurrency=worker_invocation_concurrency,
                build_concurrency=1,
            )
            remote.wait_for_worker_invocation_concurrency(
                invocation_concurrency=worker_invocation_concurrency,
            )
            remote.wait_for_isolation()
        for scenario, count, plan in plans:
            for concurrency in args.concurrency:
                for repeat in range(1, args.repeats + 1):
                    run = run_invocation_batch(
                        base_url,
                        auth,
                        functions,
                        scenario=scenario,
                        count=count,
                        concurrency=concurrency,
                        worker_invocation_concurrency=worker_invocation_concurrency,
                        repeat=repeat,
                        plan=plan,
                        remote=remote,
                    )
                    runs.append(run)
                    write_report(output, functions=functions, runs=runs)
                    print(f"checkpoint: wrote {output}")
                    if run["failures"]:
                        raise BenchmarkError(
                            f"{scenario} worker_invocation_concurrency="
                            f"{worker_invocation_concurrency} saturation_concurrency="
                            f"{concurrency} repeat={repeat} had failures: "
                            f"{json.dumps(run['failures'], indent=2)}"
                        )

    write_report(output, functions=functions, runs=runs)
    print(f"wrote {output}")
    print(f"wrote {output.with_suffix('.json')}")


if __name__ == "__main__":
    main()
