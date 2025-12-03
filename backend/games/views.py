
from .models import Game
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import GameSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status




class GamesViewSet(ReadOnlyModelViewSet):

    serializer_class = GameSerializer
    queryset = Game.objects.all()


    @action(detail=False, methods=['get'], url_path='genre/(?P<genre_id>[^/.]+)')
    def byGenre(self, request, genre_id=None):
        games = Game.objects.filter(genre__id=genre_id)
        serialized = GameSerializer(games, many=True)

        return Response(serialized.data, status=status.HTTP_200_OK)
    


    @action(detail=False,methods=['GET'],url_path='pub/(?P<pub_id>[^/.]+)')
    def byPublisher(self,request,pub_id=None):
        games = Game.objects.filter(publisher__id=pub_id)
        serialized = GameSerializer(games,many=True)

        return Response(serialized.data , status=status.HTTP_200_OK)
    

    @action(detail=False,methods=['get'],url_path='esrb/(?P<esrb>[^/.]+)')
    def byEsrb(self,request,esrb=None):
        games = Game.objects.filter(esrb__sign=esrb)
        serialized = GameSerializer(games,many=True)

        return Response(serialized.data , status=status.HTTP_200_OK)
