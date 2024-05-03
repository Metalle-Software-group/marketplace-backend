from django.urls import path
from coupons.endpoints import CouponViewSet, CreateCouponViewset
from rest_framework import routers




router = routers.DefaultRouter()

router.register(r"", CouponViewSet, basename="coupons")


urlpatterns =  [
    path(r"create/", CreateCouponViewset.as_view())
] +  router.urls