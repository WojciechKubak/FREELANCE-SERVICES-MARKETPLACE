from common.security import roles_required
from articles.forms import TagForm, CategoryForm, ArticleForm
from articles.models import Article, Category, Tag
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
import logging

logging.basicConfig(level=logging.INFO)


@roles_required(["USER", "REDACTOR", "ADMIN"])
def home(request):
    articles = Article.objects.only("title", "author", "created_at")
    return render(
        request,
        "articles/home.html",
        {
            "articles": articles,
            "has_permissions": request.session.get("role").upper()
            in ["REDACTOR", "ADMIN"],
        },
    )


@roles_required(["USER", "REDACTOR", "ADMIN"])
def tags(request):
    tags = Tag.objects.all()
    return render(
        request,
        "articles/tags.html",
        {
            "tags": tags,
            "has_permissions": request.session.get("role").upper()
            in ["REDACTOR", "ADMIN"],
        },
    )


@roles_required(["USER", "REDACTOR", "ADMIN"])
def categories(request):
    categories = Category.objects.all()
    return render(
        request,
        "articles/categories.html",
        {
            "categories": categories,
            "has_permissions": request.session.get("role").upper()
            in ["REDACTOR", "ADMIN"],
        },
    )


@roles_required(["USER", "REDACTOR", "ADMIN"])
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    logging.info(article.tags)
    return render(request, "articles/article_detail.html", {"article": article})


@roles_required(["REDACTOR"])
def create_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles:tags")
    else:
        form = TagForm()
    return render(request, "articles/create_tag.html", {"form": form})


@roles_required(["REDACTOR"])
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles:categories")
    else:
        form = CategoryForm()
    return render(request, "articles/create_category.html", {"form": form})


@roles_required(["REDACTOR"])
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()
            return redirect("articles:home")
    else:
        form = ArticleForm()

    return render(request, "articles/create_article.html", {"form": form})
