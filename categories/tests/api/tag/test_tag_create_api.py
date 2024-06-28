from common.factories import UserFactory, CategoryFactory
from custom_auth.models import RoleType
from categories.views import TagCreateApi
from categories.models import Tag
import pytest


class TestTagCreateApi:

    @pytest.mark.django_db
    def test_when_api_called_and_tag_created(self, auth_request) -> None:
        user = UserFactory(role=RoleType.ADMIN, is_admin=True, is_active=True)
        category = CategoryFactory()
        data = {
            "name": "Tag",
            "category_id": category.id,
        }
        request = auth_request(
            user=user,
            method="POST",
            url="/categories/tags/create/",
            data=data,
        )

        response = TagCreateApi.as_view()(request)

        assert 201 == response.status_code
        assert Tag.objects.filter(name=data["name"]).exists()
