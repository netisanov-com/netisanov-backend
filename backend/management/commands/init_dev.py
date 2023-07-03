from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Initialize development environment'

    def handle(self, *args, **options):
        print("init_dev")