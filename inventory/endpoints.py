from rest_framework import generics, viewsets

from inventory.serializers import InventoryItemSerializer
from inventory.models import InventoryItem
from accounts import permissions

# Create your views here.
class InventoryViewSet(viewsets.GenericViewSet,  generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    view_permissions = {
        "put,patch,destroy,create,delete": {"admin_or_owner": True},
        "list,retrieve": {"admin_or_owner": True},
        "options": {"any": True},
    }
    serializer_class = InventoryItemSerializer
    queryset = InventoryItem.objects.all()

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)
