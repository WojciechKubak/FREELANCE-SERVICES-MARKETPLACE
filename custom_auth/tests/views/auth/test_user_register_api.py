from custom_auth.models import User
from custom_auth.views import UserRegisterApi
from rest_framework.test import APIRequestFactory
import pytest


class TestUserRegisterApi:

    @pytest.mark.django_db
    def test_when_user_registered(self) -> None:
        user_data = {
            "username": "user",
            "email": "user@example.com",
            "password": "password",
        }

        factory = APIRequestFactory()
        request = factory.post(
            "/auth/register/",
            user_data,
            format="json",
        )
        response = UserRegisterApi.as_view()(request)

        assert 201 == response.status_code
        assert User.objects.filter(username=user_data["username"]).exists()
