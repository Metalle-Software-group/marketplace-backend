from django.urls import path
from accounts.endpoints import LoginView, RegisterView, UserListRetrieveView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("token/refresh", TokenRefreshView.as_view()),
    path("register/", RegisterView.as_view()),
    path("", UserListRetrieveView.as_view()),
    path("login/", LoginView.as_view()),
]