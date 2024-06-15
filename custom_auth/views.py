from custom_auth.models import User, RoleType
from custom_auth.services import AuthService
from custom_auth.selectors import AuthSelectors
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import status, serializers


class UserListApi(APIView):
    permission_classes = (IsAdminUser,)

    class Pagination(LimitOffsetPagination):
        default_limit = 10
        page_size_query_param = "count"
        max_limit = 100

    pagination_class = Pagination

    class FilterSerializer(serializers.Serializer):
        role = serializers.ChoiceField(choices=RoleType, required=False)
        is_active = serializers.BooleanField(required=False)
        is_admin = serializers.BooleanField(required=False)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ["id", "username", "email", "role", "is_active"]

    def get(self, request: Request) -> Response:
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        queryset = AuthSelectors.get_user_list(
            filters=filters_serializer.validated_data
        )
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)

        if page:
            output_serializer = self.OutputSerializer(page, many=True)
            return paginator.get_paginated_response(output_serializer.data)

        output_serializer = self.OutputSerializer(queryset, many=True)
        return Response(output_serializer.data, status=status.HTTP_200_OK)


class UserCreateApi(APIView):
    permission_classes = (IsAdminUser,)

    class InputSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=20)
        email = serializers.EmailField(max_length=30)
        password = serializers.CharField(max_length=20)
        role = serializers.ChoiceField(choices=RoleType)

    class OutputSerializer(serializers.Serializer):
        id = serializers.UUIDField()
        username = serializers.CharField(max_length=20)
        email = serializers.EmailField(max_length=30)
        role = serializers.ChoiceField(choices=RoleType)
        is_active = serializers.BooleanField()
        is_admin = serializers.BooleanField()

    def post(self, request: Request) -> Response:
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        user_dto = AuthService.create_user(**input_serializer.validated_data)
        output_serializer = self.OutputSerializer(user_dto)

        return Response(output_serializer.data, status=status.HTTP_201_CREATED)


class UserRegisterApi(APIView):
    permission_classes = (AllowAny,)

    class InputSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=20)
        email = serializers.EmailField(max_length=30)
        password = serializers.CharField(max_length=20)

    class OutputSerializer(serializers.Serializer):
        id = serializers.UUIDField()
        username = serializers.CharField(max_length=20)
        email = serializers.EmailField(max_length=30)

    def post(self, request: Request) -> Response:
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        user_dto = AuthService.register_user(**input_serializer.validated_data)
        output_serializer = self.OutputSerializer(user_dto)

        return Response(output_serializer.data, status=status.HTTP_201_CREATED)


class UserActivateApi(APIView):
    permission_classes = (AllowAny,)

    def get(self, request: Request) -> Response:
        AuthService.activate_user(
            request.query_params.get("username"),
            float(request.query_params.get("timestamp")),
        )
        return Response({"message": "User activated"}, status=status.HTTP_200_OK)
