from django.db import models

from apps.common.models import BaseModel
from apps.task_2.choices import VacancyType


class Vacancy(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=10, choices=VacancyType.choices, default=VacancyType.FIXED)
    salary_from = models.DecimalField(max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    salary_to = models.DecimalField(max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    salary = models.DecimalField(max_digits=12, decimal_places=2, default=0, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"
