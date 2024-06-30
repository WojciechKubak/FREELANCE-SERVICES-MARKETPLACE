from common.factories import UserFactory, ProfileFactory, ProfileDataFactory
from profiles.views import ProfileCreateApi
from profiles.models import Profile
import pytest


class TestProfileCreateApi:
    url = "/profiles/create/"
    data = ProfileDataFactory()

    @pytest.mark.django_db
    def test_when_user_profile_already_exists(self, auth_request) -> None:
        profile = ProfileFactory()
        request = auth_request(
            user=profile.user, method="POST", url=self.url, data=self.data
        )

        response = ProfileCreateApi.as_view()(request)

        assert 400 == response.status_code

    @pytest.mark.django_db
    def test_when_profile_created(self, auth_request) -> None:
        user = UserFactory()
        request = auth_request(user=user, method="POST", url=self.url, data=self.data)

        response = ProfileCreateApi.as_view()(request)

        assert 201 == response.status_code
        assert Profile.objects.filter(user=user).exists()
