from profiles.views import (
    ProfileDetailApi,
    ProfileCreateApi,
    ProfileUpdateApi,
    ProfileActivateApi,
    ProfileDeactivateApi,
)
from django.urls import path, include


profile_patterns = [
    path("<int:profile_id>/", ProfileDetailApi.as_view(), name="profile-detail"),
    path("create/", ProfileCreateApi.as_view(), name="profile-create"),
    path("update/", ProfileUpdateApi.as_view(), name="profile-update"),
    path(
        "<int:profile_id>/activate/",
        ProfileActivateApi.as_view(),
        name="profile-activate",
    ),
    path(
        "<int:profile_id>/deactivate/",
        ProfileDeactivateApi.as_view(),
        name="profile-deactivate",
    ),
]

urlpatterns = [
    path("", include((profile_patterns, "profiles"))),
]
