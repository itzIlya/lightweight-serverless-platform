import json
import logging
import os
import time
from datetime import datetime, timezone

from backend_client import BackendClient, BackendError


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("scheduler")

TERMINAL_JOB_STATUSES = {"succeeded", "failed", "cancelled", "dead_lettered"}


def worker_metadata(worker: dict) -> dict:
    metadata = worker.get("metadata") or {}
    return metadata if isinstance(metadata, dict) else {}


def safe_int(value, default: int = 0) -> int:
    if value in (None, ""):
        return default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def worker_active_jobs(worker: dict) -> int:
    return safe_int(worker_metadata(worker).get("active_jobs"))


def worker_active_builds(worker: dict) -> int:
    return safe_int(worker_metadata(worker).get("active_builds"))


def worker_active_invocations(worker: dict) -> int:
    metadata = worker_metadata(worker)
    if "active_invocations" in metadata:
        return safe_int(metadata.get("active_invocations"))
    return max(worker_active_jobs(worker) - worker_active_builds(worker), 0)


def worker_max_concurrency(worker: dict) -> int:
    return max(safe_int(worker.get("max_concurrency"), default=1), 1)


def worker_max_invocation_concurrency(worker: dict) -> int:
    metadata = worker_metadata(worker)
    return max(
        safe_int(
            metadata.get("max_invocation_concurrency"),
            default=worker_max_concurrency(worker),
        ),
        1,
    )


def worker_queued_invocations(worker: dict) -> int:
    return safe_int(worker.get("queued_invocations"))


def worker_queued_builds(worker: dict) -> int:
    return safe_int(worker.get("queued_builds"))


def megabytes_to_bytes(value, *, default_mb: int) -> int:
    size_mb = safe_int(value, default=default_mb)
    return max(size_mb, 1) * 1024 * 1024


def invocation_warm_key(job: dict) -> dict:
    payload = job.get("payload") or {}
    config = payload.get("config") or {}
    image_ref = str(payload.get("image_ref") or "")
    return {
        "function_version_id": str(
            payload.get("function_version_id")
            or payload.get("version_id")
            or image_ref
        ),
        "image_ref": image_ref,
        "handler": str(payload.get("handler") or "handler.main"),
        "memory_mb": safe_int(config.get("memory_mb"), default=256),
        "output_tmpfs_size_bytes": megabytes_to_bytes(
            payload.get("invocation_output_max_total_size_mb"),
            default_mb=10,
        ),
    }


def warm_reservation_key(worker: dict, warm_key: dict) -> str:
    return (
        f"{worker.get('name', '')}|{warm_key.get('function_version_id', '')}|"
        f"{warm_key.get('image_ref', '')}|{warm_key.get('handler', '')}|"
        f"{warm_key.get('memory_mb', 0)}|"
        f"{warm_key.get('output_tmpfs_size_bytes', 0)}"
    )


def invocation_route_key(job: dict) -> str:
    warm_key = invocation_warm_key(job)
    return json.dumps(warm_key, separators=(",", ":"), sort_keys=True)


def choose_worker(
    workers: list[dict],
    job: dict,
    *,
    local_invocation_loads: dict[str, list[float]] | None = None,
    local_warm_reservations: dict[str, list[float]] | None = None,
    local_recent_invocation_routes: dict[str, dict] | None = None,
    local_load_ttl_seconds: float = 10.0,
    predictive_sticky_load_slack: int = 1,
    predictive_sticky_max_local_dispatches: int = 1,
    round_robin_state: dict[str, int] | None = None,
    now: float | None = None,
) -> dict | None:
    if not workers:
        return None

    job_type = (job.get("payload") or {}).get("type")
    if job_type == "function.invoke":
        return choose_invocation_worker(
            workers,
            job,
            local_invocation_loads=local_invocation_loads,
            local_warm_reservations=local_warm_reservations,
            local_recent_invocation_routes=local_recent_invocation_routes,
            local_load_ttl_seconds=local_load_ttl_seconds,
            predictive_sticky_load_slack=predictive_sticky_load_slack,
            predictive_sticky_max_local_dispatches=(
                predictive_sticky_max_local_dispatches
            ),
            round_robin_state=round_robin_state,
            now=now,
        )
    if job_type == "function.build":
        return choose_build_worker(
            workers,
            round_robin_state=round_robin_state,
        )
    return choose_round_robin_worker(workers, "default", round_robin_state)


