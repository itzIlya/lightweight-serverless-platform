from __future__ import annotations

from dataclasses import dataclass, field
import logging
import threading
import time
from typing import Callable


logger = logging.getLogger("worker.warm_pool")


@dataclass(frozen=True)
class WarmContainerKey:
    function_version_id: str
    image_ref: str
    handler: str
    memory_mb: int
    output_tmpfs_size_bytes: int
    direct_output_upload_enabled: bool = False


@dataclass
class WarmContainerRecord:
    key: WarmContainerKey
    container: object
    volume: object | None
    created_at: float
    last_used_at: float
    use_count: int = 0
    hit_count: int = 0
    state: str = "idle"
    eviction_reason: str = ""
    metadata: dict = field(default_factory=dict)


class WarmContainerPool:
    def __init__(
        self,
        *,
        max_containers: int,
        max_per_key: int,
        idle_ttl_seconds: float,
        max_age_seconds: float,
        max_uses: int,
        max_memory_mb: int = 0,
        now: Callable[[], float] | None = None,
    ) -> None:
        self.max_containers = max(0, int(max_containers))
        self.max_per_key = max(0, int(max_per_key))
        self.idle_ttl_seconds = max(0.0, float(idle_ttl_seconds))
        self.max_age_seconds = max(0.0, float(max_age_seconds))
        self.max_uses = max(0, int(max_uses))
        self.max_memory_mb = max(0, int(max_memory_mb))
        self._now = now or time.monotonic
        self._lock = threading.Lock()
        self._records: list[WarmContainerRecord] = []
        self.eviction_log: list[dict] = []

    def acquire(self, key: WarmContainerKey) -> WarmContainerRecord | None:
        with self._lock:
            self._evict_expired_locked()
            candidates = [
                record
                for record in self._records
                if record.key == key and record.state == "idle"
            ]
            if not candidates:
                return None
            record = max(candidates, key=lambda item: item.last_used_at)
            record.state = "busy"
            record.hit_count += 1
            return record

    def add_busy(
        self,
        *,
        key: WarmContainerKey,
        container,
        volume=None,
        metadata: dict | None = None,
    ) -> WarmContainerRecord | None:
        if self.max_containers <= 0 or self.max_per_key <= 0:
            self._destroy_container(container)
            self._destroy_volume(volume)
            return None

        now = self._now()
        record = WarmContainerRecord(
            key=key,
            container=container,
            volume=volume,
            created_at=now,
            last_used_at=now,
            state="busy",
            metadata=dict(metadata or {}),
        )
        with self._lock:
            self._records.append(record)
        return record

    def release(self, record: WarmContainerRecord, *, reusable: bool) -> None:
        with self._lock:
            if record not in self._records:
                return
            if not reusable:
                self._records.remove(record)
                self._mark_evicted_locked(record, "failed_execution")
                destroy = [record]
            else:
                now = self._now()
                record.use_count += 1
                record.last_used_at = now
                record.state = "idle"
                destroy = self._records_to_evict_after_release_locked(record)
                for item in destroy:
                    if item in self._records:
                        self._records.remove(item)
                        item.state = "destroyed"

        for item in destroy:
            self._destroy_record(item)

    def evict_expired(self) -> int:
        with self._lock:
            destroy = [
                record
                for record in self._records
                if record.state == "idle"
                and self._retirement_reason_locked(record)
            ]
            for record in destroy:
                self._records.remove(record)
                self._mark_evicted_locked(
                    record,
                    self._retirement_reason_locked(record) or "retired",
                )

        for record in destroy:
            self._destroy_record(record)
        return len(destroy)

    def close(self) -> None:
        with self._lock:
            destroy = list(self._records)
            self._records.clear()
            for record in destroy:
                self._mark_evicted_locked(record, "pool_close")

        for record in destroy:
            self._destroy_record(record)

    def snapshot(self) -> list[WarmContainerRecord]:
        with self._lock:
            return list(self._records)

    def inventory(self) -> list[dict]:
        with self._lock:
            self._evict_expired_locked()
            grouped: dict[WarmContainerKey, dict] = {}
            for record in self._records:
                item = grouped.setdefault(
                    record.key,
                    {
                        "function_version_id": record.key.function_version_id,
                        "image_ref": record.key.image_ref,
                        "handler": record.key.handler,
                        "memory_mb": record.key.memory_mb,
                        "output_tmpfs_size_bytes": (
                            record.key.output_tmpfs_size_bytes
                        ),
                        "idle_count": 0,
                        "busy_count": 0,
                        "use_count": 0,
                        "hit_count": 0,
                    },
                )
                if record.state == "idle":
                    item["idle_count"] += 1
                elif record.state == "busy":
                    item["busy_count"] += 1
                item["use_count"] += record.use_count
                item["hit_count"] += record.hit_count
            return list(grouped.values())

    def _records_to_evict_after_release_locked(
        self,
        released: WarmContainerRecord,
    ) -> list[WarmContainerRecord]:
        destroy: list[WarmContainerRecord] = []
        retirement_reason = self._retirement_reason_locked(released)
        if retirement_reason:
            self._mark_evicted_locked(released, retirement_reason)
            destroy.append(released)
            return destroy

        idle_same_key = [
            record
            for record in self._records
            if record.key == released.key and record.state == "idle"
        ]
        while len(idle_same_key) > self.max_per_key:
            victim = self._choose_eviction_victim_locked(
                idle_same_key,
                pressure="function_over_limit",
            )
            self._mark_evicted_locked(victim, "function_over_limit")
            destroy.append(victim)
            idle_same_key.remove(victim)

        idle_records = [
            record for record in self._records if record.state == "idle"
        ]
        while len(self._records) - len(destroy) > self.max_containers:
            candidates = [record for record in idle_records if record not in destroy]
            if not candidates:
                break
            victim = self._choose_eviction_victim_locked(
                candidates,
                pressure="pool_container_pressure",
            )
            self._mark_evicted_locked(victim, "pool_container_pressure")
            destroy.append(victim)

        while (
            self.max_memory_mb
            and self._memory_mb_locked(excluding=destroy) > self.max_memory_mb
        ):
            candidates = [
                record
                for record in idle_records
                if record not in destroy and record.state == "idle"
            ]
            if not candidates:
                break
            victim = self._choose_eviction_victim_locked(
                candidates,
                pressure="pool_memory_pressure",
            )
            self._mark_evicted_locked(victim, "pool_memory_pressure")
            destroy.append(victim)

        return destroy

    def _evict_expired_locked(self) -> None:
        expired = [
            record
            for record in self._records
            if record.state == "idle"
            and self._retirement_reason_locked(record)
        ]
        for record in expired:
            self._records.remove(record)
            self._mark_evicted_locked(
                record,
                self._retirement_reason_locked(record) or "retired",
            )
        for record in expired:
            self._destroy_record(record)

    def _retirement_reason_locked(self, record: WarmContainerRecord) -> str:
        now = self._now()
        if self.idle_ttl_seconds and now - record.last_used_at >= self.idle_ttl_seconds:
            return "idle_ttl"
        if self.max_age_seconds and now - record.created_at >= self.max_age_seconds:
            return "max_age"
        if self.max_uses and record.use_count >= self.max_uses:
            return "max_uses"
        return ""

    def _choose_eviction_victim_locked(
        self,
        candidates: list[WarmContainerRecord],
        *,
        pressure: str,
    ) -> WarmContainerRecord:
        if pressure == "pool_memory_pressure":
            return min(
                candidates,
                key=lambda record: (
                    record.hit_count,
                    record.use_count,
                    -record.key.memory_mb,
                    record.last_used_at,
                    record.created_at,
                ),
            )
        return min(
            candidates,
            key=lambda record: (
                record.hit_count,
                record.use_count,
                record.last_used_at,
                record.created_at,
                -record.key.memory_mb,
            ),
        )

    def _memory_mb_locked(
        self,
        *,
        excluding: list[WarmContainerRecord] | None = None,
    ) -> int:
        excluded = set(id(record) for record in (excluding or []))
        return sum(
            record.key.memory_mb
            for record in self._records
            if id(record) not in excluded and record.state != "destroyed"
        )

    def _mark_evicted_locked(
        self,
        record: WarmContainerRecord,
        reason: str,
    ) -> None:
        if record.state == "destroyed":
            return
        record.state = "destroyed"
        record.eviction_reason = reason
        self.eviction_log.append(
            {
                "function_version_id": record.key.function_version_id,
                "image_ref": record.key.image_ref,
                "reason": reason,
                "hit_count": record.hit_count,
                "use_count": record.use_count,
                "memory_mb": record.key.memory_mb,
            }
        )

    def _destroy_record(self, record: WarmContainerRecord) -> None:
        self._destroy_container(record.container)
        self._destroy_volume(record.volume)

    def _destroy_container(self, container) -> None:
        if container is None:
            return
        try:
            container.remove(force=True)
        except Exception:
            logger.exception("failed to remove warm container")

    def _destroy_volume(self, volume) -> None:
        if volume is None:
            return
        try:
            volume.remove(force=True)
        except Exception:
            logger.exception("failed to remove warm container volume")
