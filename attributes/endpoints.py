from attributes import serializers as AttributesSerializers
from rest_framework import generics, viewsets

# models import
from attributes import models as AttributeModelAlias

# Create your views here.


class CreateVariantAttributeViewSet(
    generics.CreateAPIView
):
    serializer_class = AttributesSerializers.VariantAttributeCreateSerializer

    view_permissions = {
        "post,create": {"admin_or_vendor": True},
        "options": {"any": True},
    }


class VariantAttributeViewSet(
    viewsets.GenericViewSet,
    generics.ListAPIView,
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = AttributesSerializers.VariantAttributeSerializer
    queryset = AttributeModelAlias.SKUAttribute.objects.all().order_by("attribute")

    view_permissions = {
        "put,patch,delete,destroy,update,partial_update": {"admin_or_vendor": True},
        "list,retrieve": {"any": True},
        "options": {"any": True},
    }

    lookup_field = "pk"

    def get_serializer(self, *args, **kwargs):
        if self.request.method in ['PUT', 'PATCH', "UPDATE", "PARTIAL_UPDATE"]:
            kwargs.setdefault('context', self.get_serializer_context())
            return AttributesSerializers.VariantAttributeCreateSerializer(*args, **kwargs)

        return super().get_serializer(*args, **kwargs)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk)

    def perform_create(self, serializer):
        serializer.save(
            vendor=self.request.user
        )


class ProductAttributeViewSet(
    viewsets.GenericViewSet,
    generics.ListAPIView,
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = AttributesSerializers.ProductAttributeSerializer
    queryset = AttributeModelAlias.ProductAttribute.objects.all().order_by("attr")

    view_permissions = {
        "put,patch,delete,destroy,update,partial_update": {"admin_or_vendor": True},
        "list,retrieve": {"any": True},
        "options": {"any": True},
    }

    lookup_field = "pk"

    def get_serializer(self, *args, **kwargs):
        if self.request.method in ['PUT', 'PATCH', "UPDATE", "PARTIAL_UPDATE"]:
            kwargs.setdefault('context', self.get_serializer_context())
            return AttributesSerializers.ProductAttributeCreateSerializer(*args, **kwargs)

        return super().get_serializer(*args, **kwargs)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk)

    def perform_create(self, serializer):
        serializer.save(
            vendor=self.request.user
        )


class ProductCreateattributeViewSet(
    generics.CreateAPIView
):
    serializer_class = AttributesSerializers.ProductAttributeCreateSerializer

    view_permissions = {
        "post,create": {"admin_or_vendor": True},
        "options": {"any": True},
    }