def choose_invocation_worker(
    workers: list[dict],
    job: dict,
    *,
    local_invocation_loads: dict[str, list[float]] | None = None,
    local_warm_reservations: dict[str, list[float]] | None = None,
    local_recent_invocation_routes: dict[str, dict] | None = None,
    local_load_ttl_seconds: float = 10.0,
    predictive_sticky_load_slack: int = 1,
    predictive_sticky_max_local_dispatches: int = 1,
    round_robin_state: dict[str, int] | None = None,
    now: float | None = None,
) -> dict | None:
    now = time.monotonic() if now is None else now
    prune_local_invocation_loads(
        local_invocation_loads,
        now=now,
        ttl_seconds=local_load_ttl_seconds,
    )
    prune_local_warm_reservations(
        local_warm_reservations,
        now=now,
        ttl_seconds=local_load_ttl_seconds,
    )
    prune_local_recent_invocation_routes(
        local_recent_invocation_routes,
        now=now,
        ttl_seconds=local_load_ttl_seconds,
    )

    warm_key = invocation_warm_key(job)
    warm_candidates = [
        worker
        for worker in workers
        if worker_active_builds(worker) == 0
        and worker_queued_builds(worker) == 0
        and invocation_load(
            worker,
            local_invocation_loads=local_invocation_loads,
            local_load_ttl_seconds=local_load_ttl_seconds,
            now=now,
        )
        < worker_max_invocation_concurrency(worker)
        and worker_idle_warm_count(
            worker,
            warm_key,
            local_warm_reservations=local_warm_reservations,
            local_load_ttl_seconds=local_load_ttl_seconds,
            now=now,
        )
        > 0
    ]
    if warm_candidates:
        best_load = min(
            invocation_load(
                worker,
                local_invocation_loads=local_invocation_loads,
                local_load_ttl_seconds=local_load_ttl_seconds,
                now=now,
            )
            for worker in warm_candidates
        )
        best = [
            worker
            for worker in warm_candidates
            if invocation_load(
                worker,
                local_invocation_loads=local_invocation_loads,
                local_load_ttl_seconds=local_load_ttl_seconds,
                now=now,
            )
            == best_load
        ]
        return choose_round_robin_worker(best, "warm-invocation", round_robin_state)

    no_build_workers = [
        worker
        for worker in workers
        if worker_active_builds(worker) == 0 and worker_queued_builds(worker) == 0
    ]
    candidates = no_build_workers or [
        worker for worker in workers if worker_active_builds(worker) == 0
    ]
    if not candidates:
        return None

    workers_with_capacity = [
        worker
        for worker in candidates
        if invocation_load(
            worker,
            local_invocation_loads=local_invocation_loads,
            local_load_ttl_seconds=local_load_ttl_seconds,
            now=now,
        )
        < worker_max_invocation_concurrency(worker)
    ]
    candidates = workers_with_capacity or candidates

    sticky_worker = choose_predictive_sticky_worker(
        candidates,
        job,
        local_invocation_loads=local_invocation_loads,
        local_recent_invocation_routes=local_recent_invocation_routes,
        local_load_ttl_seconds=local_load_ttl_seconds,
        predictive_sticky_load_slack=predictive_sticky_load_slack,
        predictive_sticky_max_local_dispatches=predictive_sticky_max_local_dispatches,
        now=now,
    )
    if sticky_worker is not None:
        return sticky_worker

    best_load = min(
        invocation_load(
            worker,
            local_invocation_loads=local_invocation_loads,
            local_load_ttl_seconds=local_load_ttl_seconds,
            now=now,
        )
        for worker in candidates
    )
    best = [
        worker
        for worker in candidates
        if invocation_load(
            worker,
            local_invocation_loads=local_invocation_loads,
            local_load_ttl_seconds=local_load_ttl_seconds,
            now=now,
        )
        == best_load
    ]
    return choose_round_robin_worker(best, "invocation", round_robin_state)


