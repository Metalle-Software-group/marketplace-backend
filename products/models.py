from accounts.models import CustomUser
from django.db import models

from categories.models import Category
from units.models import Unit

# Create your models here.


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    description = models.TextField(null=True, default="")
    name = models.CharField(max_length=100, null=False)
    brand = models.CharField(max_length=100, null=False)

    # relationships
    vendor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "products"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def hard_delete(self):
        super().delete()

    def __str__(self):
        return self.name
