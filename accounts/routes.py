from accounts import endpoints
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("<int:pk>/", endpoints.UserRetriveUpdateDestroy.as_view()),
    path("token/refresh", TokenRefreshView.as_view()),
    path("register/", endpoints.RegisterView.as_view()),
    path("login/", endpoints.LoginView.as_view()),
    path("", endpoints.UserList.as_view()),
]