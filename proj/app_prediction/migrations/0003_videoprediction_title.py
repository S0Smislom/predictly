# Generated by Django 5.1.5 on 2025-01-25 18:32

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "app_prediction",
            "0002_imageprediction_height_imageprediction_thumbhash_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="videoprediction",
            name="title",
            field=models.CharField(
                default=datetime.datetime(
                    2025, 1, 25, 18, 32, 15, 126463, tzinfo=datetime.timezone.utc
                ),
                max_length=120,
            ),
            preserve_default=False,
        ),
    ]
