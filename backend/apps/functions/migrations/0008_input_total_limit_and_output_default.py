from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("functions", "0007_declared_output_files"),
    ]

    operations = [
        migrations.AddField(
            model_name="functionversion",
            name="invocation_input_max_total_size_mb",
            field=models.PositiveSmallIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name="functionversion",
            name="invocation_output_max_total_size_mb",
            field=models.PositiveSmallIntegerField(default=10),
        ),
    ]
