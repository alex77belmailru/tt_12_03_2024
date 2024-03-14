from django.core.management import BaseCommand

from api.models import User


class Command(BaseCommand):
    """
    Класс - команда для создания суперпользователя
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@mail.ru',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        user.set_password('123')

        user.save()
