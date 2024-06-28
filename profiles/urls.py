from profiles.views import ProfileDetailApi, ProfileCreateApi
from django.urls import path, include


profile_patterns = [
    path("<int:profile_id>/", ProfileDetailApi.as_view(), name="profile-detail"),
    path("create/", ProfileCreateApi.as_view(), name="profile-create"),
]

urlpatterns = [
    path("", include((profile_patterns, "profiles"))),
]
