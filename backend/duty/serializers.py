from rest_framework import serializers

from .models import VisitorTask, VisitorTaskDone


class VisitorTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorTask
        fields = "__all__"


class TaskDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorTaskDone
        fields = "__all__"
