# Generated by Django 4.1.13 on 2023-11-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0002_alter_novokosulinoarchive_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='novokosulinoarchive',
            name='order',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2, verbose_name='Порядковый №'),
        ),
    ]