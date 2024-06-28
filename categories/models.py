from custom_auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def update(self, name: str, description: str) -> None:
        self.name = name if name else self.name
        self.description = description if description else self.description
        self.full_clean()
        self.save()


class Tag(models.Model):
    name = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="tags"
    )

    def update(self, name: str, category_id: int) -> None:
        self.name = name if name else self.name
        self.category = category_id if category_id else self.category
        self.full_clean()
        self.save()
