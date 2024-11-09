from django.shortcuts import render
from .models import Product,Category
# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'categories':categories,
    }
    return render(request, 'app/home.html', context)