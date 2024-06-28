from categories.views import (
    CategoryCreateApi,
    CategoryDetailApi,
    CategoryListApi,
    CategoryUpdateApi,
    CategoryDeleteApi,
    TagListApi,
    TagCreateApi,
    TagDetailApi,
    TagUpdateApi,
    TagDeleteApi,
)
from django.urls import path, include


category_patterns = [
    path("", CategoryListApi.as_view(), name="list"),
    path("<int:category_id>/", CategoryDetailApi.as_view(), name="detail"),
    path("<int:category_id>/update", CategoryUpdateApi.as_view(), name="update"),
    path("create/", CategoryCreateApi.as_view(), name="create"),
    path("<int:category_id>/delete/", CategoryDeleteApi.as_view(), name="delete"),
]
tag_patterns = [
    path("", TagListApi.as_view(), name="list"),
    path("<int:tag_id>/", TagDetailApi.as_view(), name="detail"),
    path("<int:tag_id>/", TagUpdateApi.as_view(), name="update"),
    path("create/", TagCreateApi.as_view(), name="create"),
    path("<int:tag_id>/delete/", TagDeleteApi.as_view(), name="delete"),
]

urlpatterns = [
    path("", include((category_patterns, "categories"))),
    path("tags/", include((tag_patterns, "tags"))),
]
