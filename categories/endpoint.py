from rest_framework import generics
from accounts.permissions import IsAdminOrVendorOrReadOnly

from categories.models import Category
from categories.serializers import CategorySerializer
# Create your views here.
class CategoryViewset(
    generics.ListCreateAPIView,
    generics.RetrieveUpdateDestroyAPIView,
    ):
    permission_classes=[IsAdminOrVendorOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer