from django.shortcuts import render
from .models import Product,Category
# Create your views here.

def home(request):
    products = Product.objects.all()
    categories = Category.objects
    context = {
        'products': products,
    }
    return render(request, 'app/home.html', context)