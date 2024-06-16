from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from typing import Self
import uuid


class RoleType(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    USER = "USER", "User"
    AUTH = "AUTH", "Auth"


class UserManager(BaseUserManager):

    def create_user(
        self, username: str, email: str, password: str, role: RoleType
    ) -> Self:
        user = self.model(
            username=username, email=self.normalize_email(email), role=role
        )
        user.set_password(password)
        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, username: str, email: str, password: str) -> Self:
        user = self.create_user(username, email, password, RoleType.ADMIN)
        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(
        max_length=10,
        choices=RoleType,
        default=RoleType.USER,
    )
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    class Meta:
        db_table = "users"

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["role"]

    def update(self, username: str, email: str, role: RoleType) -> None:
        self.username = username if username else self.username
        self.email = email if email else self.email
        self.role = role if role else self.role
        self.is_admin = self.role == RoleType.ADMIN
        self.full_clean()
        self.save()

    def activate(self) -> None:
        self.is_active = True
        self.save()

    @property
    def is_staff(self) -> bool:
        return self.is_admin

    @property
    def is_user(self) -> bool:
        return self.role == RoleType.USER

    @property
    def is_auth(self) -> bool:
        return self.role in RoleType
