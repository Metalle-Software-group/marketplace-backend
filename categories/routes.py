from rest_framework import routers
from categories import endpoint
from django.urls import path

routes = routers.DefaultRouter()

routes.register("", endpoint.CategoryViewset, basename="categories")

urlpatterns = [
] + routes.urls