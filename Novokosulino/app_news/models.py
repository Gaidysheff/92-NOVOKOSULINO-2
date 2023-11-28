from django.db import models


class Post(models.Model):

    ACTUAL = 'ACT'
    ARCHIVE = 'ARC'

    STATUS = (
        (ACTUAL, 'Актуально'),
        (ARCHIVE, 'Архив'),
    )

    dateCreation = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')
    # date = models.DateField(default=datetime.datetime.today)
    title = models.CharField(max_length=128, verbose_name='Заголовок поста')
    overview = models.TextField(null=True, blank=True, verbose_name='Обзор')
    text = models.TextField(null=True, blank=True, verbose_name='Текст поста')
    order = models.DecimalField(max_digits=2, decimal_places=0, default=0, verbose_name='Порядковый №')
    status = models.CharField(max_length=3, choices=STATUS, default=ACTUAL, verbose_name='Статус')
    picture = models.ImageField(
        upload_to="pictures/%Y/%m/%d/", verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['order']
