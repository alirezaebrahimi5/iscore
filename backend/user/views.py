from django.conf import settings

from rest_framework import permissions, response, status, generics, filters
from rest_framework_simplejwt import tokens

from .models import User, OTP
from .permissions import *
from .serializers import *
from .utils import *


OTP_SECRET = settings.OTP_SECRET_KEY


####################### Authentication section #######################


class UserLoginAPIView(generics.GenericAPIView):
    """
    An endpoint to login users.
    """
    
    permission_classes = (permissions.AllowAny,)
    serializer_class = [LoginUserSerializer]

    def post(self, request, *args, **kwargs):
        s = LoginUserSerializer(data=request.data)
        if s.is_valid():
            idn = s.validated_data["identificationCode"]
            user = User.objects.get(identificationCode=idn)
            otp_token = sendToken(user=user)
            OTP.objects.create(user=user,otp=otp_token).save()
        return response.Response(s.data, status=status.HTTP_200_OK)


class CheckOTPAPIView(generics.GenericAPIView):
    """
    An endpoint for users to send their OTP tokens
    """
    
    def post(self, request, *args, **kwargs):
        s = OTPSerializer(data=request.data)
        if s.is_valid():
            otp = s.validated_data["otp"]
            if OTP.objects.get(otp=otp):
                # TODO : `uo` is stands for User OTP
                uo = OTP.objects.get(otp=otp)
                user = User.objects.get(phone=uo.user)
                token = tokens.RefreshToken.for_user(user)
                data = s.data
                data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}                
                uo.delete()
                return response.Response(data, status=status.HTTP_205_RESET_CONTENT)
            else:
                return response.Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return response.Response(s.errors, status=status.HTTP_408_REQUEST_TIMEOUT)


class UserLogoutAPIView(generics.GenericAPIView):
    """
    An endpoint to logout users.
    """

    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = tokens.RefreshToken(refresh_token)
            token.blacklist()
            return response.Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


class UserRegisterAPIView(generics.CreateAPIView):
    """
    An endpoint to register a user
    """
    
    serializer_class = [UserRegisterationSerializer]
    
    # permission_classes = []
    
    def get(self, request, *args, **kwargs):
        pass
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = tokens.RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return response.Response(data, status=status.HTTP_201_CREATED)


class UserProfileAPIView(generics.RetrieveAPIView):
    """
    An endpoint for users to see their profiles
    """
    
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = [UserProfileSerializer]
    
    def get(self, request, *args, **kwargs):
        pass
    
    def put(self, request, *args, **kwargs):
        pass
    
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.data
            return response.Response(data=data, status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response(status=status.HTTP_404_NOT_FOUND)


############################ Sale managers ############################


class SeeAllPersonnelAPIView(generics.GenericAPIView):
    """
    An endpoint for Sale managers to see the other users info
    """
    
    permission_classes = [IsSales_ManagerUser, IsManagementUser]
    serializer_class = [CustomUserSerializer]
    filter_backends = [filters.SearchFilter]
    search_fields = ['identificationCode', 'mobile', 'fullName', 'phone']
