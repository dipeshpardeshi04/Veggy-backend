from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Products(models.Model):
    prod_name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='images/', null=True, blank=True)  # Image field

    def __str__(self):
        return self.prod_name
    

class Student(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length=255)
    # address = models.CharField(max_length = 255)
    
   
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100, unique=True)
#     password = models.CharField(max_length=100)   

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}'s Cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product} (x{self.quantity})"

