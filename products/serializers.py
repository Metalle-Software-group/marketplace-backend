from attributes import serializers as AttributeSerializers
from variants import serializers as VariantsSerializer
from categories.serializers import CategorySerializer
from accounts.serializers import UserSerializer
from units.serializers import UnitSerializer
from rest_framework import serializers

# models
from attributes import models as AttributeModelAlias
from categories import models as CategoryModelAlias
from products import models as ProductModelAlias
from accounts import models as UserModelAlias
from units import models as UnitModelAlias


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)
    variants = VariantsSerializer.SKUSerializer(many=True, read_only=True)
    vendor = UserSerializer(read_only=True, many=False)
    unit = UnitSerializer(
        read_only=True,
        many=False
    )
    attr = AttributeSerializers.ProductAttributeSerializer(
        many=True
    )

    class Meta:
        model = ProductModelAlias.Product
        fields = ["description", "name", "brand", "vendor",
                  "category", "variants", "unit", "id", "attr", "is_deleted"]


class ProductCreateSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=CategoryModelAlias.Category.objects.all(),
        slug_field="name",
        required=False,
        many=True,
    )

    vendor = serializers.PrimaryKeyRelatedField(
        queryset=UserModelAlias.CustomUser.objects.filter(
            vendor__isnull=False
        ),
        many=False
    )

    unit = serializers.PrimaryKeyRelatedField(
        queryset=UnitModelAlias.Unit.objects.all(),
        many=False
    )

    attributes = serializers.SlugRelatedField(
        queryset=AttributeModelAlias.AttributeValue.objects.all(),
        slug_field="value",
        required=False,
        many=True,
    )

    class Meta:
        model = ProductModelAlias.Product
        fields = ["description", "name", "brand", "vendor",
                  "id", "unit", "attributes", "category"]
