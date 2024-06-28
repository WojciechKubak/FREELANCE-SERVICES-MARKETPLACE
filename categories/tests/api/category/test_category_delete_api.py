from common.factories import UserFactory, CategoryFactory
from custom_auth.models import RoleType
from categories.views import CategoryDeleteApi
from categories.models import Category
import pytest


class TestCategoryDeleteApi:

    @pytest.mark.django_db
    def test_when_api_called_and_category_deleted(self, auth_request) -> None:
        user = UserFactory(role=RoleType.ADMIN, is_admin=True, is_active=True)
        category = CategoryFactory()
        request = auth_request(
            user=user,
            method="DELETE",
            url=f"/categories/{category.id}/delete/",
        )

        response = CategoryDeleteApi.as_view()(request, category_id=category.id)

        assert 204 == response.status_code
        assert not Category.objects.filter(id=category.id).exists()
