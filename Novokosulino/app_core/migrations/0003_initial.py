# Generated by Django 4.2.7 on 2024-10-17 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_core', '0002_delete_loadedfiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, max_length=50, null=True, verbose_name='Дата')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('image', models.ImageField(blank=True, null=True, upload_to='achievements/%Y/%m/%d/', verbose_name='Файл')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='achievements/%Y/%m/%d/', verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Проведённое мероприятие',
                'verbose_name_plural': 'Проведённые мероприятия',
            },
        ),
    ]