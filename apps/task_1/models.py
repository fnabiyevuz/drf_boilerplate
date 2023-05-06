from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken
from sorl.thumbnail.fields import ImageField

from apps.task_1.manager import UserManager


# Create your models here.
class User(AbstractUser):
    username = models.CharField(_("username"), max_length=150, null=True, blank=True)
    avatar = ImageField(null=True, blank=True, upload_to="images/profile_pics/%Y/%m/%d/")
    phone_number = PhoneNumberField(region="UZ", verbose_name=_("phone number"), unique=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["username", "first_name"]

    objects = UserManager()

    def __str__(self):
        return str(self.phone_number)

    def get_tokens(self):
        refresh = RefreshToken.for_user(self)

        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return tokens

    def delete(self):
        """Mark the record as deleted instead of deleting it"""
        self.is_deleted = True
        self.username = f"{self.phone_number}|{self.username}"
        self.phone_number = None
        self.save()
