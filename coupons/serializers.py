from categories.serializers import CategorySerializer
from rest_framework import serializers
from coupons.models import Coupon


class CouponSerializer(serializers.ModelSerializer):
    # owner = UserSerializer()
    category = CategorySerializer(many = False)

    class Meta:
        model = Coupon
        # fields = ["id", "product_name", "description", "price", "created_at", "updated_at", "owner"]
        # fields = "__all__"
        exclude=["owner", "added_on"]