# Generated by Django 4.1.7 on 2023-12-11 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend_api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SitePost",
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
                ("title", models.CharField(max_length=100000)),
                ("description", models.CharField(max_length=100000)),
            ],
        ),
        migrations.DeleteModel(
            name="YouTubeVideo",
        ),
    ]
