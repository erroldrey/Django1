from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from rest_framework.authtoken.models import Token
from users.models import User


class Command(BaseCommand):
    help = 'Create Tokens for all users'

    def handle(self, *args, **options):
        # Удаляем все пользоватлелей
        users = User.objects.all()

        for item in users:
            token, id_created = Token.objects.get_or_create(user=item)
            print(item.username, token.key, f'created {id_created}')
        print('done')
