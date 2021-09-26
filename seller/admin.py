from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'email', 'phone', 'date', 'position']