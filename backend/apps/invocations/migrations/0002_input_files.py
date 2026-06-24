from django.db import migrations, models
import django.db.models.deletion

from apps.invocations.models import invocation_input_upload_to


class Migration(migrations.Migration):

    dependencies = [
        ("invocations", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="InvocationInputFile",
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
                ("position", models.PositiveSmallIntegerField(default=0)),
                ("field_name", models.CharField(default="files", max_length=120)),
                ("original_name", models.CharField(max_length=255)),
                ("content_type", models.CharField(blank=True, max_length=255)),
                ("size_bytes", models.PositiveIntegerField(default=0)),
                (
                    "file",
                    models.FileField(upload_to=invocation_input_upload_to),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "invocation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="input_files",
                        to="invocations.invocation",
                    ),
                ),
            ],
            options={"ordering": ["position", "created_at"]},
        ),
    ]
