from common.factories import CategoryFactory, UserFactory
from custom_auth.models import RoleType
from categories.views import CategoryUpdateApi
from categories.models import Category
import pytest


class TestCategoryUpdateApi:

    @pytest.mark.django_db
    def test_when_api_called_and_category_updated(self, auth_request) -> None:
        user = UserFactory(role=RoleType.ADMIN, is_admin=True, is_active=True)
        category = CategoryFactory()
        request = auth_request(
            user=user,
            method="PUT",
            url=f"/categories/{category.id}/update",
            data={"name": f"new_{category.name}"},
        )

        response = CategoryUpdateApi.as_view()(request, category_id=category.id)

        assert 200 == response.status_code
        assert Category.objects.filter(name=f"new_{category.name}").exists()
