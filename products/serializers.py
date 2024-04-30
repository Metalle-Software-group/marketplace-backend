from rest_framework import serializers
from accounts.serializers import UserSerializer
from categories.serializers import CategorySerializer

from products.models import Attributes, Product
from units.serializers import UnitSerializer
# from users.serializers import UserSerializer

class ProductAttrSerializer(serializers.ModelSerializer):
    # owner = UserSerializer()
    category = CategorySerializer(many = False)

    class Meta:
        model = Attributes
        exclude=["added_by", "added_on"]

class ProductSerializer(serializers.ModelSerializer):
    attributes = ProductAttrSerializer(read_only = True,many = True)
    category = CategorySerializer(read_only = True, many = True)
    owner = UserSerializer(read_only = True, many = False)
    unit = UnitSerializer(read_only = True, many = False)

    class Meta:
        model = Product
        fields = ["attributes", "category", "owner", "unit", "name", "description", "size", "price"]
