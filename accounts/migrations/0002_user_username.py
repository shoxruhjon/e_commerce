# Generated by Django 5.1.4 on 2025-01-07 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="username",
            field=models.CharField(
                blank=True,
                error_messages={"unique": "A user with that username already exists."},
                max_length=150,
                null=True,
                verbose_name="username",
            ),
        ),
    ]
