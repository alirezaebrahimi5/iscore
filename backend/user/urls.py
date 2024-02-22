from django.urls import path 
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import *


urlpatterns = [
    
    # TODO : Authentication 
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('login/otp/', CheckOTPAPIView.as_view(), name='otp-login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('verify-token/', TokenVerifyView.as_view(), name='verify-token'),
    
    # TODO : Registration
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('register/otp/', ActivateAccountAPIView.as_view(), name='otp-register'),
    
    # TODO : Reset password
    # path('reset/password/', GetUserIDNAPIView.as_view(), name='reset'),
    # path('reset/password/otp/', VerifyOTPAPIView.as_view(), name='otp-reset'),
    # path('reset/password/confirm/', ResetPasswordConfirmAPIView.as_view(), name='confirm'),
    
    # TODO : Sale manager
    # path('sale-manager-access-users/', SeeAllPersonnelAPIView.as_view()),
]
