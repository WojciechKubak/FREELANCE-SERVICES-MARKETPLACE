from profiles.views import ProfileDetailApi, ProfileCreateApi, ProfileUpdateApi
from django.urls import path, include


profile_patterns = [
    path("<int:profile_id>/", ProfileDetailApi.as_view(), name="profile-detail"),
    path("create/", ProfileCreateApi.as_view(), name="profile-create"),
    path("<int:profile_id>update/", ProfileUpdateApi.as_view(), name="profile-update"),
]

urlpatterns = [
    path("", include((profile_patterns, "profiles"))),
]
