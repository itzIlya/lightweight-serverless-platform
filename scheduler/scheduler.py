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
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return default


def worker_active_jobs(worker: dict) -> int:
    return safe_int(worker_metadata(worker).get("active_jobs"))


def worker_active_builds(worker: dict) -> int:
    return safe_int(worker_metadata(worker).get("active_builds"))


def worker_queued_invocations(worker: dict) -> int:
    return safe_int(worker.get("queued_invocations"))


def worker_queued_builds(worker: dict) -> int:
    return safe_int(worker.get("queued_builds"))


def invocation_affinity_key(job: dict) -> str:
    payload = job.get("payload") or {}
    return str(
        payload.get("function_version_id")
        or payload.get("image_ref")
        or payload.get("function_id")
        or ""
    )


def choose_worker(
    workers: list[dict],
    job: dict,
    *,
    recent_invocations: dict[str, dict] | None = None,
    affinity_ttl_seconds: float = 10.0,
    sticky_max_invocation_load: int = 2,
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
            recent_invocations=recent_invocations,
            affinity_ttl_seconds=affinity_ttl_seconds,
            sticky_max_invocation_load=sticky_max_invocation_load,
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
    recent_invocations: dict[str, dict] | None,
    affinity_ttl_seconds: float,
    sticky_max_invocation_load: int,
    round_robin_state: dict[str, int] | None,
    now: float | None,
) -> dict | None:
    now = time.monotonic() if now is None else now
    recent_invocations = recent_invocations or {}

    affinity_key = invocation_affinity_key(job)
    if affinity_key:
        route = recent_invocations.get(affinity_key)
        if route and now - float(route.get("last_seen", 0)) <= affinity_ttl_seconds:
            worker = next(
                (
                    item
                    for item in workers
                    if item.get("name") == route.get("worker_name")
                ),
                None,
            )
            if worker and invocation_worker_is_light_enough(
                worker,
                sticky_max_invocation_load=sticky_max_invocation_load,
            ):
                return worker

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

    best_load = min(invocation_load(worker) for worker in candidates)
    best = [
        worker for worker in candidates if invocation_load(worker) == best_load
    ]
    return choose_round_robin_worker(best, "invocation", round_robin_state)


def invocation_worker_is_light_enough(
    worker: dict,
    *,
    sticky_max_invocation_load: int,
) -> bool:
    return (
        worker_active_builds(worker) == 0
        and invocation_load(worker) <= sticky_max_invocation_load
    )


def invocation_load(worker: dict) -> int:
    return worker_active_jobs(worker) + worker_queued_invocations(worker)


def choose_build_worker(
    workers: list[dict],
    *,
    round_robin_state: dict[str, int] | None,
) -> dict | None:
    candidates = [
        worker
        for worker in workers
        if worker_active_jobs(worker) == 0
        and worker_queued_invocations(worker) == 0
        and worker_queued_builds(worker) == 0
    ]
    if not candidates:
        return None
    return choose_round_robin_worker(candidates, "build", round_robin_state)


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
    recent_invocations: dict[str, dict] | None = None,
    round_robin_state: dict[str, int] | None = None,
    affinity_ttl_seconds: float = 10.0,
    sticky_max_invocation_load: int = 2,
    requeue_delay_seconds: float = 1.0,
) -> bool:
    job = backend.get_job(job_id)
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

    workers = workers_with_queue_lengths(backend.list_workers(), redis_client)
    worker = choose_worker(
        workers,
        job,
        recent_invocations=recent_invocations,
        affinity_ttl_seconds=affinity_ttl_seconds,
        sticky_max_invocation_load=sticky_max_invocation_load,
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
    remember_invocation_route(
        job,
        worker,
        recent_invocations=recent_invocations,
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


def pending_queue_for_job(
    job: dict,
    default_queue: str,
    pending_queues: dict[str, str] | None,
) -> str:
    job_type = (job.get("payload") or {}).get("type")
    if pending_queues and job_type in pending_queues:
        return pending_queues[job_type]
    return job.get("queue_name") or default_queue


def remember_invocation_route(
    job: dict,
    worker: dict,
    *,
    recent_invocations: dict[str, dict] | None,
) -> None:
    if recent_invocations is None:
        return
    if (job.get("payload") or {}).get("type") != "function.invoke":
        return
    affinity_key = invocation_affinity_key(job)
    if not affinity_key:
        return
    recent_invocations[affinity_key] = {
        "worker_name": worker["name"],
        "last_seen": time.monotonic(),
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
        processing_queue = worker["processing_queue_name"]
        delivery_messages = redis_client.lrange(processing_queue, 0, -1)
        if not delivery_messages:
            continue

        logger.info(
            "recovering stale worker jobs worker=%s processing_queue=%s count=%s",
            worker_name,
            processing_queue,
            len(delivery_messages),
        )
        for delivery_message in delivery_messages:
            delivery = parse_delivery_message(delivery_message)
            job_id = delivery["job_id"]
            job = backend.get_job(job_id)
            if job.get("status") in TERMINAL_JOB_STATUSES:
                redis_client.lrem(processing_queue, 1, delivery_message)
                continue

            requeue = backend.requeue_job(
                job_id,
                worker_name=worker_name,
                reason=f"Worker {worker_name} missed heartbeat.",
                recovery=True,
            )
            if requeue.get("dead_lettered"):
                redis_client.lrem(processing_queue, 1, delivery_message)
                logger.warning(
                    "dead-lettered recovered job job_id=%s worker=%s",
                    job_id,
                    worker_name,
                )
                continue
            if not requeue.get("requeued"):
                continue

            redis_client.lrem(processing_queue, 1, delivery_message)
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
    affinity_ttl_seconds = float(os.getenv("SCHEDULER_AFFINITY_TTL_SECONDS", "10"))
    sticky_max_invocation_load = int(
        os.getenv("SCHEDULER_STICKY_MAX_INVOCATION_LOAD", "2")
    )
    recovery_interval_seconds = float(
        os.getenv("SCHEDULER_RECOVERY_INTERVAL_SECONDS", "5")
    )

    redis_client = redis.Redis.from_url(redis_url, decode_responses=True)
    backend = BackendClient(backend_base_url, worker_token)
    next_recovery_at = time.monotonic()
    recent_invocations: dict[str, dict] = {}
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
                recent_invocations=recent_invocations,
                round_robin_state=round_robin_state,
                affinity_ttl_seconds=affinity_ttl_seconds,
                sticky_max_invocation_load=sticky_max_invocation_load,
                requeue_delay_seconds=requeue_delay_seconds,
            )
        except BackendError:
            logger.exception("backend error while scheduling job_id=%s", job_id)
            redis_client.rpush(source_pending_queue, job_id)
        except Exception:
            logger.exception("unexpected scheduler failure job_id=%s", job_id)
            redis_client.rpush(source_pending_queue, job_id)


if __name__ == "__main__":
    main()
