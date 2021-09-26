from django import forms
# import sys
# sys.path.append(".")

# import sys
# from os import path
# sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import os
import sys
sys.path.append(os.path.abspath('.'))

from customer.models import Customer
sys.path.append(os.path.abspath('.'))

from seller.models import Seller

sys.path.append(os.path.abspath('.'))
from product.models import Product

from .models import Order




class OrderUpdateForm(forms.ModelForm):
    """ Убираем подчеркивание в селекте: -------"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].empty_label = 'Покупатель не выбран'
        self.fields['seller'].empty_label = 'Продавец не выбран'
        self.fields['product'].empty_label = 'Товар не выбран'

    class Meta:
        model = Order
        fields = '__all__'
        labels = {
            'customer': 'Покупатель',
            'seller': 'Продавец',
            'product': 'Товар(продукт)',
            'date': 'Дата продажи',
            'total': 'Сумма'
        }
        widgets = {
            'customer': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'seller': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'product': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'total': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }