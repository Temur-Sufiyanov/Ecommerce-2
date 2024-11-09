from django.shortcuts import render
from .models import Product
# Create your views here.

def home(request):
    products = Product.objects.all()
    cate
    context = {
        'products': products,
    }
    return render(request, 'app/home.html', context)