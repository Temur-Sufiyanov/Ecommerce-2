from django.contrib import admin
from .models import Product, Category
# Register your models here.

admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    dis
admin.site.register(Category)