from inventory.serializers import InventoryItemCreateSerializer, InventoryItemSerializer
from rest_framework import generics, viewsets, response,status
from inventory.models import InventoryItem


# Create your views here.
class InventoryViewSet(viewsets.GenericViewSet,  generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    view_permissions = {
        "put,patch,delete,destroy,create,post,update,partial_update": {"admin_or_owner": True},
        "list,retrieve": {"any": True},
        "options": {"any": True},
    }

    serializer_class = InventoryItemSerializer
    queryset = InventoryItem.objects.all().order_by("-created_at")


    def create(self, request, *args, **kwargs):
        serializer = InventoryItemCreateSerializer(data = {**request.data, **{"vendor":self.request.user.id}})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return response.Response(
            serializer.data,
            status = status.HTTP_201_CREATED,
            headers = self.get_success_headers(serializer.data),
            )

    def put(self, request, pk=None):
        return self.update(request, pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk)

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)
