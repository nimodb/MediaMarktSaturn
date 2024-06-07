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
