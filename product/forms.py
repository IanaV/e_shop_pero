from django import forms
from .models import  Product

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name': 'Название товара',
            'description': 'Описание',
            'image': 'Обожка товара(изображение)',
            'stock': 'Количество(шт)',
            'price': 'Цена'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }