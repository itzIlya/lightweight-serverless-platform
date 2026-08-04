from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("functions", "0012_functioninvoketoken_revoked_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="functionversion",
            name="invocation_max_retries",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="functionversion",
            name="invocation_retry_backoff_seconds",
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name="functionversion",
            name="retry_invocation_function_errors",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="functionversion",
            name="retry_invocation_timeouts",
            field=models.BooleanField(default=False),
        ),
    ]
