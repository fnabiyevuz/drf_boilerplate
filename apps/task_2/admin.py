from django.contrib import admin

from apps.task_2.models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "type", "salary", "salary_from", "salary_to")
    list_display_links = ("id", "title", "type")
    date_hierarchy = "created_at"
