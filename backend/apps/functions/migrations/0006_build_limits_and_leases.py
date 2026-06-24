from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("workers", "0002_worker_build_concurrency"),
        ("functions", "0005_invoke_access_and_tokens"),
    ]

    operations = [
        migrations.AddField(
            model_name="buildpolicy",
            name="build_lease_seconds",
            field=models.PositiveIntegerField(default=3600),
        ),
        migrations.AddField(
            model_name="buildpolicy",
            name="max_builds_per_function_per_hour",
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name="buildpolicy",
            name="max_builds_per_user_per_hour",
            field=models.PositiveIntegerField(default=20),
        ),
        migrations.AddField(
            model_name="buildpolicy",
            name="max_concurrent_builds",
            field=models.PositiveIntegerField(default=2),
        ),
        migrations.AddField(
            model_name="buildpolicy",
            name="max_queued_builds_per_function",
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AddField(
            model_name="buildpolicy",
            name="max_queued_builds_per_user",
            field=models.PositiveIntegerField(default=5),
        ),
        migrations.CreateModel(
            name="BuildLease",
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
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "Active"),
                            ("released", "Released"),
                            ("expired", "Expired"),
                        ],
                        default="active",
                        max_length=20,
                    ),
                ),
                ("acquired_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("expires_at", models.DateTimeField()),
                ("released_at", models.DateTimeField(blank=True, null=True)),
                ("release_reason", models.CharField(blank=True, max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "build_attempt",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="leases",
                        to="functions.buildattempt",
                    ),
                ),
                (
                    "worker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="build_leases",
                        to="workers.workernode",
                    ),
                ),
            ],
            options={
                "ordering": ["-acquired_at"],
            },
        ),
    ]
