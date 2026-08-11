from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("functions", "0013_invocation_retry_policy"),
        ("invocations", "0006_invocationattempt"),
    ]

    operations = [
        migrations.AddField(
            model_name="invocation",
            name="invocation_auth_type",
            field=models.CharField(
                choices=[
                    ("owner_jwt", "Owner JWT"),
                    ("function_token", "Function token"),
                    ("public", "Public"),
                ],
                default="owner_jwt",
                max_length=30,
            ),
        ),
        migrations.AddField(
            model_name="invocation",
            name="invocation_token",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="invocations",
                to="functions.functioninvoketoken",
            ),
        ),
    ]
