from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from HW_app.models import Order, Client, Product
from django.utils import lorem_ipsum
from random import choice, choices
        

class Command(BaseCommand):
    help = 'Create order.'
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('goods_amount', type=int)

        
    def handle(self, *args, **kwargs):
        goods_amount = kwargs['goods_amount']
        clients = Client.objects.all()
        products = Product.objects.all()
        
        order = Order.objects.create( 
            clients = choice(clients),
            date_ordered='2024-03-01',
            total_price=0,
        )
        
        for i in range(goods_amount):
            goods = choice(products)
            order.products.add(goods)
            order.total_price += goods.price
            
        order.save()
        self.stdout.write(f'Order: {order}')