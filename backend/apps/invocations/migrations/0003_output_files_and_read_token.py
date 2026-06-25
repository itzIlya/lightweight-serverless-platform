from django.db import migrations, models
import django.db.models.deletion

import apps.invocations.models


class Migration(migrations.Migration):
    dependencies = [
        ("invocations", "0002_input_files"),
    ]

    operations = [
        migrations.AddField(
            model_name="invocation",
            name="read_token_hash",
            field=models.CharField(blank=True, db_index=True, max_length=64),
        ),
        migrations.AddField(
            model_name="invocation",
            name="read_token_prefix",
            field=models.CharField(blank=True, db_index=True, max_length=16),
        ),
        migrations.CreateModel(
            name="InvocationOutputFile",
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
                    "file",
                    models.FileField(
                        upload_to=apps.invocations.models.invocation_output_upload_to
                    ),
                ),
                ("original_path", models.CharField(max_length=500)),
                ("safe_name", models.CharField(max_length=255)),
                ("content_type", models.CharField(blank=True, max_length=255)),
                ("size_bytes", models.PositiveIntegerField(default=0)),
                ("position", models.PositiveSmallIntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "invocation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="output_files",
                        to="invocations.invocation",
                    ),
                ),
            ],
            options={
                "ordering": ["position", "created_at"],
            },
        ),
        migrations.AddConstraint(
            model_name="invocationoutputfile",
            constraint=models.UniqueConstraint(
                fields=("invocation", "original_path"),
                name="unique_invocation_output_path",
            ),
        ),
    ]
