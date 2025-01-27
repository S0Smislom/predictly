# Generated by Django 5.1.5 on 2025-01-27 02:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_prediction", "0004_alter_audioprediction_title_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="prediction",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
