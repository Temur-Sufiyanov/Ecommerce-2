from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    product_price = models.FloatField()
    discount_price = models.FloatField()
    product_image = models.ImageField(upload_to='product')
    category_id = models.ManyToManyField()
    product_slug = models.SlugField()
    created = models.DateTimeField(au)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)    