from django.shortcuts import render
from .models import Product,Category
# Create your views here.

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories'
    }
    return render(request, 'app/home.html', context)