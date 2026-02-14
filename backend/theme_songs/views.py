from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import GameThemeSong
from .serializers import GameThemeSongSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status




class GameThemeSongViewset(ReadOnlyModelViewSet):
    queryset = GameThemeSong.objects.all()
    serializer_class = GameThemeSongSerializer


    @action(detail=False,methods=['GET'],url_path='game/(?P<game_id>[^/.]+)')
    def byGame(self,reqeust,game_id):
        songs = GameThemeSong.objects.filter(game__id = game_id)
        serializer = GameThemeSongSerializer(songs,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)