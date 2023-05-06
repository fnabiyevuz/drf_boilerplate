from rest_framework import generics

from apps.task_1.models import User

from .serializers import UserDeleteSerializer


class UserDeleteAPIView(generics.DestroyAPIView):
    serializer_class = UserDeleteSerializer
    queryset = User.objects.all()


__all__ = ("UserDeleteAPIView",)
