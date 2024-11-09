from django.db import models
from django.utils.text import slugify
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    product_price = models.FloatField()
    discount_price = models.FloatField()
    product_image = models.ImageField(upload_to='product')
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_slug = models.SlugField(max_length=100, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def 
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
      