import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("functions", "0006_build_limits_and_leases"),
        ("invocations", "0002_input_files"),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
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
                (
                    "job_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("build", "Build"),
                            ("invocation", "Invocation"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("queued", "Queued"),
                            ("dispatched", "Dispatched"),
                            ("running", "Running"),
                            ("succeeded", "Succeeded"),
                            ("failed", "Failed"),
                            ("cancelled", "Cancelled"),
                        ],
                        default="queued",
                        max_length=20,
                    ),
                ),
                ("queue_name", models.CharField(max_length=120)),
                ("payload", models.JSONField(blank=True, default=dict)),
                ("available_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("locked_until", models.DateTimeField(blank=True, null=True)),
                ("dispatch_attempts", models.PositiveIntegerField(default=0)),
                ("last_error", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "build_attempt",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="jobs",
                        to="functions.buildattempt",
                    ),
                ),
                (
                    "invocation",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="jobs",
                        to="invocations.invocation",
                    ),
                ),
            ],
            options={
                "ordering": ["created_at"],
            },
        ),
        migrations.AddIndex(
            model_name="job",
            index=models.Index(fields=["status", "available_at"], name="jobs_job_status_fb5144_idx"),
        ),
        migrations.AddIndex(
            model_name="job",
            index=models.Index(fields=["type", "status"], name="jobs_job_type_aec67a_idx"),
        ),
    ]
