from common.factories import UserFactory, ProfileFactory
from profiles.services import ProfileService
from profiles.models import Profile
from rest_framework.exceptions import ValidationError
import pytest


class TestUpdateProfile:

    @pytest.mark.django_db
    def test_when_user_profile_does_not_exist(self) -> None:
        user = UserFactory()
        with pytest.raises(ValidationError):
            ProfileService.update_profile(user=user, first_name="John")

    @pytest.mark.django_db
    def test_when_user_profile_updated(self) -> None:
        profile = ProfileFactory()
        ProfileService.update_profile(
            user=profile.user, first_name=f"new{profile.first_name}"
        )
        assert Profile.objects.filter(user=profile.user).exists()
