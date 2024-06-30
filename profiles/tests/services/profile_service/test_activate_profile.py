from common.factories import ProfileFactory, UserFactory
from profiles.services import ProfileService
from profiles.models import Profile
from rest_framework.exceptions import ValidationError
import pytest


class TestActivateProfile:

    @pytest.mark.django_db
    def test_when_profile_does_not_exist(self) -> None:
        user = UserFactory()
        with pytest.raises(ValidationError):
            ProfileService.activate_profile(user=user)

    @pytest.mark.django_db
    def test_when_profile_set_as_active(self) -> None:
        profile = ProfileFactory(is_active=False)
        ProfileService.activate_profile(user=profile.user)
        assert Profile.objects.filter(user=profile.user, is_active=True).exists()
