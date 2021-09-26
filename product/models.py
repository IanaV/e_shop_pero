from django.db import models

# Create your models here.
from django.db import models






class Product(models.Model):
    name = models.CharField(max_length=64, blank=False, verbose_name='Наименование')
    description = models.TextField(blank=True, default='', verbose_name='Описание')
    image = models.ImageField(upload_to='product_images/%Y/%m/%d', verbose_name='Изображение')
    stock = models.IntegerField(blank=True, default=0, verbose_name='В наличии (шт)')
    price = models.DecimalField(max_digits=19, decimal_places=2, default=0, verbose_name='Цена')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        app_label = 'product'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/products/{self.id}'


