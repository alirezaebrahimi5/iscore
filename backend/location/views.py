from rest_framework import response, generics, status, permissions

from .models import UserLocation, NewLocation
from .serializers import LocationSerializer, NewLocationSerializer

from user.permissions import *


class AllUsersAllLocationsAPIView(generics.GenericAPIView):
    """
    An endpoint for Sale manager to see all User's location
    """
    permission_classes = [IsManagementUser, IsSales_ManagerUser]
    serializer_class = LocationSerializer
    
    def post(self, request, *args, **kwargs):
        all_u_l = UserLocation.objects.all()
        serializer_u_l = LocationSerializer(all_u_l, many=True)
        return response.Response(serializer_u_l.data, status=status.HTTP_200_OK)
    
    def get(self, request, *args, **kwargs):
        pass


class AllUsersLatestLocationsAPIView(generics.GenericAPIView):
    """
    An endpoint for Sale manager to see latest location of any Users
    """
    permission_classes = [IsManagementUser, IsSales_ManagerUser]
    serializer_class = LocationSerializer
    
    def get(self, request, *args, **kwargs):
        all_u_l = UserLocation.objects.all().latest()
        serializer_u_l = LocationSerializer(all_u_l, many=True)
        return response.Response(serializer_u_l.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        pass


class AnyUserLocationAPIView(generics.GenericAPIView):
    """
    An endpoint for Sale managers to 
    """
    permission_classes = [IsManagementUser, IsSales_ManagerUser]
    serializer_class = LocationSerializer
    
    def get(self, request, pk, *args, **kwargs):
        pass
    
    def post(self, request, pk, *args, **kwargs):
        try:
            all_u_l = UserLocation.objects.get(pk=pk)
            serializer = LocationSerializer(all_u_l)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response("This User does not exist!", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, *args, **kwargs):
        pass


class AddNewLocationAPIView(generics.GenericAPIView):
    """
    An endpoint for Users to enter the new location that has been found
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NewLocationSerializer
    
    def perform_create(self, serializer):
        return self.serializer(user=self.request.user.id)
    
    def post(self, request, pk, *args, **kwargs):
        ls = NewLocationSerializer(data=request.data)
        if ls.is_valid():
            ls.save()
        return response.Response(ls.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        return response.Response()
    
    def put(self, request, pk, *args, **kwargs):
        pass


class VerifyLocation(generics.GenericAPIView):
    """
    An endpoint for Sale manager to verify the new location
    """
    permission_classes = [IsSales_ManagerUser, IsManagementUser]
    serializer_class = [NewLocationSerializer]
    
    def perform_create(self, serializer):
        return self.serializer(user=self.request.user.id)
    
    def post(self, request, *args, **kwargs):
        ls = NewLocationSerializer(data=request.data)
        if ls.is_valid():
            ls.data["saleManagerVerified"] = True
            ls.save()
        return response.Response(ls.data, status=status.HTTP_205_RESET_CONTENT)
    
    def get(self, request, *args, **kwargs):
        return response.Response()
