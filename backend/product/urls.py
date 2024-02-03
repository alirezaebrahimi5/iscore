from django.urls import path

from .views import *


urlpatterns = [
    path('sale-manager-create-product/', SaleManagerCreateProductAPIView.as_view()),
    path('sale-manager-verify-product/', SaleManagerVerifiedProduct.as_view()),
    
    path('visitor-create-product/', VisitorCreatProductAPIView.as_view()),
    path('all-instance-for-customers/', AllInstanceAPIView.as_view()),
]
