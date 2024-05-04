from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """Создание пользователя суперпользователя"""
    def handle(self, *args, **options):
        user = User.objects.create(
            email='keks@mail.ru',
            first_name='Kamil',
            last_name='Tutnik',
            is_superuser=False,
            is_staff=True,
            is_active=True
        )

        user.set_password('1q1a1z2w2s2x')
        user.save()
