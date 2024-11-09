from django.urls import path
from .views import home, category_view, productDetail, about, contact, all_products,search_bar, customRegister, terms, customLogin, customLogout
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('all-products/', all_products, name='all_products'),
    path('search/',search_bar, name='search'),
    path('category/<slug:slug>/', category_view, name='category_view'),
    path('product-detail/<slug:product_slug>/', productDetail, name='product_detail'),
    
    path('registration/', customRegister, name='register'),
    path('login/', customLogin, name='login'),
    path('logout/', customLogout, name='logout'),
    path('terms/', terms, name='conditions'),
    path('password-reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset'),
    path(),
    path(),
]
