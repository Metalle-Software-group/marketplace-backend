from accounts.models import CustomUser
from accounts.serializers import UserSerializer
from rest_framework import serializers
from products.models import Product

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
    vendor = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset = Product.objects.all())

    class Meta:
        model = InventoryItem
        fields = ["vendor", "product", "cost", "quantity", "id"]
