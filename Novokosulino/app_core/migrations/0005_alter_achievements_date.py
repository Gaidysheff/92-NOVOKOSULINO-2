# Generated by Django 4.2.7 on 2024-12-23 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0004_achievements_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
    ]