def choose_predictive_sticky_worker(
    candidates: list[dict],
    job: dict,
    *,
    local_invocation_loads: dict[str, list[float]] | None,
    local_recent_invocation_routes: dict[str, dict] | None,
    local_load_ttl_seconds: float,
    predictive_sticky_load_slack: int,
    predictive_sticky_max_local_dispatches: int,
    now: float,
) -> dict | None:
    if predictive_sticky_load_slack < 0 or not candidates:
        return None
    route = recent_invocation_route(
        job,
        local_recent_invocation_routes=local_recent_invocation_routes,
        local_load_ttl_seconds=local_load_ttl_seconds,
        now=now,
    )
    if not route:
        return None
    worker_name = route.get("worker_name")
    if not worker_name:
        return None

    best_reported_load = min(worker_reported_invocation_load(worker) for worker in candidates)
    for worker in candidates:
        if worker.get("name") != worker_name:
            continue
        if worker_active_builds(worker) != 0 or worker_queued_builds(worker) != 0:
            return None
        reported_load = worker_reported_invocation_load(worker)
        local_dispatches = local_invocation_load(
            worker,
            local_invocation_loads=local_invocation_loads,
            local_load_ttl_seconds=local_load_ttl_seconds,
            now=now,
        )
        if local_dispatches > predictive_sticky_max_local_dispatches:
            return None
        if reported_load + local_dispatches >= worker_max_invocation_concurrency(worker):
            return None
        if reported_load > best_reported_load + predictive_sticky_load_slack:
            return None
        return worker
    return None


def recent_invocation_route(
    job: dict,
    *,
    local_recent_invocation_routes: dict[str, dict] | None,
    local_load_ttl_seconds: float,
    now: float | None,
) -> dict | None:
    if local_recent_invocation_routes is None:
        return None
    now = time.monotonic() if now is None else now
    prune_local_recent_invocation_routes(
        local_recent_invocation_routes,
        now=now,
        ttl_seconds=local_load_ttl_seconds,
    )
    return local_recent_invocation_routes.get(invocation_route_key(job))


def worker_idle_warm_count(
    worker: dict,
    warm_key: dict,
    *,
    local_warm_reservations: dict[str, list[float]] | None = None,
    local_load_ttl_seconds: float = 10.0,
    now: float | None = None,
) -> int:
    metadata = worker_metadata(worker)
    warm_pool = metadata.get("warm_pool") or {}
    if not isinstance(warm_pool, dict) or not warm_pool.get("enabled"):
        return 0
    containers = warm_pool.get("containers") or []
    if not isinstance(containers, list):
        return 0
    idle_count = 0
    for item in containers:
        if warm_inventory_item_matches(item, warm_key):
            idle_count += safe_int(item.get("idle_count"))
    if idle_count <= 0:
        return 0
    reservations = local_warm_reservation_count(
        worker,
        warm_key,
        local_warm_reservations=local_warm_reservations,
        local_load_ttl_seconds=local_load_ttl_seconds,
        now=now,
    )
    return max(idle_count - reservations, 0)


