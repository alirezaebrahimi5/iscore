from django.urls import path 

from .views import *


urlpatterns = [
    path('all/tasks/', WriteTaskAPIView.as_view(), name='all-tasks'),
]
