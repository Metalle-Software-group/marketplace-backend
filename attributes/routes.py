from attributes import endpoints as attributeEdnpoints
from rest_framework import routers
from django.urls import path

base_routers = routers.DefaultRouter()
base_routers.register(
    "", attributeEdnpoints.ProductAttributeViewSet, basename="product-attributes"
)

base_routers.register(
    "variants", attributeEdnpoints.VariantAttributeViewSet, basename="variant-attributes"
)

urlpatterns = [
    path(r"create",
         attributeEdnpoints.ProductCreateattributeViewSet.as_view()),
    path(
        r"variants/create", attributeEdnpoints.CreateVariantAttributeViewSet.as_view()
    )
] + base_routers.urls
