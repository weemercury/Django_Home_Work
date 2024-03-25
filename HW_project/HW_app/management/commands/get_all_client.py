from django.core.management.base import BaseCommand
from HW_app.models import Client


class Command(BaseCommand):
    help = "Get all clients."
    def handle(self, *args, **kwargs):
        users = Client.objects.all()
        self.stdout.write(f'{users}')