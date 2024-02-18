from django.contrib import admin

from .models import *


@admin.register(VisitorTask)
class VTAdmin(admin.ModelAdmin):
    list_display = ['sale_manager']
    # list_filter = ['user', 'tasks']


@admin.register(VisitorTaskDone)
class TDAdmin(admin.ModelAdmin):
    list_display = ['user', 'task_done']
    list_filter = ['task_done']
