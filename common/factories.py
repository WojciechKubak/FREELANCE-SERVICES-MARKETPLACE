from factory.django import DjangoModelFactory
from custom_auth.models import User, RoleType
from categories.models import Category, Tag
from profiles.models import Profile
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


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("word")
    description = factory.Faker("sentence")
    author = factory.SubFactory(UserFactory)


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Faker("word")
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)


class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    description = factory.Faker("sentence")
    location = factory.Faker("city")
