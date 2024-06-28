from common.factories import CategoryFactory
from categories.views import CategoryListApi
from rest_framework.test import APIRequestFactory
import pytest


class TestCategoryListApi:
    url = "/categories/"

    @pytest.mark.django_db
    def test_when_api_called_with_no_categories(self) -> None:
        factory = APIRequestFactory()
        request = factory.get(self.url)

        response = CategoryListApi.as_view()(request)

        assert 404 == response.status_code

    @pytest.mark.django_db
    def test_when_api_called_with_categories(self) -> None:
        CategoryFactory.create_batch(10)
        factory = APIRequestFactory()
        request = factory.get(self.url)

        response = CategoryListApi.as_view()(request)

        assert 200 == response.status_code
        assert 10 == len(response.data)
