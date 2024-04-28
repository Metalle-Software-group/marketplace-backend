from rest_framework import serializers
from coupons.serializers import CouponSerializer

from orders.models import OrderItem, Orders
from products.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer(many = False)

    coupon = CouponSerializer(many = False)

    class Meta:
        model = OrderItem
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):

    order_items = OrderItemSerializer(many = True)

    class Meta:
        model = Orders
        fields = "__all__"
