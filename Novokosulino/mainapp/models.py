from django.db import models


class LoadedFiles(models.Model):
    text = models.CharField(max_length=100, blank=True,
                            null=True, verbose_name='Текст')
    file = models.ImageField(upload_to='upload/%Y/%m/%d/',
                             verbose_name='Изображение')

    class Meta:
        verbose_name = 'Загруженный файл'
        verbose_name_plural = 'Загруженные файлы'

    def __str__(self):
        return f'{self.text[:10]}...'


class LoadedDocuments(models.Model):
    title = models.CharField(max_length=100, blank=True,
                             null=True, verbose_name='Заголовок')
    file_docu = models.FileField(upload_to='documents/%Y/%m/%d/',
                                 verbose_name='Файл')

    class Meta:
        verbose_name = 'Загруженный документ'
        verbose_name_plural = 'Загруженные документы'

    def __str__(self):
        return self.title
