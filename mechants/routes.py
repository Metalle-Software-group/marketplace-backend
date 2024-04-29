from rest_framework import routers
from mechants import endpoints
from django.urls import path

router = routers.DefaultRouter()

router.register(r"", endpoints.VendorListRetrieveView, basename="mechants")

urlpatterns =  [
    path(r"create/", endpoints.RegisterVendorView.as_view())
] + router.urls