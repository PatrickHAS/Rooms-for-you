# Generated by Django 4.1.5 on 2023-01-11 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[(0, 'Péssimo'), (1, 'Ruim'), (2, 'Regular'), (3, 'Bom'), (4, 'Muito Bom'), (5, 'Excelente')], max_length=12)),
                ('description', models.CharField(max_length=256, null=True)),
            ],
        ),
    ]