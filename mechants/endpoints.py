from rest_framework import generics,viewsets,status, response
from accounts import serializers as VendorBaseSerializer
from accounts.models import Vendor


# Create your views here.
class RegisterVendorView(generics.CreateAPIView):
    serializer_class = VendorBaseSerializer.VendorCreateSerializer

    view_permissions = {
        "post": {"admin": True, "anon": True},
        "options": {"any": True},
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data = request.data
        )

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return response.Response(
            serializer.data,
            status = status.HTTP_201_CREATED,
            headers = self.get_success_headers(serializer.data),
            )

class VendorView(viewsets.GenericViewSet,  generics.ListAPIView, generics.RetrieveUpdateDestroyAPIView):
    view_permissions = {
        "get,list,put,patch,delete,destroy,retrieve,partial_update": {"admin": True},
        "options": {"any": True},

    }

    serializer_class = VendorBaseSerializer.VendorSerializer
    queryset = Vendor.objects.all()
    lookup_field = "pk"


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk)
