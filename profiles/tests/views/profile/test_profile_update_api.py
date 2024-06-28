from common.factories import UserFactory, ProfileFactory
from profiles.views import ProfileUpdateApi
from profiles.models import Profile
import pytest


class TestProfileUpdateApi:
    url = "/profiles"

    @pytest.mark.django_db
    def test_when_profile_does_not_exist(self, auth_request) -> None:
        user = UserFactory()
        request = auth_request(
            user=user,
            method="PUT",
            url=f"{self.url}/999/update/",
            data={
                "first_name": "John",
                "last_name": "Doe",
                "description": "description",
                "country": "USA",
                "city": "New York",
            },
        )

        response = ProfileUpdateApi.as_view()(request, profile_id=999)

        assert 404 == response.status_code

    @pytest.mark.django_db
    def test_when_profile_updated(self, auth_request) -> None:
        user = UserFactory()
        profile = ProfileFactory(user=user)
        request = auth_request(
            user=user,
            method="PUT",
            url=f"{self.url}/{profile.id}/update/",
            data={
                "first_name": "John",
                "last_name": "Doe",
                "description": f"new_{profile.description}",
                "country": "USA",
                "city": "New York",
            },
        )

        response = ProfileUpdateApi.as_view()(request, profile_id=profile.id)

        assert 200 == response.status_code
        assert Profile.objects.filter(description=f"new_{profile.description}").exists()
