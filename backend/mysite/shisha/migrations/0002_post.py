# Generated by Django 5.0.4 on 2024-12-17 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shisha", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("user_name", models.CharField(max_length=32)),
                ("body", models.TextField()),
                ("shop", models.TextField()),
                ("memo", models.TextField()),
            ],
        ),
    ]
