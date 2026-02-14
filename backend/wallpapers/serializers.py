from rest_framework.serializers import ModelSerializer
from .models import GameWallpaper , PlatformWallpaper


class GameWallpaperSerializer(ModelSerializer):
    class Meta:
        model= GameWallpaper
        fields= '__all__'




class PlatformWallpaperSerializer(ModelSerializer):
    class Meta:
        model= PlatformWallpaper
        fields= '__all__'