from accounts.models import CustomUser
from accounts.serializers import UserSerializer
from rest_framework import serializers
from products.models import Product

from products.serializers import ProductSerializer
from inventory.models import InventoryItem
from units.models import Unit
from units.serializers import UnitSerializer

class InventoryItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only = True, many = False)
    vendor = UserSerializer(read_only = True, many = False)
    unit = UnitSerializer(read_only = True, many = False)

    class Meta:
        model = InventoryItem
        fields = ["vendor", "product", "unit", "cost", "quantity", "id", "created_at"]



class InventoryItemCreateSerializer(serializers.ModelSerializer):
    vendor = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset = Product.objects.all())
    unit = serializers.PrimaryKeyRelatedField(queryset = Unit.objects.all())

    class Meta:
        model = InventoryItem
        fields = ["vendor", "product", "unit", "cost", "quantity", "id"]
