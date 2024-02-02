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
        s = ScoreSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return response.Response(s.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def put(self, request, title, *args, **kwargs):
        s = ScoreSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return response.Response(s.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def get(self, request, *args, **kwargs):
        pass


class UserDailyWorkAPIView(generics.GenericAPIView):
    """
    An endpoint for Users to see their daily time 
    """
    serializer_class = UserTimeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk, *args, **kwargs):
        s = UserTimeSerializer(data=request.data)
        return response.Response(s.data, status=status.HTTP_200_OK) 
    
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
