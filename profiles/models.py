from django.db import models


class Profile(models.Model):
    user = models.OneToOneField("custom_auth.User", on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)
