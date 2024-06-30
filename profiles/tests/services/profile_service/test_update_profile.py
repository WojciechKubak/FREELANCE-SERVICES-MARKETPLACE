from common.factories import UserFactory, ProfileFactory, ProfileDataFactory
from profiles.services import ProfileService
from profiles.models import Profile
from rest_framework.exceptions import ValidationError
import pytest


class TestUpdateProfile:
    data = ProfileDataFactory()

    @pytest.mark.django_db
    def test_when_user_profile_does_not_exist(self) -> None:
        user = UserFactory()
        with pytest.raises(ValidationError):
            ProfileService.update_profile(user=user, **self.data)

    @pytest.mark.django_db
    def test_when_user_profile_partially_updated(self) -> None:
        profile = ProfileFactory()
        updated_first_name = f"new_{profile.first_name}"

        ProfileService.update_profile(user=profile.user, first_name=updated_first_name)
        assert Profile.objects.filter(first_name=updated_first_name).exists()

    @pytest.mark.django_db
    def test_when_user_profile_fully_updated(self) -> None:
        profile = ProfileFactory()
        ProfileService.update_profile(user=profile.user, **self.data)
        assert Profile.objects.filter(**self.data).exists()
