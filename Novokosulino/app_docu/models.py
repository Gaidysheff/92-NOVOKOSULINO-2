from django.db import models
from django.urls import reverse


class LoadedDocuments(models.Model):
    title = models.CharField(max_length=100, blank=True,
                             null=True, verbose_name='Заголовок')
    date = models.CharField(max_length=50, blank=True,
                            null=True, verbose_name='Дата документа')
    file_docu = models.FileField(upload_to='documents/%Y/%m/%d/',
                                 blank=True,  null=True, verbose_name='Файл')
    icon = models.ImageField(
        upload_to='documents/%Y/%m/%d/',
        blank=True, null=True, verbose_name='Иконка'
    )
    cat = models.ForeignKey(
        'Category', on_delete=models.PROTECT, related_name='docus',
        verbose_name="Категории"
    )
    content = models.TextField(blank=True,  null=True, verbose_name="Текст")

    class Meta:
        verbose_name = 'Загруженный документ'
        verbose_name_plural = 'Загруженные документы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('docu', kwargs={'docu_id': self.pk})


class Category(models.Model):
    name = models.CharField(
        max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
