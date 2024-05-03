from accounts.permissions import IsAdminOrVendorOrReadOnly
from categories.serializers import CategorySerializer
from rest_framework import generics,viewsets
from categories.models import Category

# Create your views here.
class CategoryViewset(
    viewsets.GenericViewSet,
    generics.ListCreateAPIView,
    generics.RetrieveUpdateDestroyAPIView,
    ):
    permission_classes=[IsAdminOrVendorOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer