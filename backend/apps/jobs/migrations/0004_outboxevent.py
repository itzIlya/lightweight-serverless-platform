import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0003_job_coordination_version"),
    ]

    operations = [
        migrations.CreateModel(
            name="OutboxEvent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("event_id", models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ("aggregate_id", models.UUIDField(db_index=True)),
                ("event_type", models.CharField(max_length=80)),
                ("payload", models.JSONField(default=dict)),
                ("publish_attempts", models.PositiveIntegerField(default=0)),
                ("published_at", models.DateTimeField(blank=True, db_index=True, null=True)),
                ("stream_id", models.CharField(blank=True, max_length=128)),
                ("last_error", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["created_at"]},
        ),
    ]
