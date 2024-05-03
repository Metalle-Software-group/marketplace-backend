from accounts.permissions import   IsAdminOrVendorOrReadOnly
from rest_framework import viewsets,generics
from units.serializers import UnitSerializer
from units.models import Unit

# Create your views here.
class UnitsViewSet(viewsets.GenericViewSet,  generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

    view_permissions = {
        "post,create,retrieve,list,get,update,partial_update,destroy,patch": {"admin_or_vendor": True},
        "options": {"any": True},
    }

    lookup_field = "pk"


    def put(self, request, pk=None):
        return self.update(request, pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
