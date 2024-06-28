from profiles.views import ProfileDetailApi
from django.urls import path, include


profile_patterns = [
    path("<int:profile_id>/", ProfileDetailApi.as_view(), name="profile-detail"),
]

urlpatterns = [
    path("", include((profile_patterns, "profiles"))),
]
