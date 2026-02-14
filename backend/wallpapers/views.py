from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import GameWallpaper , PlatformWallpaper
from .serializers import GameWallpaperSerializer , PlatformWallpaperSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status



class GameWallpaperViewset(ReadOnlyModelViewSet):
    queryset = GameWallpaper.objects.all()
    serializer_class = GameWallpaperSerializer


    @action(detail=False,methods=['GET'],url_path='game/(?P<game_id>[^/.]+)')
    def byGame(self,request,game_id):
        wallpapers = GameWallpaper.objects.filter(game__id=game_id)
        serializer = GameWallpaperSerializer(wallpapers,many=True)

        return Response(serializer.data , status=status.HTTP_200_OK)




class PlatformWallpaperViewset(ReadOnlyModelViewSet):
    queryset = PlatformWallpaper.objects.all()
    serializer_class = PlatformWallpaperSerializer


    @action(detail=False,methods=['GET'],url_path='platform/(?P<plat_id>[^/.]+)')
    def byPlatform(self,request,plat_id):
        wallpapers = PlatformWallpaper.objects.filter(platform__id=plat_id)
        serializer = PlatformWallpaperSerializer(wallpapers,many=True)

        return Response(serializer.data , status=status.HTTP_200_OK)