from tests.factory import UserFactory
from custom_auth.service import UserService
from custom_auth.models import User
import pytest


@pytest.mark.django_db
def test_update_user() -> None:
    user = UserFactory()
    new_username = f"new_{user.username}"

    UserService.update_user(user_id=user.id, username=new_username)

    assert User.objects.filter(username=new_username).exists()
    assert not User.objects.filter(username=user.username).exists()
