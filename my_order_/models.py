from django.db import models

from django import forms
# import sys
# from os import path
# sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

# import sys, os
# sys.path.append(os.path.abspath('../customer'))
# from customer.models import Customer
# from ..customer.models import Customer
# from e_shop.seller.models import Seller
#
# from e_shop.product.models import Product
# import os
# import sys
# sys.path.append(os.path.abspath('.'))

# import sys,os
# sys.path.append('../')
# from courses.models import Subject
# from customer.models import Customer
# sys.path.append(os.path.abspath('.'))

# from seller.models import Seller
#
# sys.path.append(os.path.abspath('.'))
# from product.models import Product


# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(
        'customer.Customer',
        on_delete=models.CASCADE,

        # related_name='customers',
        # related_query_name='customer',

        related_name='orders',
        related_query_name='order',

        verbose_name='Покупатель'
    )
    seller = models.ForeignKey(
        'seller.Seller',
        on_delete=models.CASCADE,

        related_name='orders',
        related_query_name='order',
        # related_name='sellers',
        # related_query_name='seller',

        verbose_name='Продавец'
    )
    product = models.ForeignKey(
        'product.Product',
        on_delete=models.CASCADE,


        # related_name='products',
        # related_query_name='product',

        related_name='orders',
        related_query_name='order',

        verbose_name='Продукт'
    )
    date = models.DateField(auto_now_add=True, verbose_name='Дата заказа')
    total = models.DecimalField(max_digits=19, decimal_places=2, default=0, verbose_name='Сумма продажи')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def get_absolute_url(self):
        return f'/orders/{self.id}'


