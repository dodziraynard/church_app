from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from . models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "mobile"]

# User Serializeer
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "is_superuser", "profile"]

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        validated_data.pop('id', None)
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password:
            user.set_password(password)
            user.save()
            profile = Profile.objects.create(user=user)
        return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
