from django.core.management.base import BaseCommand
from HW_app.models import Client


class Command(BaseCommand):
    help = "Create client."
    def handle(self, *args, **kwargs):
        client = Client(
            name='Stas', 
            email='stas@example.com',
            phone_number = 89191118899, 
            address = 'Rostov-on-Don',
            registration_date = '2023-12-01')
        client.save()
        self.stdout.write(f'{client}')