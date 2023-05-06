from django.urls import path

from apps.task_2.api_endpoints.vacancy import VacancyListAPIView

app_name = "task_2"

urlpatterns = [
    path("list/", VacancyListAPIView.as_view(), name="vacancy-list"),
]