def warm_inventory_item_matches(item: dict, warm_key: dict) -> bool:
    if not isinstance(item, dict):
        return False
    return (
        str(item.get("function_version_id") or "")
        == str(warm_key.get("function_version_id") or "")
        and str(item.get("image_ref") or "") == str(warm_key.get("image_ref") or "")
        and str(item.get("handler") or "") == str(warm_key.get("handler") or "")
        and safe_int(item.get("memory_mb")) == safe_int(warm_key.get("memory_mb"))
        and safe_int(item.get("output_tmpfs_size_bytes"))
        == safe_int(warm_key.get("output_tmpfs_size_bytes"))
    )


def invocation_load(
    worker: dict,
    *,
    local_invocation_loads: dict[str, list[float]] | None = None,
    local_load_ttl_seconds: float = 10.0,
    now: float | None = None,
) -> int:
    queued = worker_queued_invocations(worker)
    local = local_invocation_load(
        worker,
        local_invocation_loads=local_invocation_loads,
        local_load_ttl_seconds=local_load_ttl_seconds,
        now=now,
    )
    return (
        worker_active_jobs(worker)
        + max(queued, local)
    )


def worker_reported_invocation_load(worker: dict) -> int:
    return worker_active_jobs(worker) + worker_queued_invocations(worker)


def local_invocation_load(
    worker: dict,
    *,
    local_invocation_loads: dict[str, list[float]] | None,
    local_load_ttl_seconds: float,
    now: float | None,
) -> int:
    if local_invocation_loads is None:
        return 0
    now = time.monotonic() if now is None else now
    prune_local_invocation_loads(
        local_invocation_loads,
        now=now,
        ttl_seconds=local_load_ttl_seconds,
    )
    return len(local_invocation_loads.get(worker.get("name"), []))


def prune_local_invocation_loads(
    local_invocation_loads: dict[str, list[float]] | None,
    *,
    now: float,
    ttl_seconds: float,
) -> None:
    if local_invocation_loads is None:
        return
    cutoff = now - ttl_seconds
    for worker_name in list(local_invocation_loads):
        local_invocation_loads[worker_name] = [
            value for value in local_invocation_loads[worker_name] if value >= cutoff
        ]
        if not local_invocation_loads[worker_name]:
            del local_invocation_loads[worker_name]


def local_warm_reservation_count(
    worker: dict,
    warm_key: dict,
    *,
    local_warm_reservations: dict[str, list[float]] | None,
    local_load_ttl_seconds: float,
    now: float | None,
) -> int:
    if local_warm_reservations is None:
        return 0
    now = time.monotonic() if now is None else now
    prune_local_warm_reservations(
        local_warm_reservations,
        now=now,
        ttl_seconds=local_load_ttl_seconds,
    )
    return len(local_warm_reservations.get(warm_reservation_key(worker, warm_key), []))


def prune_local_warm_reservations(
    local_warm_reservations: dict[str, list[float]] | None,
    *,
    now: float,
    ttl_seconds: float,
) -> None:
    if local_warm_reservations is None:
        return
    cutoff = now - ttl_seconds
    for key in list(local_warm_reservations):
        local_warm_reservations[key] = [
            value for value in local_warm_reservations[key] if value >= cutoff
        ]
        if not local_warm_reservations[key]:
            del local_warm_reservations[key]


def prune_local_recent_invocation_routes(
    local_recent_invocation_routes: dict[str, dict] | None,
    *,
    now: float,
    ttl_seconds: float,
) -> None:
    if local_recent_invocation_routes is None:
        return
    cutoff = now - ttl_seconds
    for key in list(local_recent_invocation_routes):
        route = local_recent_invocation_routes[key]
        if float(route.get("updated_at", 0)) < cutoff:
            del local_recent_invocation_routes[key]


