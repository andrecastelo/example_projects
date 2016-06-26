# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from core.models import User
from core.factories import UserFactory

class Command(BaseCommand):
    help = "Seeds the user table"

    def handle(self, *args, **options):
        self._seed_users()

    def _seed_users():
        User.objects.all().delete()
        UserFactory(
            full_name="André Castelo",
            email="andrecastelo@email.com",
            username="andrecastelo",
            password="123456",
            description="Developer of this app",
            website="andrecastelo.github.io",
            active=True,
            country="BR"
        )
        for i in range(30):
            UserFactory()
