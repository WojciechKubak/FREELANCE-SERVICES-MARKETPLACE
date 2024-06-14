from custom_auth.models import RoleType, User
from django.core.exceptions import ValidationError
from django.db.models import QuerySet
from app.email import EmailService
from dataclasses import dataclass
from datetime import datetime
from typing import Any


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
    def get_all_users(*, filters: dict[str, Any]) -> QuerySet:
        return User.objects.filter(**filters)

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
