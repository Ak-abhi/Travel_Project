# Generated by Django 4.2.5 on 2023-10-27 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
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
                ("t_name", models.CharField(max_length=150)),
                ("t_img", models.ImageField(upload_to="images")),
                ("t_desc", models.TextField()),
            ],
        ),
    ]
