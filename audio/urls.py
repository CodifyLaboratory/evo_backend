from django.urls import path
from .views import CategoryViewSet, AudioViewSet, FavoriteAudioViewSet, OwnFavoriteAudioViewSet

urlpatterns = [
    path('categories/', CategoryViewSet.as_view({'get': 'list'})),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve'})),

    path('audios/', AudioViewSet.as_view({'get': 'list'})),

    path('favorite/create/<int:pk>/', FavoriteAudioViewSet.as_view({'post': 'create'})),
    path('favorite/edit/<int:pk>/', FavoriteAudioViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('favorite/delete/<int:pk>/', FavoriteAudioViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('favorite/<int:pk>/', FavoriteAudioViewSet.as_view({'get': 'retrieve'})),

    path('favorite-audios/', OwnFavoriteAudioViewSet.as_view({'get': 'list'})),
    ]