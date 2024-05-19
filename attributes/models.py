from django.db import models
from products.models import Product

from variants.models import Variant

# Create your models here.


class Attribute(models.Model):
    name = models.CharField(max_length=100, unique=True)

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


class SKUAttribute(models.Model):
    sku = models.ForeignKey(
        Variant, related_name="attr", on_delete=models.CASCADE)
    value = models.ManyToManyField(AttributeValue, related_name="sku_values")
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    # owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "sku_attr"

    def __str__(self):
        return self.sku.product.name


class ProductAttribute(models.Model):
    product = models.ForeignKey(
        Product, related_name="attr", on_delete=models.CASCADE)
    value = models.ManyToManyField(
        AttributeValue, related_name="product_values")
    attr = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    # owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "product_attr"

    def __str__(self):
        return self.sku.product.name
