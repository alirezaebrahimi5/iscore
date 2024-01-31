from rest_framework import serializers

from .models import UserTime, UserGivenScore, Score


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score 
        fields = "__all__"


class UserTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTime
        fields = "__all__"


class UserGivenScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGivenScore
        fields = "__all__"
