from categories.models import Category, Tag
from categories.services import CategoryService, TagService
from common.utils import inline_serializer
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import serializers, status
from django.shortcuts import get_object_or_404, get_list_or_404


class CategoryListApi(APIView):
    permission_classes = (AllowAny,)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField(max_length=255)

    def get(self, _: Request) -> Response:
        categories = get_list_or_404(Category)
        output_serializer = self.OutputSerializer(categories, many=True)
        return Response(output_serializer.data)


class CategoryDetailApi(APIView):
    permission_classes = (AllowAny,)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField(max_length=255)
        description = serializers.CharField(max_length=255)

    def get(self, _: Request, category_id: int) -> Response:
        category = get_object_or_404(Category, id=category_id)
        output_serializer = self.OutputSerializer(category)
        return Response(output_serializer.data)


class CategoryCreateApi(APIView):
    permission_classes = (IsAdminUser,)

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255)
        description = serializers.CharField(max_length=255)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField(max_length=255)
        description = serializers.CharField(max_length=255)
        author = inline_serializer(
            fields={
                "id": serializers.UUIDField(),
                "username": serializers.CharField(),
            }
        )

    def post(self, request: Request) -> Response:
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        category_dto = CategoryService.create_category(
            author=request.user, **input_serializer.validated_data
        )
        output_serializer = self.OutputSerializer(category_dto)

        return Response(output_serializer.data, status=status.HTTP_201_CREATED)


class CategoryUpdateApi(APIView):
    permission_classes = (IsAdminUser,)

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255, required=False)
        description = serializers.CharField(max_length=255, required=False)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField(max_length=255)
        description = serializers.CharField(max_length=255)

    def put(self, request: Request, category_id: int) -> Response:
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        category_dto = CategoryService.update_category(
            category_id=category_id, **input_serializer.validated_data
        )
        output_serializer = self.OutputSerializer(category_dto)

        return Response(output_serializer.data)


class CategoryDeleteApi(APIView):
    permission_classes = (IsAdminUser,)

    def delete(self, _: Request, category_id: int) -> Response:
        CategoryService.delete_category(category_id=category_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TagListApi(APIView):
    permission_classes = (AllowAny,)

    class FilterSerializer(serializers.Serializer):
        category_id = serializers.IntegerField(required=False, allow_null=True)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField(max_length=255)

    def get(self, request: Request) -> Response:
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        tags = get_list_or_404(Tag, **filters_serializer.validated_data)
        output_serializer = self.OutputSerializer(tags, many=True)

        return Response(output_serializer.data)


class TagDetailApi(APIView):
    permission_classes = (IsAdminUser,)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField(max_length=255)
        category = inline_serializer(
            fields={
                "id": serializers.IntegerField(),
                "name": serializers.CharField(),
            }
        )
        author = inline_serializer(
            fields={
                "id": serializers.UUIDField(),
                "username": serializers.CharField(),
            }
        )

    def get(self, _: Request, tag_id: int) -> Response:
        tag = get_object_or_404(Tag, id=tag_id)
        output_serializer = self.OutputSerializer(tag)
        return Response(output_serializer.data)


class TagCreateApi(APIView):
    permission_classes = (IsAdminUser,)

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255)
        category_id = serializers.IntegerField()

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField(max_length=255)
        category = inline_serializer(
            fields={
                "id": serializers.IntegerField(),
                "name": serializers.CharField(),
            }
        )
        author = inline_serializer(
            fields={
                "id": serializers.UUIDField(),
                "username": serializers.CharField(),
            }
        )

    def post(self, request: Request) -> Response:
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        tag_dto = TagService.create_tag(
            author=request.user, **input_serializer.validated_data
        )
        output_serializer = self.OutputSerializer(tag_dto)

        return Response(output_serializer.data, status=status.HTTP_201_CREATED)


class TagUpdateApi(APIView):
    permission_classes = (IsAdminUser,)

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255, required=False)
        category_id = serializers.IntegerField(required=False)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField(max_length=255)
        category = inline_serializer(
            fields={
                "id": serializers.IntegerField(),
                "name": serializers.CharField(),
            }
        )
        author = inline_serializer(
            fields={
                "id": serializers.UUIDField(),
                "username": serializers.CharField(),
            }
        )

    def put(self, request: Request, tag_id: int) -> Response:
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        tag_dto = TagService.update_tag(
            tag_id=tag_id, **input_serializer.validated_data
        )
        output_serializer = self.OutputSerializer(tag_dto)

        return Response(output_serializer.data)


class TagDeleteApi(APIView):
    permission_classes = (IsAdminUser,)

    def delete(self, _: Request, tag_id: int) -> Response:
        TagService.delete_tag(tag_id=tag_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
