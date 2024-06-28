from common.factories import CategoryFactory
from categories.services import CategoryService
from categories.models import Category
import pytest


class TestDeleteCategory:

    @pytest.mark.django_db
    def test_when_category_deleted(self) -> None:
        category = CategoryFactory()
        CategoryService.delete_category(category_id=category.id)
        assert not Category.objects.filter(id=category.id).exists()
