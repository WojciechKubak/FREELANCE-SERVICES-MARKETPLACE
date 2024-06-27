from factory.django import DjangoModelFactory
from custom_auth.models import User, RoleType
import factory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    id = factory.Faker("uuid4")
    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda a: f"{a.username}@example.com")
    role = factory.Iterator(RoleType)
    password = factory.django.Password("password")
    is_active = factory.Faker("boolean")
    is_admin = factory.Faker("boolean")
