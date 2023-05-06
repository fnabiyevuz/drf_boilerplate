from django.urls import include, path

urlpatterns = [
    path("task_1/", include("apps.task_1.urls")),
    path("task_2/", include("apps.task_2.urls")),
]
