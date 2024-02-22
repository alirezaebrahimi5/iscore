from django.contrib import admin

from .models import UserLocation, NewLocation

#
# @admin.register(UserLocation)
# class ULAdmin(admin.ModelAdmin):
#     list_display = ['user', 'where_is']
#     search_fields = ['user']
#
#
# @admin.register(NewLocation)
# class NLAdmin(admin.ModelAdmin):
#     list_display = ['user', 'title']
#     list_filter = ['saleManagerVerified']
#     search_fields = ['user', 'title']
