from orders.serializers import OrderSerializer
from rest_framework import generics, permissions
from orders.models import Orders

# Create your views here.

class OrderViewSet(
    generics.ListCreateAPIView,
    generics.RetrieveUpdateDestroyAPIView
    ):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)