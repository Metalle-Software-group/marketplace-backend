from inventory.serializers import InventoryItemCreateSerializer, InventoryItemSerializer
from rest_framework import generics, viewsets, response,status
from rest_framework.permissions import IsAdminUser
from inventory.models import InventoryItem


class CreateInventoryViewset(generics.CreateAPIView):

    queryset = InventoryItem.objects.all().order_by("-created_at")
    serializer_class = InventoryItemCreateSerializer

    view_permissions = {
        "post,create": {"admin_or_vendor": True},
        "options": {"any": True},
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = {**request.data, **{"vendor":self.request.user.id}})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return response.Response(
            serializer.data,
            status = status.HTTP_201_CREATED,
            headers = self.get_success_headers(serializer.data),
            )


    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)

class AlterInventoryViewSet(viewsets.GenericViewSet, generics.RetrieveUpdateDestroyAPIView):
    view_permissions = {
        "retrieve,put,patch,delete,destroy,update,partial_update": {"admin_or_owner": True},
        "options": {"any": True},
    }

    serializer_class = InventoryItemCreateSerializer
    queryset = InventoryItem.objects.all().order_by("-created_at")

    def is_admin_check(self, request):
        return IsAdminUser().has_permission(request, self)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = InventoryItemSerializer
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk)

# Create your views here.
class InventoryListViewSet(viewsets.GenericViewSet, generics.ListAPIView):
    view_permissions = {
        "list,get": {"admin_or_vendor": True},
        "options": {"any": True},
    }

    serializer_class = InventoryItemSerializer
    queryset = InventoryItem.objects.all().order_by("-created_at")

    def is_admin_check(self, request):
        return IsAdminUser().has_permission(request, self)

    def list(self, request, *args, **kwargs):
        if not self.is_admin_check(request):
            self.queryset = self.queryset.filter(vendor=self.request.user.vendor.id)

        return super().list(request, *args, **kwargs)