import uuid

from django.db import migrations, models
import django.db.models.deletion

import apps.invocations.models


class Migration(migrations.Migration):
    dependencies = [("invocations", "0003_output_files_and_read_token")]

    operations = [
        migrations.RemoveConstraint(
            model_name="invocationoutputfile",
            name="unique_invocation_output_path",
        ),
        migrations.CreateModel(
            name="InvocationStagedCompletion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("job_id", models.UUIDField(db_index=True)),
                ("dispatch_attempt", models.PositiveIntegerField()),
                ("completion_id", models.CharField(max_length=200, unique=True)),
                ("status", models.CharField(choices=[("staged", "Staged"), ("committed", "Committed"), ("expired", "Expired")], db_index=True, default="staged", max_length=20)),
                ("terminal_status", models.CharField(blank=True, max_length=20)),
                ("result", models.JSONField(blank=True, default=dict)),
                ("stdout", models.TextField(blank=True)),
                ("stderr", models.TextField(blank=True)),
                ("exit_code", models.IntegerField(blank=True, null=True)),
                ("cold_start", models.BooleanField(default=False)),
                ("error_message", models.TextField(blank=True)),
                ("duration_ms", models.PositiveIntegerField(blank=True, null=True)),
                ("output_manifest", models.JSONField(blank=True, default=list)),
                ("artifact_commit_id", models.UUIDField(blank=True, null=True, unique=True)),
                ("expires_at", models.DateTimeField(db_index=True, default=apps.invocations.models.staged_completion_expiry)),
                ("committed_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("invocation", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="staged_completions", to="invocations.invocation")),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.AddField(
            model_name="invocationoutputfile",
            name="checksum_sha256",
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name="invocationoutputfile",
            name="staged_completion",
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="output_files", to="invocations.invocationstagedcompletion"),
        ),
        migrations.AddField(
            model_name="invocationoutputfile",
            name="status",
            field=models.CharField(choices=[("staged", "Staged"), ("committed", "Committed"), ("expired", "Expired")], db_index=True, default="committed", max_length=20),
        ),
        migrations.AlterField(
            model_name="invocationoutputfile",
            name="file",
            field=models.FileField(max_length=500, upload_to=apps.invocations.models.invocation_output_upload_to),
        ),
        migrations.AddConstraint(
            model_name="invocationstagedcompletion",
            constraint=models.UniqueConstraint(fields=("job_id", "dispatch_attempt"), name="unique_invocation_staged_job_attempt"),
        ),
        migrations.AddConstraint(
            model_name="invocationoutputfile",
            constraint=models.UniqueConstraint(fields=("staged_completion", "original_path"), name="unique_staged_completion_output_path"),
        ),
    ]
