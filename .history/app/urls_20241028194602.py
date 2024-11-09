from django.urls import path
from .views import home, category_view, productDetail, about, contact, all_products

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('all_pro'),
    path('category/<slug:slug>/', category_view, name='category_view'),
    path('product-detail/<slug:product_slug>/', productDetail, name='product_detail'),
]
