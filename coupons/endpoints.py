from rest_framework import viewsets,generics, permissions
from coupons.models import Coupon
from coupons.serializers import CouponSerializer

from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.
class CouponViewSet(viewsets.GenericViewSet,  generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = CouponSerializer
    queryset = Coupon.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
