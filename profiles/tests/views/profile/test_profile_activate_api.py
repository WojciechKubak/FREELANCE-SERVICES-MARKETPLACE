from common.factories import UserFactory, ProfileFactory
from profiles.models import Profile
from profiles.views import ProfileActivateApi
import pytest


class TestProfileActivateApi:

    @pytest.mark.django_db
    def test_when_profile_not_found(self, auth_request) -> None:
        user = UserFactory()
        request = auth_request(
            user=user,
            method="POST",
            url="/profiles/activate",
        )

        response = ProfileActivateApi.as_view()(request)

        assert 400 == response.status_code

    @pytest.mark.django_db
    def test_when_profile_activated(self, auth_request) -> None:
        user = UserFactory()
        profile = ProfileFactory(user=user, is_active=False)
        request = auth_request(
            user=user,
            method="POST",
            url="/profiles/activate",
        )

        response = ProfileActivateApi.as_view()(request)

        assert 200 == response.status_code
        assert Profile.objects.filter(id=profile.id, is_active=True).exists()
