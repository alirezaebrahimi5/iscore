from django.contrib.auth import authenticate

from rest_framework import serializers, response, status

from .models import Profile, User 


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize CustomUser model.
    """

    class Meta:
        model = User
        fields = ("id", "phone", "identificationCode", "mobile", "first_name", "last_name", "address", "role")


class LoginUserSerializer(serializers.Serializer):
    identificationCode   = serializers.CharField()


class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields =['identificationCode', 'mobile', 'phone', 'first_name', 'last_name',
                 'address', 'role']
    
    def create(self, **validated_data):
        return User.objects.create_user(**validated_data)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'phone', 'first_name', 'last_name', 'role']


class UserIDSerializer(serializers.Serializer):
    identificationCode = serializers.CharField()
    
    def validate(self, data):
        if User.objects.filter(identificationCode__exact=self.identificationCode):
            return response.Response("ok", status=status.HTTP_200_OK)
        return serializers.ValidationError("!این شماره ملی ثبت نشده است")
