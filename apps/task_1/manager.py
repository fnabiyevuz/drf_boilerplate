from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    # simple user
    def create_user(self, phone_number, username, first_name, password=None):
        if not phone_number:
            raise ValueError("Phone number is required")
        if not username:
            raise ValueError("Username is required")

        user = self.model(
            phone_number=phone_number,
            username=username,
            first_name=first_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # superuser
    def create_superuser(self, phone_number, first_name, username, password):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
            username=username,
            first_name=first_name,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
