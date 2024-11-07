# Generated by Django 5.1.2 on 2024-11-07 14:38

import vies.models
from django.db import migrations

import weblate_web.payments.validators


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0036_alter_payment_currency"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="vat",
            field=vies.models.VATINField(
                blank=True,
                default="",
                help_text="Please fill in European Union VAT ID, leave blank if not applicable.",
                max_length=14,
                null=True,
                validators=[weblate_web.payments.validators.validate_vatin],
                verbose_name="European VAT ID",
            ),
        ),
    ]
