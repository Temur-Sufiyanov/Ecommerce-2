from django.shortcuts import render, get_object_or_404, redirect
from .models import Product,Category, Customer
from .forms import RatingForm, ClientMessageForm, CustomRegistrationForm, CustomLoginForm, CustomPasswordResetForm, CustomPasswordResetConfirmForm, CustomerForm
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
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
    paginator = Paginator(products, 8)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj':page_obj,
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

def search_bar(request):
    search_bar = request.GET.get('search', '')
    products = Product.objects.filter(Q(name__icontains=search_bar))
    
    return render(request, 'app/search.html', {{'search':search_bar}})

def customRegister(request):
    
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    else:
        form = CustomRegistrationForm()    
    context = {
        'form':form,
    }
    return render(request, 'app/registration/customRegister.html', context)

def terms(request):
    
    return render(request, 'app/terms_and_conditions.html')

def customLogin(request):
    
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print('User is not found')
    else:
        form = CustomLoginForm()
    context = {
        'form': form,
    }
    return render(request,'app/registration/login.html', context)

def customLogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'app/registration/logout.html')
    
    
class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'app/registration/password_reset_form.html'
    
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomPasswordResetConfirmForm
    template_name = 'app/registration/password_reset_confirm.html'
    
def profile_view(request):
    
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        customer = None
    
    if request.method == 'POST':
        if 'edit':
            form = CustomerForm(request.POST, instance=customer)
            if form.is_valid():
                form.save()
                return  redirect('profile')
        elif 'add':
            form = 

    return render(request, 'app/profile.html', {'form':form, 'customer': customer, })
