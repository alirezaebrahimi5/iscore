from rest_framework import generics, permissions, response, status

from .models import Score
from .serializers import *

from user.permissions import *


class ChooseScore(generics.GenericAPIView):
    """
    An endpoint to define Score measure
    """
    permission_classes = [IsSales_ManagerUser, IsManagementUser]
    serializer_class = [ScoreSerializer]
    
    def post(self, request, *args, **kwargs):
        pass
    
    def put(self, request, title, *args, **kwargs):
        pass


class UserDailyWorkAPIView(generics.GenericAPIView):
    """
    An endpoint for Users to see their daily time 
    """
    serializer_class = UserTimeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk, *args, **kwargs):
        return response.Response() 
    
    def get(self, request, *args, **kwargs):
        return response.Response()


class UserScoreAPIView(generics.GenericAPIView):
    """
    An endpoint for Users to see their scores
    """
    permission_classes = [IsVisitorUser, IsMEDREP_VisitorUser, IsConsultantUser]
    serializer_class = [UserGivenScoreSerializer]
    
    def post(self, request, pk, *args, **kwargs):
        return response.Response() 
    
    def get(self, request, *args, **kwargs):
        return response.Response()
