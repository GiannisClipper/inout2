from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings
from rest_framework import status


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            return None, {'status_code': status.HTTP_422_UNPROCESSABLE_ENTITY}
            #raise ValueError('Users must have an email address')

        if self.model.objects.filter(email=email):
            return None, {'status_code': status.HTTP_422_UNPROCESSABLE_ENTITY}

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()

        return user, None

    def create_superuser(self, email, password, **extra_fields):
        user, error = self.create_user(email, password, **extra_fields)
        if user:
            user.is_staff = True
            user.is_superuser = True
            user.save()

        return user, error


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return f'{self.name} ({self.email})'