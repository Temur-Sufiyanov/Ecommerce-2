from django.shortcuts import render
from .models import Product
# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {
        'product':
    }
    return render(request, 'app/home.html')