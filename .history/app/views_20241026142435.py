from django.shortcuts import render, get_object_or_404
from .models import Product,Category
# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'app/home.html', context)

def category_view(request,slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category_id=category)
    context = {
        'Camera, Photos, and Video · 8-megapixel iSight camera · Panorama · Video recording, HD (1080p) up to 30 frames per second with audio ·'
    }