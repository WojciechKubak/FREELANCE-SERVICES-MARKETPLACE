from custom_auth.service import UserService
from custom_auth.models import User, RoleType
import pytest


class TestCreateUser:
    user_data = {
        "username": "user",
        "email": "user@example.com",
        "password": "password",
        "role": RoleType.USER,
    }

    @pytest.mark.django_db
    def test_when_user_created(self) -> None:
        UserService.create_user(**self.user_data)
        assert User.objects.filter(username=self.user_data["username"]).exists()

    @pytest.mark.django_db
    def test_when_superuser_created(self) -> None:
        superuser_data = self.user_data.copy()
        superuser_data["role"] = RoleType.ADMIN

        UserService.create_user(**superuser_data)

        result = User.objects.filter(username=superuser_data["username"]).first()
        assert result.is_admin
        assert RoleType.ADMIN == result.role
