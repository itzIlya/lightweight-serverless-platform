import uuid

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


def copy_existing_builds(apps, schema_editor):
    FunctionVersion = apps.get_model("functions", "FunctionVersion")
    BuildAttempt = apps.get_model("functions", "BuildAttempt")

    for version in FunctionVersion.objects.exclude(build_status="pending"):
        queued_at = version.build_queued_at or version.created_at
        BuildAttempt.objects.create(
            request_id=version.build_request_id,
            build_id=uuid.uuid4(),
            function_version=version,
            attempt_number=1,
            status=version.build_status,
            image_ref=version.image_ref,
            log=version.build_log,
            queued_at=queued_at,
            started_at=version.build_started_at,
            finished_at=version.build_finished_at,
        )


def create_default_policy(apps, schema_editor):
    BuildPolicy = apps.get_model("functions", "BuildPolicy")
    BuildPolicy.objects.get_or_create(pk=1, defaults={"max_retries": 2})


class Migration(migrations.Migration):

    dependencies = [
        ("functions", "0002_async_build_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="functionversion",
            name="build_status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("queued", "Queued"),
                    ("building", "Building"),
                    ("cancelling", "Cancelling"),
                    ("built", "Built"),
                    ("failed", "Failed"),
                    ("cancelled", "Cancelled"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
        migrations.CreateModel(
            name="BuildPolicy",
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
                ("max_retries", models.PositiveSmallIntegerField(default=2)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"verbose_name_plural": "build policy"},
        ),
        migrations.CreateModel(
            name="BuildAttempt",
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
                    "request_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                (
                    "build_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
                ),
                ("attempt_number", models.PositiveIntegerField(default=1)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("queued", "Queued"),
                            ("building", "Building"),
                            ("cancelling", "Cancelling"),
                            ("built", "Built"),
                            ("failed", "Failed"),
                            ("cancelled", "Cancelled"),
                        ],
                        default="queued",
                        max_length=20,
                    ),
                ),
                ("image_ref", models.CharField(blank=True, max_length=255)),
                ("log", models.TextField(blank=True)),
                ("queued_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("started_at", models.DateTimeField(blank=True, null=True)),
                ("finished_at", models.DateTimeField(blank=True, null=True)),
                ("cancel_requested_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "function_version",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="build_attempts",
                        to="functions.functionversion",
                    ),
                ),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.AddConstraint(
            model_name="buildattempt",
            constraint=models.UniqueConstraint(
                fields=("build_id", "attempt_number"),
                name="unique_build_attempt_number",
            ),
        ),
        migrations.RunPython(copy_existing_builds, migrations.RunPython.noop),
        migrations.RunPython(create_default_policy, migrations.RunPython.noop),
    ]
