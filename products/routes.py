from django.urls import include, path
from rest_framework import routers

from products.endpoints import ProductViewSet



router = routers.DefaultRouter()

router.register(r"", ProductViewSet, basename="products")


urlpatterns = [
    path('units/', include('units.routes')),
]+ router.urls