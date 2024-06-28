from common.factories import UserFactory, CategoryFactory
from categories.services import TagService
from categories.models import Tag
import pytest


class TestCreateTag:

    @pytest.mark.django_db
    def test_when_tag_created(self) -> None:
        user, category = UserFactory(), CategoryFactory()
        tag_data = {
            "name": "tag",
            "category_id": category.id,
            "author": user,
        }

        tag = TagService.create_tag(**tag_data)

        assert Tag.objects.filter(id=tag.id).exists()
