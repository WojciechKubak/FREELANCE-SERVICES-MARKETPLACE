from common.factories import TagFactory
from categories.services import TagService
from categories.models import Tag
import pytest


class TestDeleteTag:

    @pytest.mark.django_db
    def test_when_tag_deleted(self) -> None:
        tag = TagFactory()
        TagService.delete_tag(tag_id=tag.id)
        assert not Tag.objects.filter(id=tag.id).exists()
