from rest_framework import serializers
from categories.serializers import CategorySerializer

from products.models import Attributes, Product
from units.serializers import UnitSerializer
# from users.serializers import UserSerializer

class ProductAttrSerializer(serializers.ModelSerializer):
    # owner = UserSerializer()
    category = CategorySerializer(many = False)

    class Meta:
        model = Attributes
        # fields = ["id", "product_name", "description", "price", "created_at", "updated_at", "owner"]
        # fields = "__all__"
        exclude=["added_by", "added_on"]

class ProductSerializer(serializers.ModelSerializer):
    # owner = UserSerializer()
    # attributes = ProductAttrSerializer(many = True)
    # category = CategorySerializer(many = False)
    # unit = UnitSerializer(many = False)

    class Meta:
        model = Product
        exclude=["owner"]
        depth = 1
