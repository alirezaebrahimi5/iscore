from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django_jalali.admin.filters import JDateFieldListFilter

from .models import User, Profile


@admin.register(User)
class Admin(UserAdmin):
    list_display = ('nid', 'mobile')
    filter_horizontal = ()
    list_filter = (
        ('joined_at', JDateFieldListFilter), 'is_active'
    )
    fieldsets = ()
    search_fields = ('nid', 'mobile')
    ordering = ('joined_at',)


@admin.register(Profile)
class PAdmin(admin.ModelAdmin):
    list_display = ['user', 'fullName']
