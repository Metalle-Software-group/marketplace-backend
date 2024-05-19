from rest_framework import serializers
from orders.models import Orders
from orders.serializers import OrderSerializer
from payments.models import Payments


class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = Payments
        fields = "__all__"


class PaymentCreateSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(
        queryset=Orders.objects.all()
    )

    class Meta:
        model = Payments
        fields = ["order", "id", "method"]
