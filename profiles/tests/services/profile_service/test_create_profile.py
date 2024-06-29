from common.factories import UserFactory, ProfileFactory
from profiles.services import ProfileService
from profiles.models import Profile
from rest_framework.exceptions import ValidationError
import pytest


class TestCreateProfile:
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "country": "USA",
        "city": "New York",
    }

    @pytest.mark.django_db
    def test_when_profile_already_exists(self) -> None:
        profile = ProfileFactory()
        with pytest.raises(ValidationError):
            ProfileService.create_profile(user=profile.user, **self.data)

    @pytest.mark.django_db
    def test_when_profile_created(self) -> None:
        user = UserFactory()
        ProfileService.create_profile(user=user, **self.data)
        assert Profile.objects.filter(user=user).exists()
