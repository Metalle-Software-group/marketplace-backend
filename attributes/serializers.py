from rest_framework import serializers

# models
from attributes import models as AttributeModelAlias
from products import models as ProductModelAlias
from variants import models as VariantModelAlias


from django.db import transaction


class AttributeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        [attrib, created] = AttributeModelAlias.Attribute.objects.get_or_create(
            **validated_data
        )

        return attrib

    class Meta:
        model = AttributeModelAlias.Attribute
        fields = ["name", "id"]


class AttributeValueSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(many=False, write_only=True)
    value = serializers.CharField(required=True)

    def create(self, validated_data):
        with transaction.atomic():
            return AttributeModelAlias.AttributeValue.objects.create(
                **validated_data,
            )

    class Meta:
        model = AttributeModelAlias.AttributeValue
        fields = ["attribute", "value"]


class AttributeValueCreateSerializer(serializers.ModelSerializer):
    attribute = serializers.PrimaryKeyRelatedField(
        queryset=AttributeModelAlias.Attribute.objects.all(),
        required=False,
        many=False,
    )

    id = serializers.IntegerField(
        read_only=True
    )

    def create(self, validated_data):
        with transaction.atomic():
            return AttributeModelAlias.AttributeValue.objects.create(
                **validated_data,
            )

    class Meta:
        model = AttributeModelAlias.AttributeValue
        fields = ["attribute", "value", "id"]


class ProductAttributeSerializer(serializers.ModelSerializer):
    value = AttributeValueSerializer(
        read_only=True, many=False)

    attr = AttributeSerializer(read_only=True, many=False)

    def to_representation(self, instance):
        return {
            'attr': AttributeSerializer(
                instance.attr
            ).data,
            'value': [item.get("value") for item in AttributeValueSerializer(instance.value.all(), many=True).data]
        }

    class Meta:
        model = AttributeModelAlias.ProductAttribute
        fields = ["attr", "value", "id"]


class ProductAttributeCreateSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=ProductModelAlias.Product.objects.all(),
        many=False,
    )

    attr = AttributeSerializer(
        many=False,
    )

    value = AttributeValueCreateSerializer()

    def update(
        self,
            instance: AttributeModelAlias.ProductAttribute,
            validated_data
    ):
        value = validated_data.pop("value", None)

        attribute = validated_data.pop("attr", instance.attribute)

        if attribute is not None:
            attr_serializer = AttributeSerializer(
                data={
                    **attribute,
                    id: instance.attribute.id
                },
                partial=True
            )
            attr_serializer.is_valid(
                raise_exception=True
            )
            instance.attribute = attr_serializer.save()
            # print(instance.attribute)

        if value is not None:
            # delete the previous values
            instance.value.clear()

            for val in value:
                value_serializer = AttributeValueCreateSerializer(
                    data={
                        "attribute": instance.attribute.id,
                        "value": val
                    }
                )
                value_serializer.is_valid(
                    raise_exception=True
                )

                value_instance = value_serializer.save()

                # add it to the product_attribute
                instance.value.add(
                    value_instance
                )

        return instance

    def create(self, validated_data):
        value_data = validated_data.pop("value", [])

        with transaction.atomic():
            attr_serializer = AttributeSerializer(
                data=validated_data.pop("attr")
            )
            attr_serializer.is_valid(
                raise_exception=True
            )
            saved_attr = attr_serializer.save()

            product_attr_instance = AttributeModelAlias.ProductAttribute.objects.create(
                **validated_data,
                attr=saved_attr,
            )

            for val in value_data:
                value_serializer = AttributeValueCreateSerializer(
                    data={
                        "attribute": saved_attr.id,
                        "value": val
                    }
                )
                value_serializer.is_valid(
                    raise_exception=True
                )

                value_instance = value_serializer.save()

                # add it to the product_attribute
                product_attr_instance.value.add(
                    value_instance
                )

            return product_attr_instance

    def to_representation(self, instance):
        return {
            'product': instance.product.id,
            'attr': AttributeSerializer(
                instance.attr
            ).data,
            'value': [item.get("value") for item in AttributeValueSerializer(instance.value.all(), many=True).data]
        }

    class Meta:
        model = AttributeModelAlias.ProductAttribute
        fields = ["product", "attr", "value", "id"]


class VariantAttributeSerializer(serializers.ModelSerializer):
    value = AttributeValueSerializer(
        read_only=True, many=True)
    attribute = AttributeSerializer(
        read_only=True, many=False)

    def to_representation(self, instance):
        return {
            'attribute': AttributeSerializer(
                instance.attribute
            ).data,
            'value': [item.get("value") for item in AttributeValueSerializer(instance.value.all(), many=True).data]
        }

    class Meta:
        model = AttributeModelAlias.SKUAttribute
        fields = ["attribute", "value", "id"]


class VariantAttributeCreateSerializer(serializers.ModelSerializer):
    sku = serializers.PrimaryKeyRelatedField(
        queryset=VariantModelAlias.Variant.objects.all(),
        many=False,
    )

    attribute = AttributeSerializer(
        many=False,
    )

    value = serializers.ListField(
        child=serializers.CharField(),
        # write_only = True
    )

    def update(
        self,
            instance: AttributeModelAlias.SKUAttribute,
            validated_data
    ):
        value = validated_data.pop("value", None)

        attribute = validated_data.pop("attribute", instance.attribute)

        if attribute is not None:
            attr_serializer = AttributeSerializer(
                data={
                    **attribute,
                    id: instance.attribute.id
                },
                partial=True
            )
            attr_serializer.is_valid(
                raise_exception=True
            )
            instance.attribute = attr_serializer.save()
            # print(instance.attribute)

        if value is not None:
            # delete the previous values
            instance.value.clear()

            for val in value:
                value_serializer = AttributeValueCreateSerializer(
                    data={
                        "attribute": instance.attribute.id,
                        "value": val
                    }
                )
                value_serializer.is_valid(
                    raise_exception=True
                )

                value_instance = value_serializer.save()

                # add it to the sku_attribute
                instance.value.add(
                    value_instance
                )

        return instance

    def create(self, validated_data):
        value_data = validated_data.pop("value", [])

        with transaction.atomic():
            attr_serializer = AttributeSerializer(
                data=validated_data.pop("attribute")
            )
            attr_serializer.is_valid(
                raise_exception=True
            )
            saved_attr = attr_serializer.save()

            sku_attr_instance = AttributeModelAlias.SKUAttribute.objects.create(
                **validated_data,
                attribute=saved_attr,
            )

            for val in value_data:
                value_serializer = AttributeValueCreateSerializer(
                    data={
                        "attribute": saved_attr.id,
                        "value": val
                    }
                )
                value_serializer.is_valid(
                    raise_exception=True
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
            'value': [item.get("value") for item in AttributeValueSerializer(instance.value.all(), many=True).data]
        }

    class Meta:
        model = AttributeModelAlias.SKUAttribute
        fields = ["sku", "attribute", "value", "id"]
