from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="workernode",
            name="max_build_concurrency",
            field=models.PositiveIntegerField(default=1),
        ),
    ]
