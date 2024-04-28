from django.db import models

from accounts.models import CustomUser
from coupons.models import Coupon

# Create your models here.
class Orders(models.Model):
    order_date = models.DateField(auto_now_add = True, null = False)

    # relationship
    customer = models.ForeignKey(CustomUser, related_name = "orders", on_delete = models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length = 255, null = False)

    class Meta:
        db_table = "orders"


class OrderItem(models.Model):
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    # relationships
    product = models.ForeignKey("products.Product", related_name = "order_items", on_delete = models.CASCADE)
    coupon = models.ForeignKey(Coupon, related_name = "order_items", on_delete = models.CASCADE, null = True)
    order = models.ForeignKey(Orders, related_name = "order_items", on_delete = models.CASCADE)

    def __str__(self):
        return str(self.order)

    def __repr__(self):
        return str(self.order)

    class Meta:
        db_table = "order_items"
