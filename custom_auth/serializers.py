from rest_framework import serializers
from .models import User
from typing import Any


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "password_confirm", "role"]
        extra_kwargs = {
            "password": {"write_only": True},
            "password_confirm": {"write_only": True},
            "role": {"write_only": True},
        }

    id = serializers.UUIDField(default=None, read_only=True)
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    password_confirm = serializers.CharField(max_length=128, write_only=True)
    role = serializers.CharField(max_length=10, write_only=True)

    def create(self, validated_data: dict[str, Any]) -> User:
        if validated_data["password"] != validated_data["password_confirm"]:
            raise serializers.ValidationError("Passwords do not match")

        del validated_data["password_confirm"]

        if validated_data["role"] not in ["ADMIN", "AUTH", "USER"]:
            raise serializers.ValidationError("Invalid role")

        return (
            User.objects.create_superuser(**validated_data)
            if validated_data["role"] == "ADMIN"
            else User.objects.create_user(**validated_data)
        )

    def update(self, instance: User, validated_data: dict[str, Any]) -> User:
        if validated_data["password"] != validated_data["password_confirm"]:
            raise serializers.ValidationError("Passwords do not match")

        del validated_data["password_confirm"]

        if validated_data["role"] not in ["ADMIN", "AUTH", "USER"]:
            raise serializers.ValidationError("Invalid role")

        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.role = validated_data.get("role", instance.role)
        instance.password(validated_data.get("password", instance.password))
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.is_admin = validated_data.get("is_admin", instance.is_admin)

        instance.save()
        return instance
