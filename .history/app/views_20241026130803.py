from django.shortcuts import render
from .models import Product
# Create your views here.

def home(request):
    product = Product.objects.all()
    context = {
        'product'
    }
    return render(request, 'app/home.html')