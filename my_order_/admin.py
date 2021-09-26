from django.contrib import admin
from .models import Order
from django.utils.safestring import mark_safe

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'seller', 'product', 'date', 'total']
