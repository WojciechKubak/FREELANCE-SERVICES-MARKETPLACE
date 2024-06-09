from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from typing import Self
import uuid


class UserManager(BaseUserManager):

    def create_user(self, username: str, email: str, password: str, role: str) -> Self:
        if not username:
            raise ValueError("Users must have a username")
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.role = role

        user.save(using=self._db)

        return user

    def create_superuser(self, username: str, email: str, password: str) -> Self:
        if not password:
            raise ValueError("Superusers must have a password")

        user = self.create_user(username, email, password, "ADMIN")
        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    class Meta:
        db_table = "users"

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["role"]

    @property
    def is_staff(self) -> bool:
        return self.is_admin

    @property
    def is_user(self) -> bool:
        return self.role == "USER"

    @property
    def is_auth(self) -> bool:
        return self.role in ["AUTH", "ADMIN", "USER"]
