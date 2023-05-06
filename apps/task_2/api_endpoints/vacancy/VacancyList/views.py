from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from apps.task_2.filters import VacancyFilter
from apps.task_2.models import Vacancy

from .serializers import VacancySerializer


class VacancyListAPIView(generics.ListAPIView):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = VacancyFilter
    # filterset_fields = ['salary']
    # search_fields = (
    #     'salary',
    # )


__all__ = ("VacancyListAPIView",)
