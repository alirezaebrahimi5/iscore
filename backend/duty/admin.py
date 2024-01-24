from django.contrib import admin

from .models import *


@admin.register(DefineTask)
class DTAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(VisitorTask)
class VTAdmin(admin.ModelAdmin):
    list_display = ['sale_manager', 'user', 'tasks']
    list_filter = ['user', 'tasks']


@admin.register(TaskDone)
class TDAdmin(admin.ModelAdmin):
    list_display = ['user', 'compeleted_task', 'task_done']
    list_filter = ['user', 'task_done']
