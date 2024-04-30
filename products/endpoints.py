from rest_framework import viewsets, generics
from products.serializers import ProductSerializer
from products.models import Product

# Create your views here.
class ProductViewSet(viewsets.GenericViewSet,  generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    view_permissions = {
        "put,patch,delete,create,post": {"admin_or_owner": True},
        "list,retrieve": {"any": True},
        "options": {"any": True},
    }

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
