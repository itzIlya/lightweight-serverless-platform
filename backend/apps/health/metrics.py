from __future__ import annotations

from django.db.models import Avg, Count
from django.http import HttpResponse
from django.utils import timezone

from apps.functions.models import BuildAttempt, BuildStatus, Function, FunctionVersion
from apps.invocations.models import Invocation, InvocationAttempt
from apps.jobs.models import CoordinationVersion, Job, OutboxEvent
from apps.workers.models import WorkerNode


CONTENT_TYPE = "text/plain; version=0.0.4; charset=utf-8"


def metrics(_request):
    now = timezone.now()
    lines = [
        "# HELP serverless_backend_up Backend metrics endpoint availability.",
        "# TYPE serverless_backend_up gauge",
        "serverless_backend_up 1",
    ]
    emit_gauge(lines, "serverless_functions_total", Function.objects.count())
    emit_gauge(lines, "serverless_function_versions_total", FunctionVersion.objects.count())
    emit_group_counts(
        lines,
        "serverless_invocations_total",
        Invocation.objects.values("status").annotate(count=Count("id")),
        "status",
    )
    emit_group_counts(
        lines,
        "serverless_invocation_attempts_total",
        InvocationAttempt.objects.values("status").annotate(count=Count("id")),
        "status",
    )
    emit_group_counts(
        lines,
        "serverless_build_attempts_total",
        BuildAttempt.objects.values("status").annotate(count=Count("id")),
        "status",
    )
    emit_job_counts(lines)
    emit_worker_metrics(lines, now)
    emit_gauge(
        lines,
        "serverless_invocation_duration_ms_avg",
        Invocation.objects.filter(duration_ms__isnull=False).aggregate(avg=Avg("duration_ms"))[
            "avg"
        ]
        or 0,
    )
    emit_gauge(
        lines,
        "serverless_build_duration_ms_avg",
        average_build_duration_ms(),
    )
    emit_gauge(
        lines,
        "serverless_outbox_unpublished_total",
        OutboxEvent.objects.filter(published_at__isnull=True).count(),
    )
    return HttpResponse("\n".join(lines) + "\n", content_type=CONTENT_TYPE)


def emit_job_counts(lines: list[str]) -> None:
    rows = (
        Job.objects.values("type", "status", "coordination_version")
        .annotate(count=Count("id"))
        .order_by("type", "status", "coordination_version")
    )
    for row in rows:
        labels = {
            "type": row["type"],
            "status": row["status"],
            "coordination_version": CoordinationVersion(row["coordination_version"]).label,
        }
        emit_metric(lines, "serverless_jobs_total", row["count"], labels)


def emit_worker_metrics(lines: list[str], now) -> None:
    rows = WorkerNode.objects.all()
    for worker in rows:
        metadata = worker.metadata or {}
        labels = {"worker": worker.name, "status": worker.status}
        emit_metric(lines, "serverless_worker_up", 1 if worker.status == "online" else 0, labels)
        emit_metric(lines, "serverless_worker_active_jobs", metadata.get("active_jobs", 0), labels)
        emit_metric(
            lines,
            "serverless_worker_active_invocations",
            metadata.get("active_invocations", 0),
            labels,
        )
        emit_metric(
            lines,
            "serverless_worker_active_builds",
            metadata.get("active_builds", 0),
            labels,
        )
        if worker.last_seen_at:
            age = max((now - worker.last_seen_at).total_seconds(), 0)
            emit_metric(lines, "serverless_worker_last_seen_age_seconds", age, labels)


def average_build_duration_ms() -> float:
    attempts = BuildAttempt.objects.filter(
        status__in={BuildStatus.BUILT, BuildStatus.FAILED, BuildStatus.CANCELLED},
        started_at__isnull=False,
        finished_at__isnull=False,
    ).values_list("started_at", "finished_at")
    durations = [
        (finished_at - started_at).total_seconds() * 1000
        for started_at, finished_at in attempts
    ]
    if not durations:
        return 0
    return sum(durations) / len(durations)


def emit_group_counts(
    lines: list[str],
    name: str,
    rows,
    label_name: str,
) -> None:
    for row in rows:
        emit_metric(lines, name, row["count"], {label_name: row[label_name]})


def emit_gauge(lines: list[str], name: str, value) -> None:
    emit_metric(lines, name, value, {})


def emit_metric(lines: list[str], name: str, value, labels: dict[str, object]) -> None:
    label_text = ""
    if labels:
        label_text = "{" + ",".join(
            f'{key}="{escape_label(value)}"' for key, value in sorted(labels.items())
        ) + "}"
    lines.append(f"{name}{label_text} {float(value)}")


def escape_label(value) -> str:
    return str(value).replace("\\", "\\\\").replace("\n", "\\n").replace('"', '\\"')
