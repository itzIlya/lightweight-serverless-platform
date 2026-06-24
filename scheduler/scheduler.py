import json
import logging
import os
import time

from backend_client import BackendClient, BackendError


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("scheduler")

TERMINAL_JOB_STATUSES = {"succeeded", "failed", "cancelled"}


def choose_worker(workers: list[dict], job: dict) -> dict | None:
    if not workers:
        return None
    return sorted(workers, key=lambda worker: worker["name"])[0]


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


def process_job_id(
    *,
    job_id: str,
    backend: BackendClient,
    redis_client,
    pending_queue: str,
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

    workers = backend.list_workers()
    worker = choose_worker(workers, job)
    if worker is None:
        logger.info("no online workers available; requeueing job_id=%s", job_id)
        time.sleep(requeue_delay_seconds)
        redis_client.rpush(pending_queue, job_id)
        return False

    queue_name = worker["queue_name"]
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
    return True


def recover_stale_workers(
    *,
    backend: BackendClient,
    redis_client,
    pending_queue: str,
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
            )
            if not requeue.get("requeued"):
                continue

            redis_client.lrem(processing_queue, 1, delivery_message)
            redis_client.rpush(pending_queue, job_id)
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
    backend_base_url = os.getenv("BACKEND_BASE_URL", "http://backend:8000")
    worker_token = os.getenv("WORKER_SHARED_SECRET", "change-me")
    requeue_delay_seconds = float(os.getenv("SCHEDULER_REQUEUE_DELAY_SECONDS", "1"))
    stale_after_seconds = int(os.getenv("WORKER_STALE_AFTER_SECONDS", "30"))
    recovery_interval_seconds = float(
        os.getenv("SCHEDULER_RECOVERY_INTERVAL_SECONDS", "5")
    )

    redis_client = redis.Redis.from_url(redis_url, decode_responses=True)
    backend = BackendClient(backend_base_url, worker_token)
    next_recovery_at = time.monotonic()

    logger.info("scheduler started; pending_queue=%s", pending_queue)
    while True:
        if time.monotonic() >= next_recovery_at:
            try:
                recover_stale_workers(
                    backend=backend,
                    redis_client=redis_client,
                    pending_queue=pending_queue,
                    stale_after_seconds=stale_after_seconds,
                )
            except BackendError:
                logger.exception("backend error while recovering stale workers")
            except Exception:
                logger.exception("unexpected stale-worker recovery failure")
            next_recovery_at = time.monotonic() + recovery_interval_seconds

        item = redis_client.blpop(pending_queue, timeout=5)
        if item is None:
            continue

        _, job_id = item
        try:
            process_job_id(
                job_id=job_id,
                backend=backend,
                redis_client=redis_client,
                pending_queue=pending_queue,
                requeue_delay_seconds=requeue_delay_seconds,
            )
        except BackendError:
            logger.exception("backend error while scheduling job_id=%s", job_id)
            redis_client.rpush(pending_queue, job_id)
        except Exception:
            logger.exception("unexpected scheduler failure job_id=%s", job_id)
            redis_client.rpush(pending_queue, job_id)


if __name__ == "__main__":
    main()
