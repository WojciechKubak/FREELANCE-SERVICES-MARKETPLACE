from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    country = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)

    user = models.OneToOneField("custom_auth.User", on_delete=models.CASCADE)
