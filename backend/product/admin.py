from django.contrib import admin

from .models import Product, Product_by_Sales_Manager


@admin.register(Product)
class PAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'capacity', 'is_verified']
    prepopulated_fields = {
        'slug': ('title',),
    }
    list_filter = ['is_verified', 'prod_type']


@admin.register(Product_by_Sales_Manager)
class PSMAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    list_filter = ['product', 'is_represented']
