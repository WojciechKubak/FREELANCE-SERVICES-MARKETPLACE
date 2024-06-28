from categories.models import Category, Tag
from custom_auth.models import User
from dataclasses import dataclass
from typing import Optional


@dataclass
class CategoryService:

    @staticmethod
    def create_category(*, author: User, name: str, description: str) -> Category:
        category = Category.objects.create(
            author=author, name=name, description=description
        )
        return category

    @staticmethod
    def update_category(
        *,
        category_id: int,
        name: Optional[str] = None,
        description: Optional[str] = None
    ) -> Category:
        category = Category.objects.get(id=category_id)
        category.update(name=name, description=description)
        return category

    @staticmethod
    def delete_category(*, category_id: int) -> None:
        category = Category.objects.get(id=category_id)
        category.delete()


@dataclass
class TagService:

    @staticmethod
    def create_tag(*, author: User, category_id: int, name: str) -> Tag:
        tag = Tag.objects.create(author=author, category_id=category_id, name=name)
        return tag

    @staticmethod
    def update_tag(
        *, tag_id: int, name: Optional[str] = None, category_id: Optional[int] = None
    ) -> Tag:
        tag = Tag.objects.get(id=tag_id)
        tag.update(name=name, category_id=category_id)
        return tag

    @staticmethod
    def delete_tag(*, tag_id: int) -> None:
        tag = Tag.objects.get(id=tag_id)
        tag.delete()
