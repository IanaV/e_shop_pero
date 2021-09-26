from django.contrib import admin
from .models import  Product
from django.utils.safestring import mark_safe

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock', 'price', 'product_image']
    readonly_fields = ['product_image']

    def product_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=obj.image.width / 2,
            height=obj.image.height / 2,
        )
        )

    product_image.short_description = 'Изображение'
