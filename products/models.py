from email.policy import default
from django.db import models
from accounts.models import CustomUser

from categories.models import Category
from units.models import Unit


class Attributes(models.Model):
    added_on = models.DateTimeField(auto_now_add = True, null = False)
    attribute = models.CharField(max_length=255,null = False)
    value = models.CharField(max_length=255,null = False)

    # relations
    added_by = models.ForeignKey(CustomUser, related_name="added_by", on_delete = models.CASCADE)

    class Meta:
        db_table="product_attrs"
        unique_together = ("attribute", "value")


# Create your models here.
class Product(models.Model):
    # posted_on = models.DateTimeField(auto_now_add = True, null = False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(null= True, default="")
    name = models.CharField(max_length=100, null=False)
    size = models.IntegerField(default=0, null = False)

    # relationships
    attributes = models.ManyToManyField(Attributes, related_name="product_attributes")
    vendor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name