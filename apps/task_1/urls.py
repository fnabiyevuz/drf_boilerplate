from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from apps.task_1.api_endpoints.user import (UserDeleteAPIView,
                                            UserLoginAPIView,
                                            UserRegisterAPIView)

app_name = "task_1"

urlpatterns = [
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    # user
    path("register/", UserRegisterAPIView.as_view(), name="user-register"),
    path("login/", UserLoginAPIView.as_view(), name="user-login"),
    path("<int:pk>/delete/", UserDeleteAPIView.as_view(), name="user-delete"),
]
