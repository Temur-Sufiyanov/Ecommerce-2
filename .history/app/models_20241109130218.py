from django.db import models
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    product_price = models.FloatField()
    discount_price = models.FloatField()
    product_image = models.ImageField(upload_to='product')
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='product')
    product_slug = models.SlugField(max_length=100, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    total_rating = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)
    
    @property
    def average_rating(self):
        if self.rating_count > 0:
            return round(self.total_rating/self.rating_count, 1)
        return 0

    @property
    def discounted_price(self):
        if self.product_price > 0:
            return round(self.product_price * (1-self.discount_price/100),2)
        return round(self.product_price, 2)
    

    def save(self, *args, **kwargs):
        if not self.product_slug:
            self.product_slug = slugify(self.name)
        super(Product,self).save(*args, **kwargs)    
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=20, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category,self).save(*args, **kwargs)    
        
    def __str__(self):
        return self.name
      
      
class ClientMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    phone_number = PhoneNumberField(region='KR', blank=True)
    message = models.TextField(blank=True)
    
    
    def __str__(self):
        return self.name      
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f' Cart ({self.user.username})'

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity =models.PositiveBigIntegerField(default=1)
    
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    
    @property
    def total_price(self):
        return self.quantity * self.product.discounted_price
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('S', 'Shipped'),
        ('D', 'Delivered'),
        ('C', 'Canceled'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'Order {self.id} by {self.customer.name}'
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.quantity} x {self.product.name} for Order'