def choose_build_worker(
    workers: list[dict],
    *,
    round_robin_state: dict[str, int] | None,
) -> dict | None:
    candidates = [
        worker
        for worker in workers
        if worker_active_builds(worker) == 0
    ]
    if not candidates:
        return None

    def build_score(worker: dict) -> tuple[int, int, int, int, int]:
        active_invocations = worker_active_invocations(worker)
        queued_invocations = worker_queued_invocations(worker)
        return (
            active_invocations + queued_invocations,
            active_invocations,
            queued_invocations,
            worker_queued_builds(worker),
            worker_active_jobs(worker),
        )

    best_score = min(build_score(worker) for worker in candidates)
    best = [worker for worker in candidates if build_score(worker) == best_score]
    return choose_round_robin_worker(best, "build", round_robin_state)


def choose_round_robin_worker(
    workers: list[dict],
    key: str,
    round_robin_state: dict[str, int] | None,
) -> dict | None:
    if not workers:
        return None
    ordered = sorted(workers, key=lambda worker: worker["name"])
    if round_robin_state is None:
        return ordered[0]
    index = round_robin_state.get(key, 0) % len(ordered)
    round_robin_state[key] = index + 1
    return ordered[index]


def make_delivery_message(job_id: str, dispatch_attempt: int) -> str:
    return json.dumps(
        {
            "job_id": job_id,
            "dispatch_attempt": dispatch_attempt,
        },
        separators=(",", ":"),
    )


def parse_delivery_message(message: str) -> dict:
    try:
        payload = json.loads(message)
    except json.JSONDecodeError:
        return {"job_id": message, "dispatch_attempt": None}
    if isinstance(payload, dict) and payload.get("job_id"):
        return {
            "job_id": str(payload["job_id"]),
            "dispatch_attempt": payload.get("dispatch_attempt"),
        }
    return {"job_id": message, "dispatch_attempt": None}


def seconds_until_available(job: dict) -> float:
    available_at = job.get("available_at")
    if not available_at:
        return 0
    if isinstance(available_at, str):
        value = available_at.replace("Z", "+00:00")
        try:
            available_at = datetime.fromisoformat(value)
        except ValueError:
            return 0
    if available_at.tzinfo is None:
        available_at = available_at.replace(tzinfo=timezone.utc)
    return max((available_at - datetime.now(timezone.utc)).total_seconds(), 0)


