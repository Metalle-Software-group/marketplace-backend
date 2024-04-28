from django.urls import path
from orders.endpoints import OrderViewSet


urlpatterns = [
    path(
        "",
        OrderViewSet.as_view(),
        )
        ]