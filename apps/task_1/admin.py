from django.contrib import admin

from apps.task_1.models import User


class UserAdmin(admin.ModelAdmin):
    search_fields = ("username", "first_name", "last_name")
    list_display = ("id", "phone_number", "username", "first_name", "last_name", "is_deleted")
    list_display_links = (
        "id",
        "username",
    )

    fieldsets = (
        ("Personal info", {"fields": ("id", "username", "first_name", "last_name", "phone_number", "is_deleted")}),
        ("Contact info", {"fields": ("email",)}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "groups", "user_permissions")}),
        (
            "Other",
            {
                "fields": (
                    "is_active",
                    "password",
                )
            },
        ),
        ("Important dates", {"fields": ("date_joined", "last_login", "updated_at")}),
    )
    readonly_fields = (
        "id",
        "updated_at",
    )


# Register your models here.
admin.site.register(User, UserAdmin)
