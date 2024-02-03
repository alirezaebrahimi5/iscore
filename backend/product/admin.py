from django.contrib import admin

from .models import Product, Instance


@admin.register(Product)
class PAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'capacity', 'is_verified']
    prepopulated_fields = {'slug': ('title',),}
    list_filter = ['is_existed', 'is_verified', 'prod_type']


@admin.register(Instance)
class IAdmin(admin.ModelAdmin):
    list_display = ["product", "price", "capacity"]
