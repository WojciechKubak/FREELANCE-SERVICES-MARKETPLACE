from common.factories import UserFactory, ProfileFactory
from profiles.views import ProfileUpdateApi
from profiles.models import Profile
import pytest


class TestProfileUpdateApi:
    url = "/profiles/update/"

    @pytest.mark.django_db
    def test_when_profile_does_not_exist(self, auth_request) -> None:
        user = UserFactory()
        request = auth_request(
            user=user,
            method="PUT",
            url=self.url,
            data={
                "first_name": "John",
                "last_name": "Doe",
                "description": "description",
                "country": "USA",
                "city": "New York",
            },
        )

        response = ProfileUpdateApi.as_view()(request)

        assert 400 == response.status_code

    @pytest.mark.django_db
    def test_when_profile_updated(self, auth_request) -> None:
        profile = ProfileFactory()
        request = auth_request(
            user=profile.user,
            method="PUT",
            url=self.url,
            data={
                "first_name": "John",
                "last_name": "Doe",
                "description": f"new_{profile.description}",
                "country": "USA",
                "city": "New York",
            },
        )

        response = ProfileUpdateApi.as_view()(request)

        assert 200 == response.status_code
        assert Profile.objects.filter(description=f"new_{profile.description}").exists()
