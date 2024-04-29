from rest_framework import viewsets, generics

from payments.models import Payments
from payments.serializers import PaymentSerializer

# Create your views here.
class PaymentViewSet(viewsets.GenericViewSet,  generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()

    view_permissions = {
        "put,patch,destroy": {"admin": True},
        "retrieve": {"user": True},
        "options": {"any": True},
        "list": {"any": True},
    }

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)