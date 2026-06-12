from rest_framework import serializers
from datetime import date

from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    days_left = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'deadline',
            'days_left'
        ]

    def get_days_left(self, obj):
        return (obj.deadline - date.today()).days