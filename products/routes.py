from django.urls import include, path
from rest_framework import routers
from products import endpoints

router = routers.DefaultRouter()

router.register(r"variants/<int:product_pk>", endpoints.SKUViewSet, basename = "variants")
router.register(r"attributes", endpoints.AttributeViewSet, basename = "attributes")
router.register(r"", endpoints.ProductViewSet, basename = "products")

urlpatterns = [
    path(r"attributes/create", endpoints.CreateAttributeViewSet.as_view()),
    path(r"variants/create", endpoints.CreateSKUViewset.as_view()),
    path(r"create/", endpoints.CreateProductViewset.as_view()),

    path('categories/', include('categories.routes')),
    path('coupons/', include('coupons.routes')),
    path('units/', include('units.routes')),
] + router.urls