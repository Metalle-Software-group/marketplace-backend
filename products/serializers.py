from rest_framework import serializers
from accounts.models import CustomUser
from accounts.serializers import UserSerializer
from categories.models import Category
from categories.serializers import CategorySerializer

from products.models import Attributes, Product
from units.models import Unit
from units.serializers import UnitSerializer
# from users.serializers import UserSerializer

class ProductAttrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        exclude=["added_by", "added_on"]

class ProductAttrCreateSerializer(serializers.ModelSerializer):
    added_by = serializers.PrimaryKeyRelatedField(queryset = Attributes.objects.all())

    class Meta:
        model = Attributes
        fields = ["added_by", "attribute", "value"]


class ProductSerializer(serializers.ModelSerializer):
    attributes = ProductAttrSerializer(read_only = True, many = True)
    category = CategorySerializer(read_only = True, many = True)
    owner = UserSerializer(read_only = True, many = False)
    unit = UnitSerializer(read_only = True, many = False)

    class Meta:
        model = Product
        fields = ["attributes", "category", "owner", "unit", "name", "description", "size", "price", "id"]

class ProductCreateSerializer(serializers.ModelSerializer):
    attributes = serializers.PrimaryKeyRelatedField(queryset = Attributes.objects.all(), many = True)
    category = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all(), many = True)
    owner = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
    unit = serializers.PrimaryKeyRelatedField(queryset = Unit.objects.all())

    class Meta:
        model = Product
        fields = ["attributes", "category", "owner", "unit", "name", "description", "size", "price", ]