from django.core.management.base import BaseCommand
from users.models import User, Project
import random


class Command(BaseCommand):
    help = 'Create projects and todos'

    def add_arguments(self, parser):
        parser.add_argument('project_count', type=int)
        parser.add_argument('todo_count', type=int)

    def handle(self, *args, **options):
        Project.objects.all().delete()
        project_count = options['project_count']
        project_list = []
        for i in range(project_count):
            project = Project.objects.create(name=f'project{i}')
            project_list.append(project)

        print(f'{project_count} projects created')

        users.objects.all().delete()
        users_count = options['users_count']
        superuser = User.objects.filter(is_superuser=True).first()
        if superuser:
            for i in range(users_count):
                project = random.choice(project_list)
                User.objects.create(project=project, text=f'text{i}' * 5, creator=superuser)

            print(f'{users_count} todos created')
        else:
            print('Error')
            print('superuser not found')
