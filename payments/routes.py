from rest_framework import routers

from payments.endpoints import PaymentViewSet

routes = routers.DefaultRouter()

routes.register("",PaymentViewSet, basename="payment")

urlpatterns = [] + routes.urls