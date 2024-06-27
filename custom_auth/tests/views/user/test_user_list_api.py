from tests.factory import UserFactory
from custom_auth.models import RoleType
from custom_auth.views import UserListApi
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.tokens import RefreshToken
import pytest


class TestUserListApi:
    url = "/auth/users/"

    @pytest.mark.django_db
    @pytest.mark.skip("This endpoint needs to have filters modified")
    def test_when_user_list_api_called(self) -> None:
        user = UserFactory(role=RoleType.ADMIN, is_admin=True, is_active=True)
        refresh = RefreshToken.for_user(user)

        UserFactory.create_batch(10)

        factory = APIRequestFactory()
        request = factory.get(
            self.url, HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
        )
        response = UserListApi.as_view()(request)

        assert 200 == response.status_code
