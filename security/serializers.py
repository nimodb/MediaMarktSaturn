from django.contrib.auth.models import User
from rest_framework import serializers
from .models import SecurityRecord


class SecurityRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityRecord
        fields = ["id", "name", "description"]

    def validate(self, attrs):
        # validate name
        name = attrs.get("name", "")
        if len(name) < 5:
            raise serializers.ValidationError(
                "Name must be at least 5 characters long."
            )

        # validate description
        description = attrs.get("description", "")
        if len(description) < 10:
            raise serializers.ValidationError(
                "Description must be at least 10 characters long."
            )
        return super().validate(attrs)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user
