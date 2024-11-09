from django.contrib import admin
from .models import Product, Category
# Register your models here.

admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    display = ['product_slug', 'name', 'product_price', ]
admin.site.register(Category)