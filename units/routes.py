from rest_framework import routers

from units.endpoints import UnitsViewSet

defaultRoutes = routers.DefaultRouter()
defaultRoutes.register("", UnitsViewSet, basename="units")


urlpatterns = [] + defaultRoutes.urls