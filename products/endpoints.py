from products.serializers import ProductAttrCreateSerializer, ProductAttrSerializer, ProductCreateSerializer, ProductSerializer
from rest_framework import viewsets, generics, status, response
from products.models import Attributes, Product


class CreateProductViewset(generics.CreateAPIView):
    queryset = Product.objects.all().order_by("-created_at")
    serializer_class = ProductCreateSerializer

    view_permissions = {
        "post,create": {"admin_or_vendor": True},
        "options": {"any": True},
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = {**request.data, **{ "vendor": self.request.user.id }})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return response.Response(
            serializer.data,
            status = status.HTTP_201_CREATED,
            headers = self.get_success_headers(serializer.data),
            )


# Create your views here.
class ProductViewSet(viewsets.GenericViewSet,  generics.ListAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by("-created_at")

    view_permissions = {
        "put,patch,delete,destroy,update,partial_update": {"admin_or_owner": True},
        "list,retrieve": {"any": True},
        "options": {"any": True},
    }

    def put(self, request, pk=None):
        return self.update(request, pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk)

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)

# attributes model
class CreateAttributesViewset(generics.CreateAPIView):
    queryset = Attributes.objects.all().order_by("-added_on")
    serializer_class = ProductAttrCreateSerializer

    view_permissions = {
        "post,create": {"admin": True},
        "options": {"any": True},
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = { **request.data, **{ "added_by": self.request.user.id } })
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return response.Response(
            serializer.data,
            status = status.HTTP_201_CREATED,
            headers = self.get_success_headers(serializer.data),
            )

# Create your views here.
class AttributesViewSet(viewsets.GenericViewSet,  generics.ListAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Attributes.objects.all().order_by("-added_on")
    serializer_class = ProductAttrSerializer

    view_permissions = {
        "put,patch,delete,destroy,update,partial_update": {"admin": True},
        "list,retrieve": {"any": True},
        "options": {"any": True},
    }
    def put(self, request, pk=None):
        return self.update(request, pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk)

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)
