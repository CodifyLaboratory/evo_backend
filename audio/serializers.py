from rest_framework import serializers

from .models import Audio, Category, FavoriteAudio


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'icon')


class AudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Audio
        fields = ('id', 'category', 'name', 'audio_file', 'picture')


class CategoryDetailSerializer(serializers.ModelSerializer):
    audios = AudioSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'icon', 'audios')


class AudioListSerializer(serializers.ModelSerializer):

    category = CategoryListSerializer(read_only=True, many=False)

    class Meta:
        model = Audio
        fields = ('id', 'category', 'name', 'audio_file', 'picture')


class FavoriteAudioListSerializer(serializers.ModelSerializer):
    audio = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = FavoriteAudio
        fields = ('id', 'user', 'status', 'audio')
        read_only_fields = ['user', ]

    def create(self, validated_data):
        status, _ = FavoriteAudio.objects.update_or_create(
            user=validated_data.get('user', None),
            audio=validated_data.get('audio', None),
            defaults={'status': validated_data.get('status')}
        )
        return status
