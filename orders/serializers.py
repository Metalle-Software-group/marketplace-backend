from accounts.models import CustomUser
from accounts.serializers import UserSerializer
from products.models import Product
from products.serializers import ProductSerializer
from coupons.serializers import CouponSerializer
from orders.models import OrderItem, Orders
from rest_framework import serializers
from django.db import transaction

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many = False)
    coupon = CouponSerializer(many = False)

    class Meta:
        model = OrderItem
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only = True, many = False)
    order_items = OrderItemSerializer(many = True)

    class Meta:
        model = Orders
        fields = "__all__"

class OrderItemCreateSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset = Orders.objects.all(), write_only =True, required = False)
    product = serializers.PrimaryKeyRelatedField(queryset = Product.objects.all())

    def create(self, validated_data):
        price = validated_data.get("product",1).price
        discounted_price = price * 90/100

        validated_data.update({
            "total_cost": discounted_price * validated_data.get("quantity"),
            "discounted_price": discounted_price,
            "price": price,
        })

        return super().create(validated_data)

    class Meta:
        model = OrderItem
        fields = ["quantity","product","order"]

class OrderCreateSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
    order_items = OrderItemCreateSerializer(many = True)

    def create(self, validated_data):
        items = validated_data.pop('order_items', [])

        with transaction.atomic():
            order = super().create(
                validated_data = validated_data
            )

            total_cost = 0

            for order_item in items:
                order_item_instance = OrderItemCreateSerializer(
                    data = {
                        **order_item,
                            "product": order_item.get("product").id,
                            "order": order.id
                    }
                )

                order_item_instance.is_valid(
                        raise_exception = True
                )

                saved_data = order_item_instance.save()
                total_cost += saved_data.total_cost

            order.total_cost = total_cost
            order.save()

            return order

    class Meta:
        model = Orders
        fields = ["customer", "order_items"]