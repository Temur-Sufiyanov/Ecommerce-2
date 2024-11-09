from django.contrib import admin
from .models import Product, Category
# Register your models here.

@(Product)
class ProductAdmin(admin.ModelAdmin):
    display = ['product_slug', 'name', 'product_price', 'discount_price', 'category_id', 'created' ]
admin.site.register(Category)