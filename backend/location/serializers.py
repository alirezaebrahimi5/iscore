from rest_framework_mongoengine import serializers

from .models import UserLocation, NewLocation


class LocationSerializer(serializers.DocumentSerializer):
    class Meta:
        model = UserLocation
        fields = '__all__'
        # exclude = ('created_at',)


class NewLocationSerializer(serializers.DocumentSerializer):
    class Meta:
        model = NewLocation
        fields = "__all__"
        # exclude = ('user',)
