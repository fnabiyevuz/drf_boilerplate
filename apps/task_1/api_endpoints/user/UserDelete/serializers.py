from rest_framework import serializers

from apps.task_1.models import User


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("phone_number", "username", "first_name")
