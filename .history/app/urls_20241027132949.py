from django.urls import path
from .views import home, category_view, productDetail

urlpatterns = [
    path('', home, name='home'),
     path('about/', home, name='home'),
      path('contact', home, name='home'),
    path('category/<slug:slug>/', category_view, name='category_view'),
    path('product-detail/<slug:product_slug>/', productDetail, name='product_detail'),
]
