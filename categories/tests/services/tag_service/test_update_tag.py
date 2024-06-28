from common.factories import TagFactory
from categories.services import TagService
from categories.models import Tag
import pytest


class TestUpdateTag:

    @pytest.mark.django_db
    def test_when_tag_updated(self) -> None:
        tag = TagFactory()
        tag_data = {
            "tag_id": tag.id,
            "name": f"new_{tag.name}",
        }

        tag = TagService.update_tag(**tag_data)

        assert Tag.objects.filter(name=tag_data["name"]).exists()
