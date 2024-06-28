from common.factories import TagFactory
from categories.views import TagListApi
from rest_framework.test import APIRequestFactory
import pytest


class TestTagListApi:
    url = "/categories/tags/"

    @pytest.mark.django_db
    def test_when_api_called_with_no_tags(self) -> None:
        factory = APIRequestFactory()
        request = factory.get(self.url)

        response = TagListApi.as_view()(request)

        assert 404 == response.status_code

    @pytest.mark.django_db
    def test_when_api_called_with_tags_found(self) -> None:
        TagFactory.create_batch(10)
        factory = APIRequestFactory()
        request = factory.get(self.url)

        response = TagListApi.as_view()(request)

        assert 200 == response.status_code
        assert 10 == len(response.data)
