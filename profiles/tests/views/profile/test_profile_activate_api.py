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
            url="/profiles/999/activate",
        )

        response = ProfileActivateApi.as_view()(request, profile_id=999)

        assert 404 == response.status_code

    @pytest.mark.django_db
    def test_when_profile_activated(self, auth_request) -> None:
        user = UserFactory()
        profile = ProfileFactory(user=user, is_active=False)
        request = auth_request(
            user=user,
            method="POST",
            url=f"/profiles/{profile.id}/activate",
        )

        response = ProfileActivateApi.as_view()(request, profile_id=profile.id)

        assert 200 == response.status_code
        assert Profile.objects.filter(id=profile.id, is_active=True).exists()
