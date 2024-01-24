from rest_framework import serializers

from .models import DefineTask, VisitorTask, TaskDone


class DefineTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefineTask
        fields = "__all__"


class VisitorTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorTask
        fields = "__all__"
