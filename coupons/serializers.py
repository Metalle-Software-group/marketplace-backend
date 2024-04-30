from categories.serializers import CategorySerializer
from rest_framework import serializers
from coupons.models import Coupon


class CouponSerializer(serializers.ModelSerializer):
    # owner = UserSerializer()
    category = CategorySerializer(many = False)

    class Meta:
        model = Coupon
        exclude=["owner", "added_on"]