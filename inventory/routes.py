from inventory.endpoints import InventoryViewSet
from rest_framework import routers

routes = routers.DefaultRouter()

routes.register(r"", InventoryViewSet, basename="inventory")

urlpatterns = routes.urls