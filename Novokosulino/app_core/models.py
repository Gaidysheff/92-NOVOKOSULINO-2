from django.db import models
from django.urls import reverse


class Achievements(models.Model):
    YEAR = (
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
        ('2028', '2028'),
        ('2029', '2029'),
    )
    year = models.CharField(max_length=4, choices=YEAR,
                            default='2024', verbose_name='Год')
    date = models.DateField(verbose_name='Дата')
    text = models.TextField(blank=True,  null=True, verbose_name="Текст")
    image = models.ImageField(
        upload_to='achievements/%Y/%m/%d/', blank=True, null=True, verbose_name='Файл')
    icon = models.ImageField(
        upload_to='achievements/%Y/%m/%d/', blank=True, null=True, verbose_name='Иконка')

    class Meta:
        verbose_name = 'Проведённое мероприятие'
        verbose_name_plural = 'Проведённые мероприятия'

    def __str__(self):
        return f"{self.text[:5]}..."

    def get_absolute_url(self):
        return reverse('achive', kwargs={'achive_id': self.pk})
