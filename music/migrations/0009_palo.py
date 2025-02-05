# Generated by Django 5.0.4 on 2024-04-23 10:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0008_favoritecomposer"),
    ]

    operations = [
        migrations.CreateModel(
            name="Palo",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(null=True)),
                ("song", models.FileField(upload_to="palos/")),
            ],
        ),
    ]
