from rest_framework import generics, status, response

from .serializers import DefineTaskSerializer, VisitorTaskSerializer

from user.permissions import *


class WriteTaskAPIView(generics.GenericAPIView):
    serializer_class = [DefineTaskSerializer]
    permission_classes = [IsSales_ManagerUser, IsManagementUser]
    
    def post(self, request, *args, **kwargs):
        pass
