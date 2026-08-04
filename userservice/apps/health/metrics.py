from __future__ import annotations

from django.contrib.auth import get_user_model
from django.db.models import Count
from django.http import HttpResponse

from apps.accounts.models import Account


CONTENT_TYPE = "text/plain; version=0.0.4; charset=utf-8"


def metrics(_request):
    lines = [
        "# HELP serverless_userservice_up Userservice metrics endpoint availability.",
        "# TYPE serverless_userservice_up gauge",
        "serverless_userservice_up 1",
    ]
    emit_metric(lines, "serverless_userservice_users_total", get_user_model().objects.count())
    for row in Account.objects.values("role").annotate(count=Count("id")):
        emit_metric(
            lines,
            "serverless_userservice_accounts_total",
            row["count"],
            {"role": row["role"]},
        )
    emit_metric(
        lines,
        "serverless_userservice_verified_accounts_total",
        Account.objects.filter(email_verified_at__isnull=False).count(),
    )
    return HttpResponse("\n".join(lines) + "\n", content_type=CONTENT_TYPE)


def emit_metric(lines: list[str], name: str, value, labels: dict[str, object] | None = None) -> None:
    labels = labels or {}
    label_text = ""
    if labels:
        label_text = "{" + ",".join(
            f'{key}="{escape_label(value)}"' for key, value in sorted(labels.items())
        ) + "}"
    lines.append(f"{name}{label_text} {float(value)}")


def escape_label(value) -> str:
    return str(value).replace("\\", "\\\\").replace("\n", "\\n").replace('"', '\\"')
