from accounts.permissions import  IsAdminOrVendorOrReadOnly
from rest_framework import viewsets, generics

from products.serializers import ProductSerializer
from products.models import Product

# Create your views here.
class ProductViewSet(viewsets.GenericViewSet,  generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminOrVendorOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    view_permissions = {
        "list": {"vendor": False}
    }

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
