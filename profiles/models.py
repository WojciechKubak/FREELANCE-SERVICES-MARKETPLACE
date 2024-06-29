from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    country = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)

    user = models.OneToOneField("custom_auth.User", on_delete=models.CASCADE)

    def update(
        self,
        first_name: str | None,
        last_name: str | None,
        country: str | None,
        city: str | None,
        description: str | None,
    ) -> None:
        self.first_name = first_name if first_name else self.first_name
        self.last_name = last_name if last_name else self.last_name
        self.country = country if country else self.country
        self.city = city if city else self.city
        self.description = description if description else self.description
        self.full_clean()
        self.save()
