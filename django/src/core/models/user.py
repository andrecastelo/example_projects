from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django_countries.fields import CountryField
from django.contrib.auth.hashers import is_password_usable, check_password

from core.models import BaseModel


class User(AbstractBaseUser, BaseModel):
    name = models.CharField(max_length=250, blank=False, verbose_name='Name')
    username = models.CharField(max_length=30, unique=True, verbose_name='Username')
    email = models.CharField(max_length=128, unique=True, verbose_name='Email')
    description = models.TextField(verbose_name='Description')
    website = models.CharField(max_length=128, verbose_name='Website')
    active = models.BooleanField(default=False, verbose_name='Active')
    country = CountryField(blank=True)

    USERNAME_FIELD = 'username'

    def save(self, *args, **kwargs):
        if not is_password_usable(self.password):
            self.set_password(self.password)

        super().save(*args, **kwargs)

