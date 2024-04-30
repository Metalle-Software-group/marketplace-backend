from accounts.models import CustomUser
from accounts.serializers import UserSerializer
from rest_framework import serializers

from products.serializers import ProductSerializer
from inventory.models import InventoryItem
from units.serializers import UnitSerializer

class InventoryItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only = True, many = False)
    vendor = UserSerializer(read_only = True, many = False)
    unit = UnitSerializer(read_only = True, many = False)

    class Meta:
        model = InventoryItem
        fields = ["vendor", "product", "unit", "cost", "quantity"]



class InventoryItemCreateSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset = InventoryItem.objects.all())
    vendor = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())

    class Meta:
        model = InventoryItem
        fields = ["vendor", "product", "cost", "quantity"]
