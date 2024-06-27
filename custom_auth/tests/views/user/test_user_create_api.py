from tests.factory import UserFactory
from custom_auth.models import User, RoleType
from custom_auth.views import UserCreateApi
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.tokens import RefreshToken
import pytest


class TestUserCreateApi:

    @pytest.mark.django_db
    def test_when_user_created(self) -> None:
        user = UserFactory(role=RoleType.ADMIN, is_admin=True, is_active=True)
        refresh = RefreshToken.for_user(user)

        user_data = {
            "username": "user",
            "email": "user@example.com",
            "password": "password",
            "role": RoleType.ADMIN,
        }

        factory = APIRequestFactory()
        request = factory.post(
            "/auth/users/",
            user_data,
            format="json",
            HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}",
        )
        response = UserCreateApi.as_view()(request)

        assert 201 == response.status_code
        assert User.objects.filter(username=user_data["username"]).exists()
