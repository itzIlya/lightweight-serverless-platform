from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("jobs", "0004_outboxevent")]

    operations = [
        migrations.AddIndex(
            model_name="job",
            index=models.Index(
                fields=["coordination_version", "status", "updated_at"],
                name="jobs_job_coordin_03a362_idx",
            ),
        ),
    ]
