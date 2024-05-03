from coupons.serializers import CouponCreateSerializer, CouponSerializer
from rest_framework import viewsets,generics, response, status
from coupons.models import Coupon


class CreateCouponViewset(generics.CreateAPIView):
    queryset = Coupon.objects.all().order_by("-added_on")
    serializer_class = CouponCreateSerializer

    view_permissions = {
        "post,create": {"admin_or_vendor": True},
        "options": {"any": True},
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer( data = request.data
                                         if request.user.is_superuser else {
                                             **request.data,
                                             "vendor": self.request.user.id
                                             }
                                             )

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return response.Response(
            serializer.data,
            status = status.HTTP_201_CREATED,
            headers = self.get_success_headers(serializer.data),
            )


class CouponViewSet(viewsets.GenericViewSet,  generics.ListAPIView,generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CouponSerializer
    queryset = Coupon.objects.all()

    view_permissions = {
        "put,patch,delete,destroy,update,partial_update": {"admin_or_owner": True},
        "list,retrieve,options": {"any": True},
    }

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
