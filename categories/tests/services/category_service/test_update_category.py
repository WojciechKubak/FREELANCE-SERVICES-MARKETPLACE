from common.factories import CategoryFactory
from categories.services import CategoryService
from categories.models import Category
import pytest


class TestUpdateCategory:

    @pytest.mark.django_db
    def test_when_category_updated(self) -> None:
        category = CategoryFactory()
        category_data = {
            "category_id": category.id,
            "name": f"new_{category.name}",
            "description": "Category description",
        }

        category = CategoryService.update_category(**category_data)

        assert Category.objects.filter(name=category_data["name"]).exists()
