from rest_framework import viewsets, generics, status, response
from orders.serializers import OrderCreateSerializer, OrderSerializer
from orders.models import Orders


class CreateOrderViewset(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer

    view_permissions = {
        "post,create": {"user": True},
        "options": {"any": True},
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = {**request.data, **{ "customer": self.request.user.id }})

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return response.Response(
            serializer.data,
            status = status.HTTP_201_CREATED,
            headers = self.get_success_headers(serializer.data),
            )


# Create your views here.
class OrdersViewSet(viewsets.GenericViewSet,  generics.ListAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all().order_by("-order_date")
    serializer_class = OrderSerializer

    view_permissions = {
        "put,patch,delete,destroy,update,partial_update": {"admin_or_owner": True},
        "list,retrieve": {"user": True},
        "options": {"any": True},
    }

    def list(self, request, *args, **kwargs):
        self.queryset = Orders.objects.filter(
            **{"customer": request.user.id} if request.user.is_superuser else {}
        ).order_by("-order_date")
        return super().list(request, *args, **kwargs)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.id)
