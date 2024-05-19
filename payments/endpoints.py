from rest_framework import viewsets, generics, status, response

from payments import serializers as PaymentSerializerAlias
from payments import models as PaymentsAlias

# Create your views here.


class CreatePaymentViewset(generics.CreateAPIView):
    queryset = PaymentsAlias.Payments.objects.all().order_by("-initiated_on")
    serializer_class = PaymentSerializerAlias.PaymentCreateSerializer

    view_permissions = {
        "post,create": {"user": True},
        "options": {"any": True},
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data if self.request.user.is_superuser else {**request.data, "customer": self.request.user.id})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return response.Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data),
        )


class PaymentViewSet(viewsets.GenericViewSet,  generics.ListAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializerAlias.PaymentSerializer
    queryset = PaymentsAlias.Payments.objects.all().order_by("-initiated_on")

    view_permissions = {
        "put,patch,delete,destroy": {"admin": True},
        "retrieve,list": {"user": True},
        "options": {"any": True},
    }

    def get_queryset(self):
        queryset = self.queryset

        return queryset if self.request.user.is_authenticated and \
            self.request.user.is_superuser else queryset.filter(
                customer=self.request.user,
            )

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
