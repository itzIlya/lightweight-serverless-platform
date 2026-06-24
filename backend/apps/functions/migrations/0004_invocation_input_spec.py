from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("functions", "0003_build_attempts_and_policy"),
    ]

    operations = [
        migrations.AddField(
            model_name="functionversion",
            name="invocation_input_mime_types",
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name="functionversion",
            name="invocation_input_max_files",
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name="functionversion",
            name="invocation_input_max_size_mb",
            field=models.PositiveSmallIntegerField(default=10),
        ),
    ]
