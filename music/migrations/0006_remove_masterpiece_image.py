# Generated by Django 5.0.4 on 2024-04-06 15:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0005_composer_genre"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="masterpiece",
            name="image",
        ),
    ]
