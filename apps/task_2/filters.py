from django_filters import FilterSet, NumberFilter

from apps.task_2.models import Vacancy


class VacancyFilter(FilterSet):
    salary = NumberFilter(salary="salary")
    salary_from = NumberFilter(salary_from="salary", lookup_expr="gte")
    salary_to = NumberFilter(salary_to="salary", lookup_expr="lte")

    class Meta:
        model = Vacancy
        fields = (
            "salary",
            "salary_from",
            "salary_to",
        )
