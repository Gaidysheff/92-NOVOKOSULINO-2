from django.db import models


class LoadedFiles (models.Model):
    text = models.CharField(max_length=100, blank=True,
                            null=True, verbose_name='Текст')
    file = models.ImageField(upload_to='upload/%Y/%m/%d/',
                             verbose_name='Изображение')

    class Meta:
        verbose_name = 'Загруженный файл'
        verbose_name_plural = 'Загруженные файлы'
