from django.core.management import BaseCommand
from HW_app.models import Product
from django.utils import lorem_ipsum


class Command(BaseCommand):
    help = 'Create product.'
    
    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        
    def handle(self, *args, **kwargs):
        name = kwargs["name"]
        description = lorem_ipsum.paragraphs(2, common=False)
        product = Product.objects.create(
            name=name, 
            description=description, 
            price=899.99, 
            quantity_of_products=9,
            add_date='2023-12-01',
            )
        self.stdout.write(f'{product}')