from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0002_recovery_dead_letter_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="coordination_version",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "V1 - Django/PostgreSQL"),
                    (2, "V2 - Redis orchestrator"),
                ],
                db_index=True,
                default=1,
            ),
        ),
    ]
