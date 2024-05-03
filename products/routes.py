from django.urls import include, path
from rest_framework import routers
from products import endpoints

router = routers.DefaultRouter()

router.register('attributes', endpoints.AttributesViewSet, basename = "attributes")
router.register(r"", endpoints.ProductViewSet, basename = "products")

urlpatterns = [
    path('attributes/create/', endpoints.CreateAttributesViewset.as_view()),
    path(r"create/", endpoints.CreateProductViewset.as_view()),
    path('categories/', include('categories.routes')),
    path('coupons/', include('coupons.routes')),
    path('units/', include('units.routes')),
] + router.urls