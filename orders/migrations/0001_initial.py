# Generated by Django 5.1.4 on 2025-01-10 09:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("common", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CartItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(verbose_name="quantity")),
                ("subtotal", models.FloatField(verbose_name="subtotal")),
            ],
        ),
        migrations.CreateModel(
            name="DeliveryTariff",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("high", models.FloatField(verbose_name="High")),
                ("width", models.FloatField(verbose_name="Width")),
                ("weight", models.FloatField(verbose_name="Weight")),
                ("price", models.FloatField(verbose_name="Price")),
                ("delivery_time", models.TimeField(verbose_name="Delivery Time")),
            ],
        ),
        migrations.CreateModel(
            name="Discount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=60, verbose_name="Code")),
                ("max_limit_price", models.FloatField(verbose_name="Max Limit Price")),
                ("percentage", models.FloatField(verbose_name="Percentage")),
                ("start_date", models.DateTimeField(verbose_name="Start Date")),
                ("end_date", models.DateTimeField(verbose_name="End Date")),
                ("max_limit", models.IntegerField(verbose_name="Max Limit")),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("created", "Created"),
                            ("in_progress", "In progress"),
                            ("delivered", "Delivered"),
                            ("cancelled", "Cancelled"),
                            ("finished", "Finished"),
                        ],
                        default="created",
                        max_length=60,
                        verbose_name="Status",
                    ),
                ),
                ("total_price", models.FloatField(verbose_name="Total Price")),
                (
                    "payment_status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("created", "Created"),
                            ("pending", "Pending"),
                            ("paid", "Paid"),
                            ("cancelled", "Cancelled"),
                        ],
                        max_length=60,
                        null=True,
                        verbose_name="Payment Status",
                    ),
                ),
                (
                    "payment_method",
                    models.CharField(
                        blank=True,
                        max_length=60,
                        null=True,
                        verbose_name="Payment Method",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Branch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120, verbose_name="Name")),
                ("zip_code", models.CharField(max_length=10, verbose_name="Zip Code")),
                ("street", models.CharField(max_length=120, verbose_name="Street")),
                ("address", models.TextField(verbose_name="Address")),
                ("longitude", models.FloatField(verbose_name="Longitude")),
                ("latitude", models.FloatField(verbose_name="Latitude")),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="branches",
                        to="common.region",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Card",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "card_name",
                    models.CharField(max_length=120, verbose_name="Card Name"),
                ),
                (
                    "card_number",
                    models.CharField(max_length=16, verbose_name="Card Number"),
                ),
                ("expiry_date", models.DateField(verbose_name="Expiration Date")),
                ("cvv", models.CharField(max_length=3, verbose_name="CVV")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cards",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
