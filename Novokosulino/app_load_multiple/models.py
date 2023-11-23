from django.db import models


class UploadFilesMultiple(models.Model):
    file = models.FileField(
        upload_to='uploads_multiple/%Y/%m/%d/', verbose_name='Файл')
    uploaded_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата/Время загрузки')

    class Meta:
        verbose_name = 'Загруженный файл'
        verbose_name_plural = 'Загруженные файлы'
