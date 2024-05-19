from attributes import endpoints as attributeEdnpoints
from rest_framework import routers
from django.urls import include, path
from products import endpoints

router = routers.DefaultRouter()

router.register(r"attributes", attributeEdnpoints.ProductAttributeViewSet,
                basename="attributes")

router.register(r"", endpoints.ProductViewSet, basename="products")

urlpatterns = [
    path(r"create/", endpoints.CreateProductViewset.as_view()),

    path('categories/', include('categories.routes')),
    path('attributes/', include('attributes.routes')),
    path('variants/', include('variants.routes')),
    path('coupons/', include('coupons.routes')),
    path('units/', include('units.routes')),
] + router.urls
