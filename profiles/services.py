from custom_auth.models import User
from profiles.models import Profile
from dataclasses import dataclass
from rest_framework.exceptions import ValidationError


@dataclass
class ProfileService:

    @staticmethod
    def create_profile(
        *,
        user: User,
        first_name: str,
        last_name: str,
        country: str,
        city: str,
        description: str | None = None,
    ) -> Profile:
        if Profile.objects.filter(user=user).exists():
            raise ValidationError("Profile already exists")
        profile = Profile.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            description=description,
            country=country,
            city=city,
        )
        return profile
