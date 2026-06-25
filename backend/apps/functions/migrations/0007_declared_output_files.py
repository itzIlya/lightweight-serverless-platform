from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("functions", "0006_build_limits_and_leases"),
    ]

    operations = [
        migrations.AddField(
            model_name="functionversion",
            name="declared_output_files",
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name="functionversion",
            name="invocation_output_max_files",
            field=models.PositiveSmallIntegerField(default=5),
        ),
        migrations.AddField(
            model_name="functionversion",
            name="invocation_output_max_file_size_mb",
            field=models.PositiveSmallIntegerField(default=10),
        ),
        migrations.AddField(
            model_name="functionversion",
            name="invocation_output_max_total_size_mb",
            field=models.PositiveSmallIntegerField(default=25),
        ),
    ]
