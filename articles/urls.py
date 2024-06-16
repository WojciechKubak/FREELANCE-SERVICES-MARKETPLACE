from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("create_tag/", views.create_tag, name="create_tag"),
    path("create_category/", views.create_category, name="create_category"),
    path("create_article/", views.create_article, name="create_article"),
    path("<int:article_id>/", views.article_detail, name="article_detail"),
    path("", views.home, name="home"),
    path("tags/", views.tags, name="tags"),
    path("categories/", views.categories, name="categories"),
]
