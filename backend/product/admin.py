from django.contrib import admin

from .models import Product


@admin.register(Product)
class PAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'capacity', 'is_verified']
    prepopulated_fields = {'slug': ('title',),}
    list_filter = ['is_verified', 'prod_type']
