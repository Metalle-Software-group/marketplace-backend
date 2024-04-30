from django.db import models
from accounts.models import CustomUser

from products.models import Product
from units.models import Unit

# Create your models here.
class InventoryItem(models.Model):
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0, null = False)
    updated_at = models.DateTimeField(auto_now=True)

    # relationships
    vendor = models.ForeignKey(CustomUser, related_name = "inventory", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name = "inventory", on_delete=models.CASCADE)
    units = models.ForeignKey(Unit,related_name = "inventory", on_delete = models.CASCADE)

    def __str__(self):
        return self.product.name

    def __repr__(self):
        return self.product.name