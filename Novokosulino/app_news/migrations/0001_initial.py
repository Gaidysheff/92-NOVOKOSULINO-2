# Generated by Django 4.1.13 on 2023-11-22 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок поста')),
                ('overview', models.TextField(blank=True, null=True, verbose_name='Обзор')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст поста')),
                ('picture', models.ImageField(upload_to='pictures/%Y/%m/%d/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-dateCreation', 'title'],
            },
        ),
    ]
