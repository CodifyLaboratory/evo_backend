from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Category, Audio, FavoriteAudio
from .serializers import CategoryListSerializer, CategoryDetailSerializer, AudioListSerializer, \
    FavoriteAudioListSerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        elif self.action == 'retrieve':
            return CategoryDetailSerializer


class AudioViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Audio.objects.all()
    serializer_class = AudioListSerializer


class FavoriteAudioViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FavoriteAudioListSerializer
    queryset = FavoriteAudio.objects.all()

    def perform_create(self, serializer):
        audio = Audio.objects.get(id=self.kwargs['pk'])
        return serializer.save(user=self.request.user, audio=audio)


class OwnFavoriteAudioViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FavoriteAudioListSerializer

    def get_queryset(self):
        queryset = FavoriteAudio.objects.filter(user=self.request.user, status=True)
        return queryset