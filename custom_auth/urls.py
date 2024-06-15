from custom_auth.views import (
    UserListApi,
    UserDetailApi,
    UserCreateApi,
    UserUpdateApi,
    UserActivateApi,
    UserRegisterApi,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include


auth_patterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("register/", UserRegisterApi.as_view(), name="register"),
    path("activate/", UserActivateApi.as_view(), name="activate"),
]
user_patterns = [
    path("", UserListApi.as_view(), name="list"),
    path("<str:user_id>/", UserDetailApi.as_view(), name="detail"),
    path("<str:user_id>/", UserUpdateApi.as_view(), name="update"),
    path("", UserCreateApi.as_view(), name="create"),
]

urlpatterns = [
    path("", include((auth_patterns, "courses"))),
    path("users/", include((user_patterns, "users"))),
]