def process_job_id(
    *,
    job_id: str,
    backend: BackendClient,
    redis_client,
    pending_queue: str,
    pending_queues: dict[str, str] | None = None,
    local_invocation_loads: dict[str, list[float]] | None = None,
    local_warm_reservations: dict[str, list[float]] | None = None,
    local_recent_invocation_routes: dict[str, dict] | None = None,
    local_load_ttl_seconds: float = 10.0,
    predictive_sticky_load_slack: int = 1,
    predictive_sticky_max_local_dispatches: int = 1,
    round_robin_state: dict[str, int] | None = None,
    requeue_delay_seconds: float = 1.0,
    stale_after_seconds: int | None = None,
) -> bool:
    job = backend.get_job(job_id)
    coordination_version = safe_int(job.get("coordination_version", 1), default=1)
    if coordination_version != 1:
        logger.warning(
            "refusing non-V1 job on V1 scheduler path job_id=%s coordination_version=%s",
            job_id,
            coordination_version,
        )
        return False
    if job.get("status") != "queued":
        logger.info(
            "ignoring non-queued job job_id=%s status=%s",
            job_id,
            job.get("status"),
        )
        return False

    wait_seconds = seconds_until_available(job)
    if wait_seconds > 0:
        logger.info(
            "job is not available yet; requeueing job_id=%s wait_seconds=%.3f",
            job_id,
            wait_seconds,
        )
        time.sleep(min(wait_seconds, requeue_delay_seconds))
        redis_client.rpush(pending_queue_for_job(job, pending_queue, pending_queues), job_id)
        return False

    if stale_after_seconds is not None:
        backend.expire_stale_workers(stale_after_seconds=stale_after_seconds)

    workers = workers_with_queue_lengths(backend.list_workers(), redis_client)
    worker = choose_worker(
        workers,
        job,
        local_invocation_loads=local_invocation_loads,
        local_warm_reservations=local_warm_reservations,
        local_recent_invocation_routes=local_recent_invocation_routes,
        local_load_ttl_seconds=local_load_ttl_seconds,
        predictive_sticky_load_slack=predictive_sticky_load_slack,
        predictive_sticky_max_local_dispatches=predictive_sticky_max_local_dispatches,
        round_robin_state=round_robin_state,
    )
    if worker is None:
        logger.info("no online workers available; requeueing job_id=%s", job_id)
        time.sleep(requeue_delay_seconds)
        redis_client.rpush(pending_queue_for_job(job, pending_queue, pending_queues), job_id)
        return False

    queue_name = worker_queue_for_job(worker, job)
    dispatch = backend.dispatch_job(
        job_id,
        worker_name=worker["name"],
        queue_name=queue_name,
    )
    if not dispatch.get("dispatched"):
        logger.info(
            "job was not dispatched after worker queue push job_id=%s status=%s",
            job_id,
            dispatch.get("status"),
        )
        return False

    dispatch_attempt = dispatch["job"]["payload"]["dispatch_attempt"]
    delivery_message = make_delivery_message(job_id, dispatch_attempt)
    try:
        redis_client.rpush(queue_name, delivery_message)
    except Exception:
        backend.requeue_job(
            job_id,
            worker_name=worker["name"],
            reason="Scheduler failed to push job ID to worker queue.",
        )
        raise

    logger.info(
        "dispatched job_id=%s type=%s worker=%s queue=%s",
        job_id,
        job.get("type"),
        worker["name"],
        queue_name,
    )
    remember_local_warm_reservation(
        job,
        worker,
        local_warm_reservations=local_warm_reservations,
        local_load_ttl_seconds=local_load_ttl_seconds,
    )
    remember_local_invocation_dispatch(
        job,
        worker,
        local_invocation_loads=local_invocation_loads,
        local_load_ttl_seconds=local_load_ttl_seconds,
    )
    remember_recent_invocation_route(
        job,
        worker,
        local_recent_invocation_routes=local_recent_invocation_routes,
        local_load_ttl_seconds=local_load_ttl_seconds,
    )
    return True


def workers_with_queue_lengths(workers: list[dict], redis_client) -> list[dict]:
    enriched = []
    for worker in workers:
        item = dict(worker)
        item["queued_invocations"] = redis_client.llen(
            worker.get("invocation_queue_name") or worker.get("queue_name")
        )
        item["queued_builds"] = redis_client.llen(
            worker.get("build_queue_name") or worker.get("queue_name")
        )
        enriched.append(item)
    return enriched


def worker_queue_for_job(worker: dict, job: dict) -> str:
    job_type = (job.get("payload") or {}).get("type")
    if job_type == "function.invoke":
        return worker.get("invocation_queue_name") or worker["queue_name"]
    if job_type == "function.build":
        return worker.get("build_queue_name") or worker["queue_name"]
    return worker["queue_name"]


def worker_recovery_queues(worker: dict) -> list[str]:
    queue_names = [
        worker.get("processing_queue_name"),
        worker.get("invocation_queue_name"),
        worker.get("build_queue_name"),
        worker.get("queue_name"),
    ]
    seen = set()
    unique = []
    for queue_name in queue_names:
        if queue_name and queue_name not in seen:
            unique.append(queue_name)
            seen.add(queue_name)
    return unique


def pending_queue_for_job(
    job: dict,
    default_queue: str,
    pending_queues: dict[str, str] | None,
) -> str:
    job_type = (job.get("payload") or {}).get("type")
    if pending_queues and job_type in pending_queues:
        return pending_queues[job_type]
    return job.get("queue_name") or default_queue


