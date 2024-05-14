from accounts.models import CustomUser
from django.db import models

from categories.models import Category
from units.models import Unit

# Create your models here.
class Attribute(models.Model):
    name = models.CharField(max_length=100, unique = True )

    def __str__(self):
        return self.name, self.id

    def __repr__(self):
        return self.name

    class Meta:
        db_table = "attributes"


class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    description = models.TextField(null= True, default="")
    name = models.CharField(max_length=100, null=False)
    brand = models.CharField(max_length=100, null=False)

    # relationships
    vendor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    attributes = models.ManyToManyField(AttributeValue)
    category = models.ManyToManyField(Category)
    # is_deleted = models.BooleanField(default = False)

    class Meta:
        db_table = "products"


    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def hard_delete(self):
        super().delete()

    def __str__(self):
        return self.name

class SKU(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0, null = False)
    updated_at = models.DateTimeField(auto_now=True)

    # relationships
    product = models.ForeignKey(Product, related_name = "variants", on_delete=models.CASCADE)

    class Meta:
        db_table = "skus"

    def __str__(self):
        return self.product.name


    def destock(self, quantity = 0):
        self.quantity -= quantity

    def restock(self, quantity = 0):
        self.quantity += quantity

class SKUAttribute(models.Model):
    value = models.ManyToManyField(AttributeValue, related_name="attr_values")
    sku = models.ForeignKey(SKU,related_name = "attributes", on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    # owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "sku_attributes"

    def __str__(self):
        return self.sku.product.name