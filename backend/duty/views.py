from rest_framework import generics, status, response

from .serializers import *

from user.permissions import *


class SaleManagerSetTask(generics.GenericAPIView):
    """
    An endpoint for Sale Manager to introduce the tasks to Visitors, MEDREP & Consultant
    """
    permission_classes = [IsSales_ManagerUser]
    serializer_class = [VisitorTaskSerializer]
    
    def post(self, *args, **kwargs):
        return response.Response()
    
    def get(self, *args, **kwargs):
        return response.Response()


class PersonnelTaskOverView(generics.GenericAPIView):
    """
    An endpoint for Visitors, MEDREP & Consultant to see their tasks
    """
    permission_classes = [IsVisitorUser, IsConsultantUser, IsMEDREP_VisitorUser]
    serializer_class = [VisitorTaskSerializer]
    
    def post(self, request, *args, **kwargs):
        return response.Response()
    
    def get(self, request, *args, **kwargs):
        return response.Response()


class PersonnelFinishedTask(generics.GenericAPIView):
    """
    An endpoint for Visitors, MEDREP & Consultant to mark the finished work
    """    
    permission_classes = [IsVisitorUser, IsConsultantUser, IsMEDREP_VisitorUser]
    serializer_class = []
    
    def post(self, request, *args, **kwargs):
        return response.Response()
    
    def get(self, request, *args, **kwargs):
        return response.Response()
