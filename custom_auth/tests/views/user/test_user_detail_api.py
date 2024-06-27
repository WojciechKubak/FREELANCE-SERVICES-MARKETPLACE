from tests.factory import UserFactory
from custom_auth.models import RoleType
from custom_auth.views import UserDetailApi
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.tokens import RefreshToken
import pytest
import uuid


class TestUserDetailApi:
    url = "/auth/users/"

    @pytest.mark.django_db
    def test_when_user_not_found(self) -> None:
        user = UserFactory(role=RoleType.ADMIN, is_admin=True, is_active=True)
        refresh = RefreshToken.for_user(user)

        factory = APIRequestFactory()
        request = factory.get(
            self.url, HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
        )
        response = UserDetailApi.as_view()(request, user_id=uuid.uuid4())

        assert 404 == response.status_code

    @pytest.mark.django_db
    def test_when_user_found(self) -> None:
        user = UserFactory(role=RoleType.ADMIN, is_admin=True, is_active=True)
        refresh = RefreshToken.for_user(user)

        factory = APIRequestFactory()
        request = factory.get(
            self.url, HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
        )
        response = UserDetailApi.as_view()(request, user_id=user.id)

        assert 200 == response.status_code
        assert user.id == response.data["id"]
