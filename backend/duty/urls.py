from django.urls import path 

from .views import *


urlpatterns = [
    path('sale-manager/define-tasks/', SaleManagerSetTask.as_view(), name=''),
    path('personnel-task-overview/', PersonnelTaskOverView.as_view(), name=''),
]
