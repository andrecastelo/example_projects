from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django_countries.fields import CountryField
from django.contrib.auth.hashers import is_password_usable

from core.models import BaseModel


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    # My custom fields
    name = models.CharField(max_length=250, blank=False, verbose_name='Name')
    username = models.CharField(max_length=30, unique=True, verbose_name='Username')
    email = models.CharField(max_length=128, unique=True, verbose_name='Email')
    description = models.TextField(verbose_name='Description')
    website = models.CharField(max_length=128, verbose_name='Website')
    country = CountryField(blank=True)

    # Fields needed by AbstractBaseUser
    date_joined = models.DateTimeField('Date joined', default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    def save(self, *args, **kwargs):
        if not is_password_usable(self.password):
            self.set_password(self.password)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
