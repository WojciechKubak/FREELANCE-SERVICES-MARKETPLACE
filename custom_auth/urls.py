from custom_auth.views import (
    UserCreateApi,
    UserActivateApi,
    UserRegisterApi,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include


auth_patterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
]
user_patterns = [
    path("create/", UserCreateApi.as_view(), name="create"),
    path("register/", UserRegisterApi.as_view(), name="register"),
    path("activate/", UserActivateApi.as_view(), name="activate"),
]

urlpatterns = [
    path("", include((auth_patterns, "courses"))),
    path("users/", include((user_patterns, "users"))),
]
