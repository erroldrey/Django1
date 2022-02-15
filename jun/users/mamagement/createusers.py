from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'Create Superuser and some test users'

    def add_arguments(self, parser):
        parser.add_argument('user_count', type=int)

    def handle(self, *args, **options):
        # Удаляем все пользоватлелей
        User.objects.all().delete()
        user_count = options['user_count']
        # Создаем суперпользователя
        User.objects.create_superuser('err', 'err@test.com', 'den12345678')
        # Создаем тестовых пользователей
        for i in range(user_count):
            User.objects.create_user(f'user{i}', f'user{i}@test.com', 'den12345678')

        print('done')
