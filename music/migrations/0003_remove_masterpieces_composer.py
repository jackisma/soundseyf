# Generated by Django 5.0.4 on 2024-04-05 19:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0002_composers_masterpieces_composer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="masterpieces",
            name="Composer",
        ),
    ]