def remember_local_warm_reservation(
    job: dict,
    worker: dict,
    *,
    local_warm_reservations: dict[str, list[float]] | None,
    local_load_ttl_seconds: float,
) -> None:
    if local_warm_reservations is None:
        return
    if (job.get("payload") or {}).get("type") != "function.invoke":
        return
    now = time.monotonic()
    warm_key = invocation_warm_key(job)
    if worker_idle_warm_count(
        worker,
        warm_key,
        local_warm_reservations=local_warm_reservations,
        local_load_ttl_seconds=local_load_ttl_seconds,
        now=now,
    ) <= 0:
        return
    prune_local_warm_reservations(
        local_warm_reservations,
        now=now,
        ttl_seconds=local_load_ttl_seconds,
    )
    local_warm_reservations.setdefault(
        warm_reservation_key(worker, warm_key),
        [],
    ).append(now)


def remember_local_invocation_dispatch(
    job: dict,
    worker: dict,
    *,
    local_invocation_loads: dict[str, list[float]] | None,
    local_load_ttl_seconds: float,
) -> None:
    if local_invocation_loads is None:
        return
    if (job.get("payload") or {}).get("type") != "function.invoke":
        return
    now = time.monotonic()
    prune_local_invocation_loads(
        local_invocation_loads,
        now=now,
        ttl_seconds=local_load_ttl_seconds,
    )
    local_invocation_loads.setdefault(worker["name"], []).append(now)


def remember_recent_invocation_route(
    job: dict,
    worker: dict,
    *,
    local_recent_invocation_routes: dict[str, dict] | None,
    local_load_ttl_seconds: float,
) -> None:
    if local_recent_invocation_routes is None:
        return
    if (job.get("payload") or {}).get("type") != "function.invoke":
        return
    now = time.monotonic()
    prune_local_recent_invocation_routes(
        local_recent_invocation_routes,
        now=now,
        ttl_seconds=local_load_ttl_seconds,
    )
    local_recent_invocation_routes[invocation_route_key(job)] = {
        "worker_name": worker["name"],
        "updated_at": now,
    }


def recover_stale_workers(
    *,
    backend: BackendClient,
    redis_client,
    pending_queue: str,
    pending_queues: dict[str, str] | None = None,
    stale_after_seconds: int,
) -> int:
    expired_response = backend.expire_stale_workers(
        stale_after_seconds=stale_after_seconds,
    )
    recovered = 0
    for worker in expired_response.get("expired", []):
        worker_name = worker["name"]
        for queue_name in worker_recovery_queues(worker):
            delivery_messages = redis_client.lrange(queue_name, 0, -1)
            if not delivery_messages:
                continue

            logger.info(
                "recovering stale worker jobs worker=%s queue=%s count=%s",
                worker_name,
                queue_name,
                len(delivery_messages),
            )
            for delivery_message in delivery_messages:
                delivery = parse_delivery_message(delivery_message)
                job_id = delivery["job_id"]
                job = backend.get_job(job_id)
                if job.get("status") in TERMINAL_JOB_STATUSES:
                    redis_client.lrem(queue_name, 1, delivery_message)
                    continue

                requeue = backend.requeue_job(
                    job_id,
                    worker_name=worker_name,
                    reason=f"Worker {worker_name} missed heartbeat.",
                    recovery=True,
                )
                if requeue.get("dead_lettered"):
                    redis_client.lrem(queue_name, 1, delivery_message)
                    logger.warning(
                        "dead-lettered recovered job job_id=%s worker=%s",
                        job_id,
                        worker_name,
                    )
                    continue
                if not requeue.get("requeued"):
                    continue

                redis_client.lrem(queue_name, 1, delivery_message)
                redis_client.rpush(
                    pending_queue_for_job(
                        requeue.get("job") or job,
                        pending_queue,
                        pending_queues,
                    ),
                    job_id,
                )
                recovered += 1
                logger.info(
                    "recovered stale job job_id=%s worker=%s",
                    job_id,
                    worker_name,
                )
    return recovered


