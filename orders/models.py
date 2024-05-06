from enum import Enum
from django.db import models

from accounts.models import CustomUser
from coupons.models import Coupon
from products.models import Product

# Create your models here.

class ORDER_STATUS(Enum):
    PENDING = "pending payment"
    PROCESSING = "processing"
    DELIVERED = "delivered"


STATUS_CHOICES = [(member.value, member.name) for member in ORDER_STATUS]
class Orders(models.Model):
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default = 0)
    order_date = models.DateField(auto_now_add = True, null = False)

    status = models.CharField(
        default = ORDER_STATUS.PENDING.value,
        choices = STATUS_CHOICES,
        max_length = 100
        )

    # relationship
    customer = models.ForeignKey(CustomUser, related_name = "orders", on_delete = models.CASCADE)

    class Meta:
        db_table = "orders"

class OrderItem(models.Model):
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0, null = False)

    # relationships
    coupon = models.ForeignKey(Coupon, related_name = "order_item", on_delete = models.CASCADE, null = True)
    order = models.ForeignKey(Orders, related_name = "order_items", on_delete = models.CASCADE, null = False)
    product = models.ForeignKey(Product, related_name = "orders", on_delete = models.CASCADE, null = False)

    def __str__(self):
        return str(self.product)

    def __repr__(self):
        return str(self.product)

    class Meta:
        db_table = "order_items"



class Cart(models.Model):
    customer = models.ForeignKey(CustomUser, related_name = "cart", on_delete = models.CASCADE)
    # order_items = models.ManyToManyField(OrderItem)

    class Meta:
        db_table = 'cart'