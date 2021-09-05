from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from .models import User
from audio.serializers import AudioListSerializer


class CustomUserCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'first_name', 'email', 'password']


class CustomUserSerializer(UserSerializer):
    favorite_audios = AudioListSerializer(many=True, read_only=True)

    class Meta(UserSerializer.Meta):
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'date_of_birth', 'gender',
            'country', 'city', 'avatar', 'favorite_audios']
