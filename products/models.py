from django.db import models
from accounts.models import CustomUser

from categories.models import Category
from units.models import Unit

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(null= True, default="")
    size = models.IntegerField(default=0, null = False)
    price = models.FloatField(default=0)

    # relationships
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, related_name='products', on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, related_name='units', on_delete=models.CASCADE)

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.product_name


class Attributes(models.Model):
    product = models.ForeignKey(Product, related_name="product", on_delete = models.CASCADE)
    attribute = models.CharField(max_length=255,null = False)
    value = models.CharField(max_length=255,null = False)
    added_by = models.ForeignKey(CustomUser, related_name="added_by", on_delete = models.CASCADE)
    added_on = models.DateTimeField(auto_now_add = True, null = False)

    class Meta:
        db_table="product_attrs"