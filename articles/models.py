from common.models import BaseModel
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tag(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Article(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="articles")
    category = models.ForeignKey(
        Category, related_name="articles", on_delete=models.CASCADE
    )
    author = models.ForeignKey(User, related_name="articles", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
