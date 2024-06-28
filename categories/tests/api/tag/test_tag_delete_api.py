from common.factories import UserFactory, TagFactory
from custom_auth.models import RoleType
from categories.views import TagDeleteApi
from categories.models import Tag
import pytest


class TestTagDeleteApi:

    @pytest.mark.django_db
    def test_when_api_called_and_tag_deleted(self, auth_request) -> None:
        user = UserFactory(role=RoleType.ADMIN, is_admin=True, is_active=True)
        tag = TagFactory()
        request = auth_request(
            user=user,
            method="DELETE",
            url=f"/categories/tags{tag.id}/delete/",
        )

        response = TagDeleteApi.as_view()(request, tag_id=tag.id)

        assert 204 == response.status_code
        assert not Tag.objects.filter(id=tag.id).exists()
