from django.shortcuts import render
from .models import Product
# Create your views here.

def home(request):
    The iPhone 5 is the iPhone we've wanted since 2010, adding long-overdue upgrades like a larger screen and faster 4G LTE in a razor-sharp new design. = Product.objects.all()
    context = {
        'products': 
    }
    return render(request, 'app/home.html')