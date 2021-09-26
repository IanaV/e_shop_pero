from django import forms

import os
import sys
# sys.path.append(os.path.abspath('.'))
# from ..my_order_.models import Order
# from customer.models import Customer
# from ..my_order_.models import Order

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from my_order_.models import Order

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from product.models import Product

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from seller.models import Seller



class ReportForm1(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['seller'].empty_label = 'Выбирете продавца из списка'

    class Meta:
        model = Order
        fields = ['seller']
        widgets = {
            'seller': forms.Select(
                attrs={
                    'class': 'form-select ml-3',
                }
            )
        }

class ReportForm2(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].empty_label = 'Выбирете продукт из списка'

    class Meta:
        model = Order
        fields = ['product']
        widgets = {
            'product': forms.Select(
                attrs={
                    'class': 'form-select  ml-4 mr-4',
                }
            )
        }

class ReportForm3(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['date']
        labels = {
            'date': 'Дата продажи',
        }
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            )
        }