# Generated by Django 5.1.3 on 2024-11-27 12:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("weblate_web", "0034_service_backup_size_service_backup_timestamp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="backup_size",
            field=models.BigIntegerField(default=0),
        ),
    ]
