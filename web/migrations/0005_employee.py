# Generated by Django 5.0.3 on 2024-05-06 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0004_rename_first_image_transformation_after_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("name", models.CharField(max_length=150)),
                ("position", models.CharField(max_length=150)),
                ("image", models.ImageField(upload_to="employee/")),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
    ]
