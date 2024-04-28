from coupons.endpoints import CouponViewSet
from rest_framework import routers




router = routers.DefaultRouter()

router.register(r"", CouponViewSet, basename="coupons")


urlpatterns =  router.urls