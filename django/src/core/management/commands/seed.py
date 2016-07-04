# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.hashers import make_password

from core.models import User
from core.factories import UserFactory

class Command(BaseCommand):
    help = "Seeds the user table"

    def handle(self, *args, **options):
        self._seed_users()

    def _seed_users(self):
        self.stdout.write('Seeding users.')
        User.objects.all().delete()
        default_password = make_password('123456')
        UserFactory(
            name="André Castelo",
            email="andrecastelo@email.com",
            username="andrecastelo",
            password=default_password,
            description="Developer of this app",
            website="http://andrecastelo.github.io",
            is_active=True,
            country="BR"
        )

        for i in range(30):
            self.stdout.write('.', ending='')
            UserFactory(password=default_password)

        self.stdout.write('')
