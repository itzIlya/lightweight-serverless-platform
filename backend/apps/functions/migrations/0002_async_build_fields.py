import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("functions", "0001_initial"),
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
                    ("built", "Built"),
                    ("failed", "Failed"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="functionversion",
            name="build_request_id",
            field=models.UUIDField(
                default=uuid.uuid4,
                db_index=True,
                editable=False,
            ),
        ),
        migrations.AddField(
            model_name="functionversion",
            name="build_queued_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="functionversion",
            name="build_started_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="functionversion",
            name="build_finished_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
