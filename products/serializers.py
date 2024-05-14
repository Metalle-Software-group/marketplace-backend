from categories.serializers import CategorySerializer
from accounts.serializers import UserSerializer
from units.serializers import UnitSerializer
from rest_framework import serializers

# models
from categories import models as CategoryModelAlias
from products import models as ProductModelAlias
from accounts import models as UserModelAlias
from units import models as UnitModelAlias

from django.db import transaction

class AttributeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        [attrib, created] = ProductModelAlias.Attribute.objects.get_or_create(
            **validated_data
            )

        return attrib

    class Meta:
        model = ProductModelAlias.Attribute
        fields = ["name", "id"]

class AttributeValueSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(many = False,write_only = True)

    class Meta:
        model = ProductModelAlias.AttributeValue
        fields = ["attribute","value"]

class AttributeValueCreateSerializer(serializers.ModelSerializer):
    attribute = serializers.PrimaryKeyRelatedField(
        queryset = ProductModelAlias.Attribute.objects.all(),
        many = False,
    )

    id = serializers.IntegerField(
        read_only = True
    )

    def create(self, validated_data):
        with transaction.atomic():
            return ProductModelAlias.AttributeValue.objects.create(
                **validated_data,
                )

    class Meta:
        model = ProductModelAlias.AttributeValue
        fields = ["attribute","value", "id"]

class SKUAttributeSerializer(serializers.ModelSerializer):
    value = AttributeValueSerializer(read_only = True, many = True)
    attribute = AttributeSerializer(read_only = True, many = False)


    def to_representation(self, instance):
        return {
            'attribute': AttributeSerializer(
                instance.attribute
                ).data,
                'value': [item.get("value") for item in AttributeValueSerializer(instance.value.all(), many = True ).data]
        }

    class Meta:
        model = ProductModelAlias.SKUAttribute
        fields = ["attribute", "value", "id"]

class SKUAttributeCreateSerializer(serializers.ModelSerializer):
    sku = serializers.PrimaryKeyRelatedField(
        queryset = ProductModelAlias.SKU.objects.all(),
        many = False,
    )

    attribute = AttributeSerializer(
        many = False,
    )

    value = serializers.ListField(
        child = serializers.CharField(),
        # write_only = True
        )


    def create(self, validated_data):
        value_data = validated_data.pop("value", [])

        with transaction.atomic():
            attr_serializer = AttributeSerializer(
                    data = validated_data.pop("attribute")
                )
            attr_serializer.is_valid(
                    raise_exception = True
                )
            saved_attr = attr_serializer.save()

            sku_attr_instance = ProductModelAlias.SKUAttribute.objects.create(
                **validated_data,
                attribute = saved_attr,
                )

            for val in value_data:
                value_serializer = AttributeValueCreateSerializer(
                    data = {
                        "attribute": saved_attr.id,
                        "value": val
                    }
                )
                value_serializer.is_valid(
                    raise_exception = True
                )

                value_instance = value_serializer.save()

                # add it to the sku_attribute
                sku_attr_instance.value.add(
                    value_instance
                    )

            return sku_attr_instance


    def to_representation(self, instance):
        return {
            'sku': instance.sku.id,
            'attribute': AttributeSerializer(
                instance.attribute
                ).data,
                'value': [item.get("value") for item in AttributeValueSerializer( instance.value.all(), many = True ).data]
        }

    class Meta:
        model = ProductModelAlias.SKUAttribute
        fields = ["sku", "attribute", "value", "id"]

class SKUSerializer(serializers.ModelSerializer):
    attributes = SKUAttributeSerializer(many = True, read_only = True)
    # product = ProductSerializer(read_only = True, many = False)

    class Meta:
        model = ProductModelAlias.SKU
        fields = ["price", "quantity", "product", "attributes", "id"]

class SKUCreateSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset = ProductModelAlias.Product.objects.all(),
        required = True
        )

    attributes = serializers.PrimaryKeyRelatedField(
        queryset = ProductModelAlias.SKUAttribute.objects.all(),
        required = False,
        many = True,
    )

    class Meta:
        model = ProductModelAlias.SKU
        fields = ["price", "quantity", "product", "id","attributes"]

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True, many = True)
    variants = SKUSerializer(many = True, read_only = True)
    vendor = UserSerializer(read_only = True, many = False)
    unit = UnitSerializer(
        read_only = True,
        many = False
    )
    attributes = AttributeSerializer(
        many = True
        )

    class Meta:
        model = ProductModelAlias.Product
        fields = ["description", "name", "brand", "vendor", "category","variants","unit", "id","attributes"]
        # hidden_fields = ["is_deleted"]

class ProductCreateSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset = CategoryModelAlias.Category.objects.all(),
        slug_field="name",
        required = False,
        many = True,
        )

    vendor = serializers.PrimaryKeyRelatedField(
        queryset = UserModelAlias.CustomUser.objects.filter(
            vendor__isnull = False
            ),
            many = False
        )

    unit = serializers.PrimaryKeyRelatedField(
        queryset = UnitModelAlias.Unit.objects.all(),
        many = False
        )

    attributes = serializers.SlugRelatedField(
        queryset = ProductModelAlias.AttributeValue.objects.all(),
        slug_field="value",
        required = False,
        many = True,
        )

    class Meta:
        model = ProductModelAlias.Product
        fields = ["description", "name", "brand", "vendor", "id", "unit", "attributes", "category"]