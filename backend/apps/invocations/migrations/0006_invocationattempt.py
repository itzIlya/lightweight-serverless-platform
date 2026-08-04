from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0004_outboxevent"),
        ("invocations", "0005_invocationlogartifact"),
    ]

    operations = [
        migrations.CreateModel(
            name="InvocationAttempt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("attempt_number", models.PositiveIntegerField()),
                ("dispatch_attempt", models.PositiveIntegerField(default=0)),
                ("worker_name", models.CharField(blank=True, max_length=120)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("queued", "Queued"),
                            ("running", "Running"),
                            ("succeeded", "Succeeded"),
                            ("failed", "Failed"),
                            ("retrying", "Retrying"),
                            ("stale", "Stale"),
                        ],
                        default="queued",
                        max_length=20,
                    ),
                ),
                (
                    "failure_kind",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("", "None"),
                            ("platform", "Platform"),
                            ("timeout", "Timeout"),
                            ("function", "Function"),
                            ("output", "Output"),
                        ],
                        max_length=20,
                    ),
                ),
                ("error_message", models.TextField(blank=True)),
                ("queued_at", models.DateTimeField(auto_now_add=True)),
                ("started_at", models.DateTimeField(blank=True, null=True)),
                ("finished_at", models.DateTimeField(blank=True, null=True)),
                ("duration_ms", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "invocation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attempts",
                        to="invocations.invocation",
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="invocation_attempts",
                        to="jobs.job",
                    ),
                ),
            ],
            options={
                "ordering": ["attempt_number"],
                "constraints": [
                    models.UniqueConstraint(
                        fields=("invocation", "attempt_number"),
                        name="unique_invocation_attempt_number",
                    )
                ],
            },
        ),
    ]
