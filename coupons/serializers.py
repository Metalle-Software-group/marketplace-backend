from accounts.serializers import VendorSerializer
from products.serializers import ProductSerializer
from rest_framework import serializers
from products.models import Product
from accounts.models import Vendor
from coupons.models import Coupon


class CouponSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(many=False)
    product = ProductSerializer(many=False)

    class Meta:
        model = Coupon
        fields = ["vendor", "product", "discount", "valid_from", "valid_until",
                  "code", "max_uses", "id", "curr_uses", "is_authorized"]


class CouponCreateSerializer(serializers.ModelSerializer):
    vendor = serializers.PrimaryKeyRelatedField(
        queryset=Vendor.objects.all(),
        many=False
    )

    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        many=False
    )

    class Meta:
        model = Coupon
        fields = ["vendor", "product", "discount", "valid_from",
                  "valid_until", "code", "max_uses", "id", "curr_uses"]
