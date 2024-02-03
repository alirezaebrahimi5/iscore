from rest_framework import serializers

from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instance
        fields = "__all__"


class FactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factor
        fields = "__all__"
