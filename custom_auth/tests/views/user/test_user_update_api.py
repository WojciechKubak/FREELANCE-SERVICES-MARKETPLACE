from tests.factory import UserFactory
from custom_auth.models import User, RoleType
from custom_auth.views import UserUpdateApi
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.tokens import RefreshToken
import pytest


class TestUserUpdateApi:

    @pytest.mark.django_db
    def test_when_user_updated(self) -> None:
        _user = UserFactory(role=RoleType.ADMIN, is_admin=True, is_active=True)
        refresh = RefreshToken.for_user(_user)
        user = UserFactory()

        user_data = {"username": f"new_{user.username}"}

        factory = APIRequestFactory()
        request = factory.put(
            "/auth/users/",
            user_data,
            format="json",
            HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}",
        )
        response = UserUpdateApi.as_view()(request, user_id=user.id)

        assert 200 == response.status_code
        assert User.objects.filter(username=user_data["username"]).exists()
