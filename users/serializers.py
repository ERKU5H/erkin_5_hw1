from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import UserConfirm


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField( write_only=True)


class UserConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserConfirm
        fields = ['code']
