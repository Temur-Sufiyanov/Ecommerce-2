from django.contrib import admin
from .models import Product, Category,ClientMessage
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_slug', 'name', 'product_price', 'discount_price', 'category_id', 'created' ]

admin.site.register(Category)

@admin.register
class ClientMessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone_number', 'message']

