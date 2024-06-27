from tests.factory import UserFactory
from custom_auth.service import UserService
from custom_auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime
import pytest


class TestActivateUser:
    token_now = datetime.now().timestamp() * 1000

    @pytest.mark.django_db
    def test_when_token_expired(self) -> None:
        user = UserFactory(is_active=False)

        with pytest.raises(ValidationError):
            UserService.activate_user(
                username=user.username, timestamp=self.token_now - 10000
            )

    @pytest.mark.django_db
    def test_when_activated(self) -> None:
        user = UserFactory(is_active=False)

        UserService.activate_user(
            username=user.username, timestamp=self.token_now + 10000
        )

        assert User.objects.get(username=user.username).is_active
