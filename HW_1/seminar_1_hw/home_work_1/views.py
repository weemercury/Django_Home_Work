from django.shortcuts import render
from django.http import HttpResponse
import logging


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


@log
def about(request):
    return HttpResponse("<h1>Hello! My name is George. I am learning Python in GeekBrains school.</h1>")