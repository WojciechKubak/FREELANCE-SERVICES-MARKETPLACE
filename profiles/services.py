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

    @staticmethod
    def update_profile(
        *,
        user: User,
        first_name: str | None = None,
        last_name: str | None = None,
        country: str | None = None,
        city: str | None = None,
        description: str | None = None,
    ) -> Profile:
        profile = Profile.objects.filter(user=user).first()
        if not profile:
            raise ValidationError("Profile does not exist")

        profile.first_name = first_name if first_name else profile.first_name
        profile.last_name = last_name if last_name else profile.last_name
        profile.country = country if country else profile.country
        profile.city = city if city else profile.city
        profile.description = description if description else profile.description
        profile.full_clean()
        profile.save()

        return profile

    @staticmethod
    def activate_profile(*, user: User) -> Profile:
        profile = Profile.objects.filter(user=user).first()
        if not profile:
            raise ValidationError("Profile does not exist")

        profile.is_active = True
        profile.full_clean()
        profile.save()

        return profile

    @staticmethod
    def deactivate_profile(*, user: User) -> Profile:
        profile = Profile.objects.filter(user=user).first()
        if not profile:
            raise ValidationError("Profile does not exist")

        profile.is_active = False
        profile.full_clean()
        profile.save()

        return profile
