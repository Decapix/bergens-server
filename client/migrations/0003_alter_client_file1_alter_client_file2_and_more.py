# Generated by Django 5.0.2 on 2024-03-04 17:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("client", "0002_client_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="file1",
            field=models.FileField(blank=True, null=True, upload_to="fichiers/"),
        ),
        migrations.AlterField(
            model_name="client",
            name="file2",
            field=models.FileField(blank=True, null=True, upload_to="fichiers/"),
        ),
        migrations.AlterField(
            model_name="client",
            name="file3",
            field=models.FileField(blank=True, null=True, upload_to="fichiers/"),
        ),
    ]
