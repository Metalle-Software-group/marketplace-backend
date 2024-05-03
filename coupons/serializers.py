from accounts.models import CustomUser
from accounts.serializers import VendorSerializer
from categories.serializers import CategorySerializer
from rest_framework import serializers
from coupons.models import Coupon
from marketplace.roles import VENDOR_ROLE
from products.models import Product
from products.serializers import ProductSerializer


class CouponSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(many = False)
    product = ProductSerializer(many = False)
    class Meta:
        model = Coupon
        exclude=["added_on"]


class CouponCreateSerializer(serializers.ModelSerializer):
    vendor = serializers.PrimaryKeyRelatedField(
        queryset = CustomUser.objects.filter(
            vendor__isnull = False,
              groups__name = VENDOR_ROLE
              ),
              many = False
              )
    product = serializers.PrimaryKeyRelatedField(
        queryset = Product.objects.all(),
        many = False
    )

    class Meta:
        model = Coupon
        fields = ["vendor","product", "discount", "valid_from", "valid_until", "code", "max_uses"]