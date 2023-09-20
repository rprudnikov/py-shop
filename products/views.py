from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'productsList': products})


def new(request):
    return HttpResponse('Hello New')
