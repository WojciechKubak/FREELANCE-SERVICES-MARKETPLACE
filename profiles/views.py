from profiles.models import Profile
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_200_OK
from django.shortcuts import get_object_or_404


class ProfileDetailApi(APIView):
    permission_classes = (AllowAny,)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        first_name = serializers.CharField(max_length=30)
        last_name = serializers.CharField(max_length=30)
        country = serializers.CharField(max_length=30)
        city = serializers.CharField(max_length=30)
        is_active = serializers.BooleanField(source="user.is_active")

    def get(self, _: Request, profile_id: int) -> Response:
        profile = get_object_or_404(Profile, id=profile_id)
        output_serializer = self.OutputSerializer(profile)
        return Response(output_serializer.data, status=HTTP_200_OK)


class ProfileCreateApi(APIView):
    permission_classes = (IsAuthenticated,)

    class InputSerializer(serializers.Serializer):
        first_name = serializers.CharField(max_length=30)
        last_name = serializers.CharField(max_length=30)
        country = serializers.CharField(max_length=30)
        description = serializers.CharField(max_length=255, required=False)
        city = serializers.CharField(max_length=30)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        first_name = serializers.CharField(max_length=30)
        last_name = serializers.CharField(max_length=30)
        country = serializers.CharField(max_length=30)
        city = serializers.CharField(max_length=30)

    def post(self, request: Request) -> Response:
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        profile = Profile.objects.create(
            user=request.user, **input_serializer.validated_data
        )
        output_serializer = self.OutputSerializer(profile)

        return Response(output_serializer.data, status=HTTP_200_OK)


class ProfileUpdateApi(APIView):
    permission_classes = (IsAuthenticated,)

    class InputSerializer(serializers.Serializer):
        first_name = serializers.CharField(max_length=30)
        last_name = serializers.CharField(max_length=30)
        country = serializers.CharField(max_length=30)
        description = serializers.CharField(max_length=255, required=False)
        city = serializers.CharField(max_length=30)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        first_name = serializers.CharField(max_length=30)
        last_name = serializers.CharField(max_length=30)
        country = serializers.CharField(max_length=30)
        description = serializers.CharField(max_length=255, required=False)
        city = serializers.CharField(max_length=30)

    def put(self, request: Request, profile_id: int) -> Response:
        profile = get_object_or_404(Profile, id=profile_id)
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        profile.update(**input_serializer.validated_data)
        output_serializer = self.OutputSerializer(profile)

        return Response(output_serializer.data, status=HTTP_200_OK)
