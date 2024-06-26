from common.factories import ProfileFactory
from profiles.views import ProfileDetailApi
from rest_framework.test import APIRequestFactory
import pytest


class TestProfileDetailApi:
    url = "/profiles"

    @pytest.mark.django_db
    def test_when_profile_not_found(self) -> None:
        factory = APIRequestFactory()
        request = factory.get(f"{self.url}/999/")

        response = ProfileDetailApi.as_view()(request, profile_id=999)

        assert 404 == response.status_code

    @pytest.mark.django_db
    def test_when_profile_found(self) -> None:
        profile = ProfileFactory(is_active=True)
        factory = APIRequestFactory()
        request = factory.get(f"{self.url}/{profile.id}/")

        response = ProfileDetailApi.as_view()(request, profile_id=profile.id)

        assert 200 == response.status_code
        assert profile.id == response.data["id"]

    @pytest.mark.django_db
    def test_when_profile_full_name_field_is_correctly_generated(self) -> None:
        profile = ProfileFactory(is_active=True)
        factory = APIRequestFactory()
        request = factory.get(f"{self.url}/{profile.id}/")

        response = ProfileDetailApi.as_view()(request, profile_id=profile.id)

        assert (
            f"{profile.first_name} {profile.last_name[0]}."
            == response.data["full_name"]
        )

    @pytest.mark.django_db
    def test_when_profile_location_field_is_correctly_generated(self) -> None:
        profile = ProfileFactory(is_active=True)
        factory = APIRequestFactory()
        request = factory.get(f"{self.url}/{profile.id}/")

        response = ProfileDetailApi.as_view()(request, profile_id=profile.id)

        assert f"{profile.city}, {profile.country}" == response.data["location"]
