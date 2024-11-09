from django.shortcuts import render, get_object_or_404, redirect
from .models import Product,Category
from .forms import RatingForm, ClientMessageForm
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'app/home.html', context)


def about(request):
    return render(request, 'app/about.html')


def contact(request):
    
    if request.method == 'POST':
        form = ClientMessageForm(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ClientMessageForm()    
    context = {
        'form':form
    }
    return render(request, 'app/contact.html', context)

def all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products':products,
    }
    return render(request, 'app/all_products.html', context)


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
            rating = int(form.cleaned_data['rating'])
            product.total_rating += rating
            product.rating_count += 1
            product.save()
            return redirect('product_detail', product_slug = product.product_slug)
    else:
        form = RatingForm()
            
    context = {
        'product':product,
        'form':form,
    }
    return render(request, 'app/product_detail.html', context)