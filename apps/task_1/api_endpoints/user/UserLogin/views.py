from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.task_1.models import User

from .serializers import UserLoginSerializer, UserLoginWithoutPassSerializer


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    queryset = User.objects.all()

    @swagger_auto_schema(request_body=UserLoginSerializer)
    def post(self, request, format=None):
        phone_number = request.data["phone_number"]
        password = request.data["password"]
        user = authenticate(phone_number=phone_number, password=password)
        print(user)
        if (user is not None) and user.is_deleted == False:
            serializer = UserLoginWithoutPassSerializer(user)
            return Response(serializer.data)
        return Response({"error": f"{user} not found"})


__all__ = ("UserLoginAPIView",)
