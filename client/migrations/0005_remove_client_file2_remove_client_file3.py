# Generated by Django 5.0.2 on 2024-03-06 07:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("client", "0004_remove_client_qr_code_qrcode"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="client",
            name="file2",
        ),
        migrations.RemoveField(
            model_name="client",
            name="file3",
        ),
    ]
