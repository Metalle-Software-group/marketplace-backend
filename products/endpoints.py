from rest_framework import viewsets, generics, status, response

# serializers
from products import serializers as ProductSerializers

# models
from categories import models as CategoryModelAlias
from products import models as ProductModelAlias
from accounts import models as UserModelAlias
from units import models as UnitModelAlias


class CreateProductViewset(generics.CreateAPIView):
    queryset = ProductModelAlias.Product.objects.all().order_by("-created_at")
    serializer_class = ProductSerializers.ProductCreateSerializer

    view_permissions = {
        "post,create": {"admin_or_vendor": True},
        "options": {"any": True},
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data if self.request.user.is_superuser else {**request.data, "vendor": self.request.user.id})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return response.Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data),
        )


class ProductViewSet(
    viewsets.GenericViewSet,
    generics.ListAPIView,
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = ProductSerializers.ProductSerializer
    queryset = ProductModelAlias.Product.objects.all().order_by("-created_at")

    view_permissions = {
        "put,patch,delete,destroy,update,partial_update": {"admin_or_vendor": True},
        "list,retrieve": {"any": True},
        "options": {"any": True},
    }

    def get_queryset(self):
        queryset = self.queryset

        if self.request.method in ['PUT', 'PATCH', "UPDATE", "DELETE", "DESTROY", "PARTIAL_UPDATE"]:
            return queryset if self.request.user.is_authenticated and \
                self.request.user.is_superuser else queryset.filter(
                    vendor=self.request.user,
                )

        return queryset.filter(
            **{} if self.request.user.is_authenticated and
            self.request.user.is_superuser else {"is_deleted": False}
        )

    def put(self, request, pk=None):
        return self.update(request, pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk)

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)
