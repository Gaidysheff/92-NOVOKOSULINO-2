# Generated by Django 4.1.13 on 2023-11-25 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novokosulinoarchive',
            name='text',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Комментарий'),
        ),
    ]
