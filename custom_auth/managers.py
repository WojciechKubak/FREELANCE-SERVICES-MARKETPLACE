from django.contrib.auth.models import BaseUserManager
from typing import Self


class UserManager(BaseUserManager):

    def create_user(self, username: str, email: str, password: str, role: str) -> Self:
        user = self.model(
            username=username, email=self.normalize_email(email), role=role
        )
        user.set_password(password)
        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, username: str, email: str, password: str) -> Self:
        user = self.create_user(username, email, password, "ADMIN")
        user.is_admin = True
        user.save(using=self._db)

        return user
