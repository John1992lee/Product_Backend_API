from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    inventory_quantity = models.IntegerField
    price = models.DecimalField(max_digits=8, decimal_places=2)