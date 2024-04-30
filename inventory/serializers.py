from rest_framework import serializers
from accounts.serializers import UserSerializer

from inventory.models import InventoryItem
from products.models import Product
from products.serializers import ProductSerializer
from units.serializers import UnitSerializer

class InventoryItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only = True, many = False)
    vendor = UserSerializer(read_only = True, many = False)
    unit = UnitSerializer(read_only = True, many = False)

    class Meta:
        model = InventoryItem
        fields = ["vendor", "product", "unit", "price", "quantity"]