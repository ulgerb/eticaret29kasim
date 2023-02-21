from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def Products(request):
    products = Product.objects.all()
    
    context = {
        "products": products,
    }
    return render(request, 'products.html',context)

def Detail(request):
    return render(request,'detail.html')

def Shoping(request):
    return render(request,'shoping.html')