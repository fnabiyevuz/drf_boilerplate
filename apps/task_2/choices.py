from django.db import models


class VacancyType(models.TextChoices):
    FIXED = "fixed", "Fixed"
    RANGE = "range", "Range"
