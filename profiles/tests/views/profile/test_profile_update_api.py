from common.factories import UserFactory, ProfileFactory, ProfileDataFactory
from profiles.views import ProfileUpdateApi
from profiles.models import Profile
import pytest


class TestProfileUpdateApi:
    url = "/profiles/update/"
    data = ProfileDataFactory()

    @pytest.mark.django_db
    def test_when_profile_does_not_exist(self, auth_request) -> None:
        user = UserFactory()
        request = auth_request(user=user, method="PUT", url=self.url, data=self.data)

        response = ProfileUpdateApi.as_view()(request)

        assert 400 == response.status_code

    @pytest.mark.django_db
    def test_when_profile_partially_updated(self, auth_request) -> None:
        profile = ProfileFactory()
        updated_description = f"new_{profile.description}"
        request = auth_request(
            user=profile.user,
            method="PUT",
            url=self.url,
            data={"description": updated_description},
        )

        response = ProfileUpdateApi.as_view()(request)

        assert 200 == response.status_code
        assert Profile.objects.filter(description=updated_description).exists()

    @pytest.mark.django_db
    def test_when_profile_fully_updated(self, auth_request) -> None:
        profile = ProfileFactory()
        request = auth_request(
            user=profile.user, method="PUT", url=self.url, data=self.data
        )

        response = ProfileUpdateApi.as_view()(request)

        assert 200 == response.status_code
        assert Profile.objects.filter(**self.data).exists()
