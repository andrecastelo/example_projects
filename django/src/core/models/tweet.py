from django.db import models
from core.models import BaseModel, User, Tag


class Tweet(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    content = models.CharField(max_length=140, verbose_name='Content', blank=False, null=False)
    mentions = models.ManyToManyField(User, related_name='mentions')
    tags = models.ManyToManyField(Tag)
