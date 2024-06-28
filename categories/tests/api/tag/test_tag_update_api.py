from common.factories import TagFactory, UserFactory
from custom_auth.models import RoleType
from categories.views import TagUpdateApi
from categories.models import Tag
import pytest


class TestTagyUpdateApi:

    @pytest.mark.django_db
    def test_when_api_called_and_tag_updated(self, auth_request) -> None:
        user = UserFactory(role=RoleType.ADMIN, is_admin=True, is_active=True)
        tag = TagFactory()
        request = auth_request(
            user=user,
            method="PUT",
            url=f"/categories/tags/{tag.id}/update",
            data={"name": f"new_{tag.name}"},
        )

        response = TagUpdateApi.as_view()(request, tag_id=tag.id)

        assert 200 == response.status_code
        assert Tag.objects.filter(name=f"new_{tag.name}").exists()
