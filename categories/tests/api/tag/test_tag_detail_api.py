from common.factories import TagFactory, UserFactory
from categories.views import TagDetailApi
from custom_auth.models import RoleType
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.tokens import RefreshToken
import pytest


class TestTagDetailApi:
    url = "/categories/tags"

    @pytest.mark.django_db
    def test_when_api_called_and_tag_not_found(self) -> None:
        user = UserFactory(role=RoleType.ADMIN, is_admin=True, is_active=True)
        refresh = RefreshToken.for_user(user)
        factory = APIRequestFactory()
        request = factory.get(
            self.url, HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
        )

        response = TagDetailApi.as_view()(request, tag_id=999)

        assert 404 == response.status_code

    @pytest.mark.django_db
    def test_when_api_called_and_tag_found(self) -> None:
        user = UserFactory(role=RoleType.ADMIN, is_admin=True, is_active=True)
        refresh = RefreshToken.for_user(user)
        tag = TagFactory()
        factory = APIRequestFactory()
        request = factory.get(
            self.url, HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
        )

        response = TagDetailApi.as_view()(request, tag_id=tag.id)

        assert 200 == response.status_code
        assert tag.id == response.data["id"]
