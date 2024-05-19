from django.urls import path
from rest_framework import routers

from payments import endpoints as PaymentsEndpoint

routes = routers.DefaultRouter()

routes.register("", PaymentsEndpoint.PaymentViewSet, basename="payment")

urlpatterns = [
    path(r"pay", PaymentsEndpoint.CreatePaymentViewset.as_view())
] + routes.urls
