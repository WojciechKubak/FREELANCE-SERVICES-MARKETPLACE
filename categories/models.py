from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)


class Tag(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="tags"
    )
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
