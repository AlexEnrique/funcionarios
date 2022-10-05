from rest_framework import serializers

from .models import Enterprise


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    empresa = serializers.CharField(max_length=255)
    senha = serializers.CharField(max_length=255, min_length=8)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    senha = serializers.CharField(max_length=255, min_length=8)


class EnterpriseSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(source="user.email")

    class Meta:
        model = Enterprise
        exclude = ["user"]