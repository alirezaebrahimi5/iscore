from rest_framework import serializers

from .models import Product, Product_by_Sales_Manager


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class Product_by_Sales_ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_by_Sales_Manager
        fields = "__all__"
