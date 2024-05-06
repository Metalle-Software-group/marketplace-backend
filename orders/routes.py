from django.urls import path
from orders import endpoints
from rest_framework import routers

router = routers.DefaultRouter()

router.register("", endpoints.OrdersViewSet, basename="orders")



urlpatterns = [
    path("create/", endpoints.CreateOrderViewset.as_view())
] + router.urls