from tests.factory import UserFactory
from custom_auth.models import User
from custom_auth.views import UserActivateApi
from rest_framework.test import APIRequestFactory
from datetime import datetime
import pytest


class TestUserActivateApi:

    @pytest.mark.django_db
    def test_when_user_activated(self) -> None:
        user = UserFactory(is_active=False)
        valid_timestamp = datetime.now().timestamp() * 1000 + 10000

        factory = APIRequestFactory()
        request = factory.get(
            f"/auth/activate?username={user.username}&timestamp={valid_timestamp}"
        )
        response = UserActivateApi.as_view()(request)

        assert 200 == response.status_code
        assert User.objects.get(username=user.username).is_active
