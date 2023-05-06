from rest_framework import serializers

from apps.task_1.models import User


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("phone_number", "password")


class UserLoginWithoutPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("phone_number",)
