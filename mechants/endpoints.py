from accounts.serializers import VendorUserCreateSerializer, VendorUserSerializer
from rest_framework import generics,viewsets,status, response
from marketplace.roles import VENDOR_ROLE
from accounts.models import CustomUser


# Create your views here.
class RegisterVendorView(generics.CreateAPIView):
    serializer_class = VendorUserCreateSerializer

    view_permissions = {
        "post": {"admin": True, "anon": True},
        "options": {"any": True},
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return response.Response(
            serializer.data,
            status = status.HTTP_201_CREATED,
            headers = self.get_success_headers(serializer.data),
            )


class AlterVendorView(viewsets.GenericViewSet,generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VendorUserCreateSerializer

    view_permissions = {
        "put,patch,delete,destroy,retrieve": {"admin_or_owner": True},
        "options": {"any": True},
    }

    queryset = CustomUser.objects.filter(vendor__isnull = False)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return response.Response(
            serializer.data,
            status = status.HTTP_201_CREATED,
            headers = self.get_success_headers(serializer.data),
            )


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)


class VendorListRetrieveView(viewsets.GenericViewSet,generics.ListAPIView):
    view_permissions = {
        "get,list": {"admin": True},
        "options": {"any": True},

    }

    queryset = CustomUser.objects.filter(groups__name = VENDOR_ROLE, vendor__isnull = False)
    serializer_class = VendorUserSerializer
    lookup_field = "pk"
