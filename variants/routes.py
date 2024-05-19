from rest_framework.routers import DefaultRouter
from django.urls import path

from attributes import endpoints as AttributeEndpoints
from variants import endpoints

router = DefaultRouter()
router.register(r"<int:product_pk>",
                endpoints.VariantViewSet, basename="variants")
router.register(r"attributes", AttributeEndpoints.VariantAttributeViewSet,
                basename="variant-attributes")


urlpatterns = [
    path(r"attributes/create",
         AttributeEndpoints.CreateVariantAttributeViewSet.as_view()),
    path(r"create", endpoints.CreateVariantViewset.as_view()),

]
