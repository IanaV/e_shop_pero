from django.db import models

# Create your models here.
from django.db import models

class Seller(models.Model):
    POSITION_CHOICES = [
        (0, 'Продавец'),
        (1, 'Старший продавец'),
        (2, 'Руководитель отдела продаж')
    ]

    first_name = models.CharField(max_length=64, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=64, blank=False, verbose_name='Фамилия')
    email = models.EmailField(max_length=64, blank=True, null=True, verbose_name='Почта')
    phone = models.CharField(max_length=32, blank=False, verbose_name='Номер телефона')
    date = models.DateField(blank=False, verbose_name='Дата контракта')
    position = models.IntegerField(
        blank=False,
        choices=POSITION_CHOICES,
        default=0,
        verbose_name='Должность'
    )

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'
        app_label = 'seller'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return f'/sellers/{self.id}'