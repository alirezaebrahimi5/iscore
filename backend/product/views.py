from rest_framework import generics, permissions, status, response

from .serializers import *

from user.permissions import *


class SaleManagerCreateProductAPIView(generics.GenericAPIView):
    """
    An endpoint for Sale manager to create a Product by its own
    """
    permission_classes = [IsSales_ManagerUser, IsManagementUser]
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        return self.serializer(user=self.request.user.id)
    
    def post(self, request, *args, **kwargs):
        ps = ProductSerializer(data=request.data)
        if ps.is_valid():
            ps.save(is_verified=True)
            return response.Response(ps.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, *args, **kwargs):
        pass
    
    def get(self, request, *args, **kwargs):
        pass


class VisitorCreatProductAPIView(generics.GenericAPIView):
    """
    An endpoint for Visitors to create a product and inform Sale managers
    """
    permission_classes = [IsVisitorUser, IsMEDREP_VisitorUser, IsConsultantUser]
    serializer_class = [ProductSerializer]
    
    def perform_create(self, serializer):
        return self.serializer(user=self.request.user.id)
    
    def post(self, request, *args, **kwargs):
        ps = ProductSerializer(data=request.data)
        if ps.is_valid():
            ps.save()
            return response.Response(ps.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        pass
