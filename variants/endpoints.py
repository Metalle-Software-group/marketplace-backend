from rest_framework import viewsets, generics, status, response

# serializers
from variants import serializers as ProductSerializers

# models
from categories import models as CategoryModelAlias
from products import models as ProductModelAlias
from variants import models as VariantModelAlias
from accounts import models as UserModelAlias
from units import models as UnitModelAlias


class CreateVariantViewset(generics.CreateAPIView):
    queryset = VariantModelAlias.Variant.objects.all().order_by("-created_at")
    serializer_class = ProductSerializers.SKUCreateSerializer

    view_permissions = {
        "post,create": {"admin_or_vendor": True},
        "options": {"any": True},
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data={
                **request.data,
                "vendor": self.request.user.id
            }
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return response.Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(
                serializer.data
            ),
        )


class VariantViewSet(viewsets.GenericViewSet,  generics.ListAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializers.SKUSerializer
    queryset = ProductModelAlias.Product.objects.all().order_by("-created_at")
    lookup_field = "product_pk"

    view_permissions = {
        "put,patch,delete,destroy,update,partial_update": {"admin_or_vendor": True},
        "list,retrieve": {"any": True},
        "options": {"any": True},
    }

    # override the get query set method
    def get_queryset(self):
        if self.request.method in ['PUT', 'PATCH', "UPDATE", "DELETE", "DESTROY", "PARTIAL_UPDATE"]:
            return self.queryset if self.request.user.is_authenticated and \
                self.request.user.is_superuser else self.queryset.filter(vendor=self.request.user)
        else:
            return self.queryset

    # override the get serializer class
    def get_serializer(self, *args, **kwargs):
        if self.request.method in ['PUT', 'PATCH', "UPDATE", "PARTIAL_UPDATE"]:
            kwargs.setdefault('context', self.get_serializer_context())
            return ProductSerializers.SKUCreateSerializer(*args, **kwargs)

        return super().get_serializer(*args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk)

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)
