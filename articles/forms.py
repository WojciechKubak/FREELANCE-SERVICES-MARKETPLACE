from django import forms
from .models import Tag, Category, Article


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "tags", "category"]
