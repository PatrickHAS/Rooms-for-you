# Generated by Django 4.1.5 on 2023-03-24 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotels', to=settings.AUTH_USER_MODEL),
        ),
    ]