def main() -> None:
    import redis

    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    pending_queue = os.getenv("SCHEDULER_QUEUE_NAME", "scheduler-pending-jobs")
    invocation_pending_queue = os.getenv(
        "SCHEDULER_INVOCATION_QUEUE_NAME",
        "scheduler-pending-invocations",
    )
    build_pending_queue = os.getenv(
        "SCHEDULER_BUILD_QUEUE_NAME",
        "scheduler-pending-builds",
    )
    pending_queues = {
        "function.invoke": invocation_pending_queue,
        "function.build": build_pending_queue,
    }
    backend_base_url = os.getenv("BACKEND_BASE_URL", "http://backend:8000")
    worker_token = os.getenv("WORKER_SHARED_SECRET", "change-me")
    requeue_delay_seconds = float(os.getenv("SCHEDULER_REQUEUE_DELAY_SECONDS", "1"))
    stale_after_seconds = int(os.getenv("WORKER_STALE_AFTER_SECONDS", "30"))
    local_load_ttl_seconds = float(
        os.getenv("SCHEDULER_LOCAL_LOAD_TTL_SECONDS", "10")
    )
    predictive_sticky_load_slack = int(
        os.getenv("SCHEDULER_PREDICTIVE_STICKY_LOAD_SLACK", "1")
    )
    predictive_sticky_max_local_dispatches = int(
        os.getenv("SCHEDULER_PREDICTIVE_STICKY_MAX_LOCAL_DISPATCHES", "1")
    )
    recovery_interval_seconds = float(
        os.getenv("SCHEDULER_RECOVERY_INTERVAL_SECONDS", "5")
    )

    redis_client = redis.Redis.from_url(redis_url, decode_responses=True)
    backend = BackendClient(backend_base_url, worker_token)
    next_recovery_at = time.monotonic()
    local_invocation_loads: dict[str, list[float]] = {}
    local_warm_reservations: dict[str, list[float]] = {}
    local_recent_invocation_routes: dict[str, dict] = {}
    round_robin_state: dict[str, int] = {}

    logger.info(
        "scheduler started; invocation_queue=%s build_queue=%s",
        invocation_pending_queue,
        build_pending_queue,
    )
    while True:
        if time.monotonic() >= next_recovery_at:
            try:
                recover_stale_workers(
                    backend=backend,
                    redis_client=redis_client,
                    pending_queue=pending_queue,
                    pending_queues=pending_queues,
                    stale_after_seconds=stale_after_seconds,
                )
            except BackendError:
                logger.exception("backend error while recovering stale workers")
            except Exception:
                logger.exception("unexpected stale-worker recovery failure")
            next_recovery_at = time.monotonic() + recovery_interval_seconds

        item = redis_client.blpop(
            [invocation_pending_queue, build_pending_queue],
            timeout=5,
        )
        if item is None:
            continue

        source_pending_queue, job_id = item
        try:
            process_job_id(
                job_id=job_id,
                backend=backend,
                redis_client=redis_client,
                pending_queue=source_pending_queue,
                pending_queues=pending_queues,
                local_invocation_loads=local_invocation_loads,
                local_warm_reservations=local_warm_reservations,
                local_recent_invocation_routes=local_recent_invocation_routes,
                local_load_ttl_seconds=local_load_ttl_seconds,
                predictive_sticky_load_slack=predictive_sticky_load_slack,
                predictive_sticky_max_local_dispatches=(
                    predictive_sticky_max_local_dispatches
                ),
                round_robin_state=round_robin_state,
                requeue_delay_seconds=requeue_delay_seconds,
                stale_after_seconds=stale_after_seconds,
            )
        except BackendError:
            logger.exception("backend error while scheduling job_id=%s", job_id)
            redis_client.rpush(source_pending_queue, job_id)
        except Exception:
            logger.exception("unexpected scheduler failure job_id=%s", job_id)
            redis_client.rpush(source_pending_queue, job_id)


if __name__ == "__main__":
    main()
