from django.db import models
from accounts.models import CustomUser

from products.models import Product

# Create your models here.
class Coupon(models.Model):
    discount = models.DecimalField(max_length = 10,null = False,decimal_places = 0, max_digits=3)
    valid_from = models.DateTimeField(auto_now_add = True, null = False)
    valid_until = models.DateTimeField(auto_now_add = True, null = False)
    added_on = models.DateTimeField(auto_now_add = True, null = False)
    code = models.CharField(max_length = 255,null = False)
    max_uses = models.IntegerField(null = False)
    curr_uses = models.IntegerField(null = False)

    # relationships
    vendor = models.ForeignKey(CustomUser, related_name="coupon_vendor", on_delete = models.CASCADE)
    product = models.ForeignKey(Product, related_name="coupon", on_delete = models.CASCADE)



    class Meta:
        db_table = "coupons"