from django.urls import path

from .views import *


urlpatterns = [
    path('sale-manager/create-product/', SaleManagerCreateProductAPIView.as_view(), name=''),
    path('visitors-create-products/', VisitorCreatProductAPIView.as_view(), name=''),
]
