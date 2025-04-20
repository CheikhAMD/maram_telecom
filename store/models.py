from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name

from django.db import models
from .models import Product

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    customer_address = models.TextField()
    payment_method = models.CharField(max_length=50, blank=True)
    delivery_method = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"طلب {self.customer_name} - {self.product.name}"
