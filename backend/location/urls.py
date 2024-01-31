from django.urls import path 

from .views import *


urlpatterns = [
    path('all-users-locations/', AllUsersAllLocationsAPIView.as_view(), name=''),
    path('all-users-latest-locations/', AllUsersLatestLocationsAPIView.as_view(), name=''),
    path('any-user-location/', AnyUserLocationAPIView.as_view(), name=''),
    path('new-location/', AddNewLocationAPIView.as_view(), name=''),
    path('verify-locations/', VerifyLocation.as_view(), name=''),
]
