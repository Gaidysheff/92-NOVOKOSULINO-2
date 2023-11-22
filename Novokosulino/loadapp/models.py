from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    uploadedFile = models.FileField(
        upload_to="upload/%Y/%m/%d/", verbose_name='Файл')
    dateTimeOfUpload = models.DateTimeField(
        auto_now=True, verbose_name='Время создания')

    class Meta:
        verbose_name = 'Загруженный файл'
        verbose_name_plural = 'Загруженные файлы'

    def __str__(self):
        return self.title
