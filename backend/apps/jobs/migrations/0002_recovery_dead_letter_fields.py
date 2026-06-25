from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="status",
            field=models.CharField(
                choices=[
                    ("queued", "Queued"),
                    ("dispatched", "Dispatched"),
                    ("running", "Running"),
                    ("succeeded", "Succeeded"),
                    ("failed", "Failed"),
                    ("cancelled", "Cancelled"),
                    ("dead_lettered", "Dead-lettered"),
                ],
                default="queued",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="job",
            name="recovery_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="job",
            name="max_recovery_attempts",
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AddField(
            model_name="job",
            name="last_recovered_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="job",
            name="dead_lettered_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="job",
            name="dead_letter_reason",
            field=models.TextField(blank=True),
        ),
    ]
