from django.contrib.auth.hashers import make_password
from rest_framework import generics, status
from rest_framework.response import Response

from apps.task_1.models import User

from .serializers import UserRegisterWithPassSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterWithPassSerializer
    queryset = User.objects.all()

    """
        Create a model instance.
    """

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        request.data["password"] = make_password(request.data["password"])
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


__all__ = ("UserRegisterAPIView",)
