from custom_auth.managers import UserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
import uuid


class RoleType(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    USER = "USER", "User"
    AUTH = "AUTH", "Auth"


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
