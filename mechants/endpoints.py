from accounts.models import CustomUser, Vendor
from rest_framework.response import Response
from rest_framework import generics,viewsets
from accounts.serializers import UserSerializer
from marketplace.roles import VENDOR_ROLE
from django.contrib.auth.models import Group


# Create your views here.
class RegisterVendorView(generics.CreateAPIView):
    serializer_class = UserSerializer

    view_permissions = {
        "post": {"admin": True, "anon": True},
        "options": {"any": True},
    }

    def perform_create(self, serializer):
        user = serializer.save()
        user_group, _ = Group.objects.get_or_create(name=VENDOR_ROLE)
        user.groups.add(user_group)


class VendorListRetrieveView(viewsets.GenericViewSet,generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    view_permissions = {
        "get,list,put,create,patch,delete": {"admin_or_owner": True, "any": True},
        "options": {"any": True},

    }

    queryset = CustomUser.objects.filter(groups__name = VENDOR_ROLE)
    serializer_class = UserSerializer
    lookup_field = "pk"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
