# Generated by Django 5.0.2 on 2024-03-04 13:26

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("thumbnail1", models.ImageField(blank=True, upload_to="products/")),
                ("thumbnail2", models.ImageField(blank=True, upload_to="products/")),
                ("thumbnail3", models.ImageField(blank=True, upload_to="products/")),
                ("thumbnail4", models.ImageField(blank=True, upload_to="products/")),
                ("thumbnail5", models.ImageField(blank=True, upload_to="products/")),
                ("video", models.FileField(blank=True, upload_to="products/videos/")),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("supplier", models.CharField(max_length=255)),
                ("release_date", models.DateField()),
            ],
        ),
    ]
