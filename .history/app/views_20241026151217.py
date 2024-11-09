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
    products = category.product.all()
    context = {
        'category':category,
        'products':products,
        'total_products':products.count(),
    }
    
    return render(request, 'app/category.html', context)


def productDetail(request, slug):
    product = get_object_or_404()
    context = {
        'product':product,
    }
    return render(request, 'app/product_detail.html', context)