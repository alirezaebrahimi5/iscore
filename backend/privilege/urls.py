from django.urls import path 

from .views import *


urlpatterns = [
    path('user-daily-work/', ChooseScore.as_view(), name=''),
    path('choose-score/', UserDailyWorkAPIView.as_view(), name=''),
    path('user-score/', UserScoreAPIView.as_view(), name=''),
]
