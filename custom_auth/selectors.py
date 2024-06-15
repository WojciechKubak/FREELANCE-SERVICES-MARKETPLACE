from custom_auth.models import User
from dataclasses import dataclass
from typing import Any


@dataclass
class AuthSelectors:

    @staticmethod
    def get_user_list(*, filters: dict[str, Any]) -> list[User]:
        return User.objects.filter(**filters)

    @staticmethod
    def get_user_detail(*, user_id: str) -> User:
        return User.objects.get(id=user_id)
