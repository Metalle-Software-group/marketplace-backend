from attributes import serializers as AttributeSerializers
from rest_framework import serializers

# models
from attributes import models as AttributeModelAlias
from products import models as ProductModelAlias
from variants import models as VariantModelAlias


class SKUSerializer(serializers.ModelSerializer):
    attr = AttributeSerializers.VariantAttributeSerializer(
        many=True, read_only=True)
    # product = ProductSerializer(read_only = True, many = False)

    class Meta:
        model = VariantModelAlias.Variant
        fields = ["price", "quantity", "product", "attr", "id", "sku"]


class SKUCreateSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=ProductModelAlias.Product.objects.all(),
        required=True
    )

    attributes = serializers.PrimaryKeyRelatedField(
        queryset=AttributeModelAlias.SKUAttribute.objects.all(),
        required=False,
        many=True,
    )

    class Meta:
        model = VariantModelAlias.Variant
        fields = ["price", "quantity", "product", "id", "attributes", "sku"]
