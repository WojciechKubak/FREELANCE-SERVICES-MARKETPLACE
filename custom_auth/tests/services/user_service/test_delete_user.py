from tests.factory import UserFactory
from custom_auth.service import UserService
from custom_auth.models import User
import pytest


class TestDeleteUser:

    @pytest.mark.django_db
    def test_when_user_deleted(self) -> None:
        user = UserFactory()
        UserService.delete_user(user_id=user.id)
        assert not User.objects.filter(id=user.id).exists()
