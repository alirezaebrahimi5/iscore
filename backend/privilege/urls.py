from django.urls import path 

from .views import *


urlpatterns = [
    path('user-daily-work/', UserDailyWorkAPIView.as_view(), name=''),
]
