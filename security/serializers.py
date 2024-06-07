from rest_framework import serializers
from .models import SecurityRecord


class SecurityRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityRecord
        fields = ["id", "name", "description"]
