from rest_framework import generics, permissions, status

from .serializers import *

from user.permissions import *


class SaleManagerCreateProductAPIView(generics.GenericAPIView):
    """
    An endpoint for Sale manager to create a Product by its own
    """
    permission_classes = [IsSales_ManagerUser, IsManagementUser]
    serializer_class = ProductSerializer
    
    def post(self, request, *args, **kwargs):
        pass
    
    def get(self, request, *args, **kwargs):
        pass


class SaleManagerReserveProductAPIView(generics.GenericAPIView):
    """
    An endpoint for Sale manager to create tasks for Visitors
    """
    permission_classes = [IsSales_ManagerUser, IsManagementUser]
    serializer_class = [Product_by_Sales_ManagerSerializer]
    
    def post(self, request, *args, **kwargs):
        pass
    
    def get(self, request, *args, **kwargs):
        pass


class sendProductInfoAPIView(generics.GenericAPIView):
    """
    An endpoint for Visitors to see their tasks
    """ 
    permission_classes = [IsSales_ManagerUser]
    serializer_class = [Product_by_Sales_ManagerSerializer]
    
    def post(self, request, *args, **kwargs):
        pass
    
    def get(self, request, *args, **kwargs):
        pass


class SendSuccessedProductAPIView(generics.GenericAPIView):
    """
    An endpoint for Sale manager to see Visitors tasks
    """
    permission_classes = [IsVisitorUser, IsMEDREP_VisitorUser, IsConsultantUser]
    serializer_class = [Product_by_Sales_ManagerSerializer]
    
    def post(self, request, *args, **kwargs):
        pass
    
    def get(self, request, *args, **kwargs):
        pass


class VisitorCreatProductAPIView(generics.GenericAPIView):
    """
    An endpoint for Visitors to create a product and inform Sale managers
    """
    permission_classes = [IsVisitorUser, IsMEDREP_VisitorUser, IsConsultantUser]
    serializer_class = [ProductSerializer]
    
    def post(self, request, *args, **kwargs):
        pass
    
    def get(self, request, *args, **kwargs):
        pass
