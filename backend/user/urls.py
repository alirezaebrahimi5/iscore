from django.urls import path 
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import *


urlpatterns = [
    # Auth view sets
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('check-otp-token/', CheckOTPAPIView.as_view(), name='check-otp-token'),
    path('remember-me/', TokenRefreshView.as_view(), name='refresh'),
    path('verify-token/', TokenVerifyView.as_view(), name='verify-token'),
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
]
