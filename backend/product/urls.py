from django.urls import path

from .views import *


urlpatterns = [
    path('sale-manager/create-product/', SaleManagerCreateProductAPIView.as_view(), name=''),
    path('create-product/visitor/', SaleManagerReserveProductAPIView.as_view(), name=''),
    path('visitor-tasks/', sendProductInfoAPIView.as_view(), name=''),
    path('sale-manager/visistor-tasks-done/', SendSuccessedProductAPIView.as_view(), name=''),
    path('visitors-create-products/', VisitorCreatProductAPIView.as_view(), name=''),
]
