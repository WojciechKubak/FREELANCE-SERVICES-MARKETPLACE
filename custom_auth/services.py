from custom_auth.models import RoleType, User
from django.core.exceptions import ValidationError
from app.email import EmailService
from dataclasses import dataclass
from datetime import datetime


@dataclass
class AuthService:

    @staticmethod
    def create_user(
        *, username: str, password: str, email: str, role: RoleType
    ) -> User:
        user = (
            User.objects.create_user(username, email, password, role)
            if role != RoleType.ADMIN
            else User.objects.create_superuser(username, email, password)
        )
        EmailService.send_activation_link(user, email)
        return user

    @staticmethod
    def update_user(
        *, user_id: str, username: str = None, email: str = None, role: RoleType = None
    ) -> User:
        user = User.objects.get(id=user_id)
        user.update(username, email, role)
        return user

    @staticmethod
    def register_user(*, username: str, password: str, email: str) -> User:
        user = User.objects.create_user(username, email, password, RoleType.USER)
        EmailService.send_activation_link(user, email)
        return user

    @staticmethod
    def activate_user(*, username: str, timestamp: float) -> User:
        if timestamp < datetime.now().timestamp() * 1000:
            raise ValidationError("Activation link has expired")
        user = User.objects.get(username=username)
        user.activate()
        return user
