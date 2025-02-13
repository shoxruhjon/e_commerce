# Generated by Django 5.1.4 on 2025-01-20 11:02

import accounts.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_alter_user_address_alter_user_is_active_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="verifictionotp",
            name="code",
            field=models.IntegerField(
                validators=[accounts.utils.check_otp_code], verbose_name="Otp code"
            ),
        ),
    ]
