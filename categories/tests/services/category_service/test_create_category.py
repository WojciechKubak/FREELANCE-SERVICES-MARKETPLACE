from common.factories import UserFactory
from categories.services import CategoryService
from categories.models import Category
import pytest


class TestCreateCategory:

    @pytest.mark.django_db
    def test_when_category_created(self) -> None:
        user = UserFactory()
        category_data = {
            "name": "Category",
            "description": "Category description",
            "author": user,
        }

        category = CategoryService.create_category(**category_data)

        assert Category.objects.filter(id=category.id).exists()
