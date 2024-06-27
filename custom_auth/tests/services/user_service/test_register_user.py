from custom_auth.service import UserService
from custom_auth.models import User
from unittest.mock import patch
import pytest


@pytest.mark.django_db
@patch("custom_auth.service.EmailService.send_activation_link")
def test_register_user(mock_send_activation_link) -> None:
    user_data = {
        "username": "user",
        "email": "user@example.com",
        "password": "password",
    }

    UserService.register_user(**user_data)

    assert User.objects.filter(username=user_data["username"]).exists()
    mock_send_activation_link.assert_called_once_with(
        user_data["username"], user_data["email"]
    )
