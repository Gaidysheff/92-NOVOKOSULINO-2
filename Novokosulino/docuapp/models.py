from django.db import models


class LoadedDocuments(models.Model):
    title = models.CharField(max_length=100, blank=True,
                             null=True, verbose_name='Заголовок')
    file_docu = models.FileField(upload_to='documents/%Y/%m/%d/',
                                 verbose_name='Файл')
    icon = models.ImageField(
        upload_to='documents/%Y/%m/%d/', blank=True, null=True, verbose_name='Иконка')

    class Meta:
        verbose_name = 'Загруженный документ'
        verbose_name_plural = 'Загруженные документы'

    def __str__(self):
        return self.title
