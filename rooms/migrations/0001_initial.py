# Generated by Django 4.1.5 on 2023-01-05 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('beds', models.IntegerField()),
                ('ranking', models.CharField(max_length=255)),
                ('services', models.ManyToManyField(default=None, related_name='Rooms', to='services.service')),
            ],
        ),
    ]