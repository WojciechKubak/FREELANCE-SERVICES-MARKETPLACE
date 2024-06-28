from common.factories import CategoryFactory
from categories.views import CategoryDetailApi
from rest_framework.test import APIRequestFactory
import pytest


class TestCategoryDetailApi:
    url = "/categories/"

    @pytest.mark.django_db
    def test_when_api_called_and_category_not_found(self) -> None:
        factory = APIRequestFactory()
        request = factory.get(self.url)

        response = CategoryDetailApi.as_view()(request, category_id=999)

        assert 404 == response.status_code

    @pytest.mark.django_db
    def test_when_api_called_and_category_found(self) -> None:
        category = CategoryFactory()
        factory = APIRequestFactory()
        request = factory.get(self.url)

        response = CategoryDetailApi.as_view()(request, category_id=category.id)

        assert 200 == response.status_code
        assert category.id == response.data["id"]
