from django.contrib.auth import authenticate

from rest_framework import serializers, response, status

from .models import Profile, User 


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize CustomUser model.
    """

    class Meta:
        model = User
        fields = ("pk", "phone", "identificationCode", "mobile", "first_name", "last_name",
                  "address", "profile_pic", "role")


class LoginUserSerializer(serializers.Serializer):
    identificationCode   = serializers.CharField()
    password             = serializers.CharField(required=False)


class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields =['pk', 'identificationCode', 'mobile', 'phone', 'first_name', 'last_name',
                 'address', "profile_pic", 'role']
    
    def create(self, **validated_data):
        return User.objects.create_user(**validated_data)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'phone', 'first_name', 'last_name', 'role', 'pic']


class OTPSerializer(serializers.Serializer):
    """
    Serializer class for getting OTP from Users
    """
    otp = serializers.CharField()
    phone = serializers.CharField(required=False)


class UserIDSerializer(serializers.Serializer):
    identificationCode = serializers.CharField()
    
    def validate(self, data):
        if User.objects.filter(identificationCode__exact=self.identificationCode):
            return response.Response(self.identificationCode, status=status.HTTP_200_OK)
        return serializers.ValidationError("!این شماره ملی ثبت نشده است")
