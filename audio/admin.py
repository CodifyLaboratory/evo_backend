from django.contrib import admin

from django.contrib import admin

from .models import Category, Audio


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'picture', 'audio_file']
