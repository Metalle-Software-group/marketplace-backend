from django.db import models

from products.models import Product

# Create your models here.


class Variant(models.Model):
    sku = models.CharField(max_length=255, null=True, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=0, null=False)

    # relationships
    product = models.ForeignKey(
        Product, related_name="variants", on_delete=models.CASCADE)

    class Meta:
        db_table = "variants"

    def __str__(self):
        return self.product.name

    def destock(self, quantity=0):
        self.quantity -= quantity

    def restock(self, quantity=0):
        self.quantity += quantity
