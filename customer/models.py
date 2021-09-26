from django.db import models

# Create your models here.
from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=64, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=64, blank=False, verbose_name='Фамилия')
    email = models.EmailField(max_length=64, blank=True, null=True, verbose_name='Почта')
    phone = models.CharField(max_length=32, blank=False, verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
        app_label = 'customer'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return f'/customer/{self.id}'