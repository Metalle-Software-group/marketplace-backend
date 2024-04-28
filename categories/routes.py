from django.urls import path

from categories import endpoint


urlpatterns = [
    path('', endpoint.CategoryViewset.as_view())
]