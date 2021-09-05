from django.db import models
from evo import settings


class Category(models.Model):
    name = models.CharField(max_length=155, verbose_name='Желание')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    icon = models.ImageField(upload_to='category-icons/', null=True, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Плейлист'
        verbose_name_plural = 'Плейлисты'

    def __str__(self):
        return self.name


class Audio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='audios', null=True,
                                 verbose_name='Категория')
    name = models.CharField(verbose_name='Название', max_length=255)
    audio_file = models.FileField(upload_to='audio-files/', null=True, blank=True, verbose_name='Аудиофайл')
    picture = models.ImageField(upload_to='audio-images/', null=True, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Аудиомедитация'
        verbose_name_plural = 'Аудиомедитации'

    def __str__(self):
        return self.name


class FavoriteAudio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь',
                             related_name='favorite_audios')
    status = models.BooleanField(verbose_name='Статус')
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, verbose_name='Аудиомедитация', related_name='favorites')

    class Meta:
        verbose_name = 'Избранные аудио'
        verbose_name_plural = 'Избранные аудио'

    def __str__(self):
        return '{}'.format(self.user)
