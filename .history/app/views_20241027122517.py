from django.shortcuts import render, get_object_or_404, redirect
from .models import Product,Category
from .forms import RatingForm
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


def productDetail(request, product_slug):
    product = get_object_or_404(Product, product_slug=product_slug)
    
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = int(form.changed_data['rating'])
            product.total_rating += rating
            product.rating_count += 1
            product.save()
            return redirect('product_detail', product_slug = product.product_slug)
    els    
    context = {
        'product':product,
    }
    return render(request, 'app/product_detail.html', context)