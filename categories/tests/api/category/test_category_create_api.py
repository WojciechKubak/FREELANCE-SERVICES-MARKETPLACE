from common.factories import UserFactory
from custom_auth.models import RoleType
from categories.views import CategoryCreateApi
from categories.models import Category
import pytest


class TestCategoryCreateApi:

    @pytest.mark.django_db
    def test_when_api_called_and_category_created(self, auth_request) -> None:
        user = UserFactory(role=RoleType.ADMIN, is_admin=True, is_active=True)
        data = {
            "name": "Category",
            "description": "Category description",
        }
        request = auth_request(
            user=user,
            url="/categories/create/",
            method="POST",
            data=data,
        )

        response = CategoryCreateApi.as_view()(request)

        assert 201 == response.status_code
        assert Category.objects.filter(name=data["name"]).exists()
