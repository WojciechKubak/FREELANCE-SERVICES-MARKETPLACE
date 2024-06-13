from custom_auth.services import AuthService, RoleType
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import serializers


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
