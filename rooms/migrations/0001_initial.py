# Generated by Django 4.1.5 on 2023-01-11 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("services", "0001_initial"),
        ("hotels", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
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
                ("number", models.IntegerField()),
                ("beds", models.IntegerField()),
                ("ranking", models.CharField(max_length=255)),
                (
                    "hotel",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rooms",
                        to="hotels.hotel",
                    ),
                ),
                (
                    "services",
                    models.ManyToManyField(
                        default=None, related_name="Rooms", to="services.service"
                    ),
                ),
            ],
        ),
    ]
