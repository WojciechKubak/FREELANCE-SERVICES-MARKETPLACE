from tests.factory import UserFactory
from custom_auth.models import User, RoleType
from custom_auth.views import UserDeleteApi
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.tokens import RefreshToken
import pytest


class TestUserDeleteApi:

    @pytest.mark.django_db
    def test_when_user_deleted(self) -> None:
        user_ = UserFactory(role=RoleType.ADMIN, is_admin=True, is_active=True)
        refresh = RefreshToken.for_user(user_)

        user = UserFactory()

        factory = APIRequestFactory()
        request = factory.delete(
            f"/auth/users/{user.id}/",
            HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}",
        )
        response = UserDeleteApi.as_view()(request, user_id=user.id)

        assert 204 == response.status_code
        assert not User.objects.filter(id=user.id).exists()
