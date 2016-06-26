from django.db import models
from django_countries.fields import CountryField
from core.models import BaseModel

class User(BaseModel):
    full_name = models.CharField(max_length=250, blank=False, verbose_name='Full Name')
    username = models.CharField(max_length=30, unique=True, verbose_name='Username')
    password = models.CharField(max_length=128, verbose_name='Password')
    email = models.CharField(max_length=128, unique=True, verbose_name='Email')
    description = models.TextField(verbose_name='Description')
    website = models.CharField(max_length=128, verbose_name='Website')
    active = models.BooleanField(default=False, verbose_name='Active')
    country = CountryField(blank=True)
