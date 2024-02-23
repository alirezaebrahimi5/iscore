from datetime import datetime

from django.conf import settings
from django.utils import timezone

from rest_framework import permissions, response, status, generics, filters
from rest_framework_simplejwt import tokens
from django.shortcuts import get_object_or_404
from .models import User, OTP
from .permissions import *
from .serializers import *
from .utils import *
from .tasks import deleteOTP

OTP_SECRET = settings.OTP_SECRET_KEY


####################### TODO : Authentication section #######################


class UserLoginAPIView(generics.GenericAPIView):
    """
    An endpoint to login users.
    """
    
    permission_classes = (permissions.AllowAny,)
    serializer_class = [LoginUserSerializer]

    def post(self, request, *args, **kwargs):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            nid = serializer.validated_data["nid"]
            user = get_object_or_404(User, nid=nid)
            result = sendToken(user=user)
            otp = result['otp']
            error = result['error']
            if otp:
                print(f"The OTP is : {otp}")
                return response.Response({"mobile": user.mobile[-4:]}, status=status.HTTP_200_OK)
            else:
                return response.Response({"waite": error}, status=status.HTTP_429_TOO_MANY_REQUESTS)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckOTPAPIView(generics.GenericAPIView):
    """
    An endpoint for users to send their OTP tokens
    """
    
    def post(self, request, *args, **kwargs):
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            otp = serializer.validated_data["otp"]
            nid = serializer.validated_data["nid"]
            # TODO : `uo` is stands for User OTP
            uo = get_object_or_404(OTP, user__nid=nid)
            counter = uo.counter
            if uo.otp == otp and counter > 0:
                access_time = (datetime.timedelta(minutes=10) + otp.created_at).timestamp()
                delta_time = access_time - timezone.now().timestamp()
                if delta_time > 0:
                    user = uo.user
                    token = tokens.RefreshToken.for_user(user)
                    data = {"refresh": str(token), "access": str(token.access_token)}
                    uo.delete()
                    return response.Response(data, status=status.HTTP_205_RESET_CONTENT)
                else:
                    uo.delete()
            else:
                if counter < 0:
                    uo.delete()
                else:
                    uo.counter -= 1
                    uo.save()
            return response.Response({'error': "Token has been expired"}, status=status.HTTP_408_REQUEST_TIMEOUT)
        else:
            return response.Response(serializer.errors, status=status.HTTP_408_REQUEST_TIMEOUT)


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


####################### TODO : Registration section #######################


class UserRegisterAPIView(generics.CreateAPIView):
    """
    An endpoint to register a user
    """
    
    serializer_class = [UserRegisterationSerializer]
    
    # permission_classes = []
    
    def get(self, request, *args, **kwargs):
        pass
    
    def post(self, request, *args, **kwargs):
        s = UserRegisterationSerializer(data=request.data)
        if s.is_valid():
            s.save()
            otp = sendToken(user=s.data)
            user = User.objects.get(phone=s.validated_data["phone"])
            OTP.objects.create(user=user, otp=otp).save()
            return response.Response(data=s.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(data=s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class ActivateAccountAPIView(generics.GenericAPIView):
    """
    An endpoint to activate their account via OTP 
    """
    permission_classes = []
    serializer_class = [OTPSerializer]
    
    def post(self, request, *args, **kwargs):
        deleteOTP(request.user)
        s = OTPSerializer(data=request.data)
        if s.is_valid():
            otp = s.validated_data["otp"]
            if OTP.objects.get(otp=otp):
                # TODO : `uo` is stand for User OTP
                uo = OTP.objects.get(otp=otp)
                user = User.objects.get(phone=uo)
                token = tokens.RefreshToken.for_user(user)
                # TODO : Activating the User
                user.is_active = True
                user.save()
                data = s.data
                data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}                
                uo.delete()
                return response.Response(data, status=status.HTTP_205_RESET_CONTENT)
            else:
                return response.Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return response.Response(s.errors, status=status.HTTP_408_REQUEST_TIMEOUT)


####################### TODO : Password Reset section #######################


class GetUserIDNAPIView(generics.GenericAPIView):
    """
    An endpoint to get User identification code
    """
    permission_classes = []
    serializer_class = [UserIDSerializer]
    
    def get(self, request, *args, **kwargs):
        return response.Response()
    
    def post(self, request, *args, **kwargs):
        s = UserIDSerializer(data=request.data)
        if s.is_valid():
            idn = s.validated_data["nid"]
            user = User.objects.get(nid=idn)
            if user is not None:
                otp = sendToken(user=user)
                OTP.objects.create(user=user,otp=otp).save()
                return response.Response(data=s.data, status=status.HTTP_200_OK)
            else:
                return response.Response(data="User does not exists!", status=status.HTTP_404_NOT_FOUND)
        else:
            return response.Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPAPIView(generics.GenericAPIView):
    """
    An endpoint to make sure users OTP for reset password
    """    
    permission_classes = []
    serializer_class = [OTPSerializer]
    
    def get(self, request, *args, **kwargs):
        return response.Response()
    
    def post(self, request, *args, **kwargs):
        s = OTPSerializer(data=request.data)
        if s.is_valid():
            otp = s.validated_data["otp"]
            if OTP.objects.get(otp=otp):
                user_otp = OTP.objects.get(otp=otp)
                user_otp.delete()
                return response.Response(data=s.data, status=status.HTTP_200_OK)
            else:
                return response.Response("OTP has been expired or used before", status=status.HTTP_408_REQUEST_TIMEOUT)
        else:
            return response.Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)

#
# class ResetPasswordConfirmAPIView(generics.GenericAPIView):
#     """
#     An endpoint for Users to reset their password
#     """
#     permission_classes = []
#     serializer_class = [ResetPassowrdSerializer]
#
#     def get(self, request, *args, **kwargs):
#         return response.Response()
#
#     def post(self, request, *args, **kwargs):
#         s = ResetPassowrdSerializer(data=request.data)
#         return response.Response()


############################ TODO : Sale managers ############################


# class SeeAllPersonnelAPIView(generics.GenericAPIView):
#     """
#     An endpoint for Sale managers to see the other users info
#     """
#
#     permission_classes = [IsSales_ManagerUser, IsManagementUser]
#     serializer_class = [CustomUserSerializer]
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['nid', 'mobile', 'fullName', 'phone']
