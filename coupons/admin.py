from django.contrib import admin

from coupons.models import Coupon

# Register your models here.

class CouponAdmin(admin.ModelAdmin):
    class Meta:
        model = Coupon

    list_display = ("vendor","product", "discount", "valid_from", "valid_until", "code", "max_uses", "curr_uses")

admin.site.register(Coupon, CouponAdmin)