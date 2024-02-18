from rest_framework import generics, permissions, status, response, filters

from .models import Product
from .serializers import *

from user.permissions import *


############################## Sale managers concern ##############################


class SaleManagerCreateProductAPIView(generics.GenericAPIView):
    """
    An endpoint for Sale managers to create a Product by its own
    """
    permission_classes = [IsSales_ManagerUser, IsManagementUser]
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        return self.serializer(user=self.request.user.id)
    
    def post(self, request, *args, **kwargs):
        ps = ProductSerializer(data=request.data)
        if ps.is_valid():
            ps.save()
            return response.Response(ps.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, title, *args, **kwargs):
        p = Product.objects.get(title=title)
        ps = ProductSerializer(instance=p, data=request.data)
        if ps.is_valid():
            ps.save()
            return response.Response(ps.data, status=status.HTTP_205_RESET_CONTENT)
        else:
            return response.Response(ps.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def get(self, request, *args, **kwargs):
        pass


class SaleManagerVerifiedProduct(generics.GenericAPIView):
    """
    An endpoint for Sale managers to verify a product that has been created by Visitors
    """
    permission_classes = [IsManagementUser, IsSales_ManagerUser]
    serializer_class = [ProductSerializer]
    
    def perform_create(self, serializer):
        return self.serializer(user=self.request.user.id)
    
    def put(self, request, title, *args, **kwargs):
        p = Product.objects.get(title=title)
        ps = ProductSerializer(instance=p, data=request.data)
        if ps.is_valid():
            ps.save()
            return response.Response(ps.data, status=status.HTTP_205_RESET_CONTENT)
        else:
            return response.Response(ps.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


############################## Visitors concern ##############################


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


class SearchProduct(generics.ListAPIView):
    """
    An endpoint for Users to find specific products
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = [ProductSerializer]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'prod_type', 'is_exisited', 'is_verified', 'price', 'capacity']


class AllInstanceAPIView(generics.GenericAPIView):
    """
    An endpoint for Visitors to show exsiting instnaces
    """
    permission_classes = [IsVisitorUser, IsMEDREP_VisitorUser, IsConsultantUser]
    # queryset = Product.objects.filter(is_verified=True).filter(is_exisited=True)
    serializer_class = [InstanceSerializer]
    
    def post(self, request, *args, **kwargs):
        pass
