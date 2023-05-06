from rest_framework import serializers

from apps.task_1.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("phone_number", "username", "first_name")


class UserRegisterWithPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("phone_number", "username", "first_name", "password")
