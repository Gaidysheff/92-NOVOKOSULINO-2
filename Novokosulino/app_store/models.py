from django.db import models


class NovokosulinoArchive(models.Model):

    YEAR = (
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
    )
    year = models.CharField(max_length=4, choices=YEAR,
                            default='2024', verbose_name='Год')
    text = models.CharField(max_length=200, blank=True,
                            null=True, verbose_name='Комментарий')
    uploadedImage = models.ImageField(
        upload_to="village/%Y/%m/%d/", verbose_name='Файл')
    dateOfUpload = models.DateField(
        auto_now=True, verbose_name='Дата загрузки')

    class Meta:
        verbose_name = 'АРХИВ "Новокосулино-2"'
        verbose_name_plural = 'АРХИВ "Новокосулино-2"'

    def __str__(self):
        return f'{self.text[:10]}...'
