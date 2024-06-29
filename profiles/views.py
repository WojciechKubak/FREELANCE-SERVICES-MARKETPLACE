from profiles.models import Profile
from profiles.services import ProfileService
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_201_CREATED
from django.shortcuts import get_object_or_404


class ProfileDetailApi(APIView):
    permission_classes = (AllowAny,)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        full_name = serializers.SerializerMethodField()
        location = serializers.SerializerMethodField()
        is_active = serializers.BooleanField(source="user.is_active")

        def get_full_name(self, obj: Profile) -> str:
            return f"{obj.first_name} {obj.last_name[0]}."

        def get_location(self, obj: Profile) -> str:
            return f"{obj.city}, {obj.country}"

    def get(self, _: Request, profile_id: int) -> Response:
        profile = get_object_or_404(Profile, id=profile_id, is_active=True)
        output_serializer = self.OutputSerializer(profile)
        return Response(output_serializer.data, status=HTTP_200_OK)


class ProfileCreateApi(APIView):
    permission_classes = (IsAuthenticated,)

    class InputSerializer(serializers.Serializer):
        first_name = serializers.CharField(max_length=50)
        last_name = serializers.CharField(max_length=50)
        country = serializers.CharField(max_length=50)
        description = serializers.CharField(max_length=255, required=False)
        city = serializers.CharField(max_length=50)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        first_name = serializers.CharField(max_length=50)
        last_name = serializers.CharField(max_length=50)
        country = serializers.CharField(max_length=50)
        city = serializers.CharField(max_length=50)

    def post(self, request: Request) -> Response:
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        profile = ProfileService.create_profile(
            user=request.user, **input_serializer.validated_data
        )
        output_serializer = self.OutputSerializer(profile)

        return Response(output_serializer.data, status=HTTP_201_CREATED)


class ProfileUpdateApi(APIView):
    permission_classes = (IsAuthenticated,)

    class InputSerializer(serializers.Serializer):
        first_name = serializers.CharField(max_length=50)
        last_name = serializers.CharField(max_length=50)
        country = serializers.CharField(max_length=50)
        description = serializers.CharField(max_length=255, required=False)
        city = serializers.CharField(max_length=50)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        first_name = serializers.CharField(max_length=50)
        last_name = serializers.CharField(max_length=50)
        country = serializers.CharField(max_length=50)
        description = serializers.CharField(max_length=255, required=False)
        city = serializers.CharField(max_length=50)

    def put(self, request: Request) -> Response:
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        profile = ProfileService.update_profile(
            user=request.user, **input_serializer.validated_data
        )
        output_serializer = self.OutputSerializer(profile)

        return Response(output_serializer.data, status=HTTP_200_OK)


class ProfileDeactivateApi(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, _: Request, profile_id: int) -> Response:
        profile = get_object_or_404(Profile, id=profile_id)
        profile.deactivate()
        return Response(status=HTTP_204_NO_CONTENT)


class ProfileActivateApi(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, _: Request, profile_id: int) -> Response:
        profile = get_object_or_404(Profile, id=profile_id)
        profile.activate()
        return Response(status=HTTP_200_OK)
