from django.shortcuts import render
from django.http import HttpResponse
import logging
from HW_app.models import Client, Product, Order
from datetime import datetime, timedelta
from django.utils import timezone


logger = logging.getLogger(__name__)

def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'Run function "{func.__name__}"')
        return result
    return wrapper


# Create your views here.
@log
def main(request):
    return HttpResponse("<h1>Hello World! It's my first Django App.</h1>")


# HW_3 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@log 
def get_order(request, client_id):
    days = 365
    days = 30
    days = 7
    client = Client.objects.get(pk=client_id)
    last_days = timezone.now() - timedelta(days=days)
    resent_orders = Product.objects.filter(order__date_ordered__gte=last_days, order__clients=client).distinct()
    orders = resent_orders.order_by('add_date')

    return render(request, 'HW_app/order.html', {'orders': orders, 'time':days})