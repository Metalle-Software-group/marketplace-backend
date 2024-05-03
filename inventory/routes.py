from django.urls import path
from rest_framework import routers
from inventory import endpoints

routes = routers.DefaultRouter()

routes.register(r"", endpoints.AlterInventoryViewSet, basename="alter-inventory")
routes.register(r"", endpoints.InventoryListViewSet, basename="list-inventory")


urlpatterns = [
    path("create/", endpoints.CreateInventoryViewset.as_view())
] + routes.urls