from common.factories import UserFactory
from profiles.views import ProfileCreateApi
from profiles.models import Profile
import pytest


class TestProfileCreateApi:
    url = "/profiles/create/"

    @pytest.mark.django_db
    def test_when_profile_created(self, auth_request) -> None:
        user = UserFactory()
        request = auth_request(
            user=user,
            method="POST",
            url=self.url,
            data={
                "first_name": "John",
                "last_name": "Doe",
                "country": "USA",
                "city": "New York",
            },
        )

        response = ProfileCreateApi.as_view()(request)

        assert response.status_code == 200
        assert Profile.objects.filter(user=user).exists()
