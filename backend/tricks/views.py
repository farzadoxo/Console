
from .models import Trick
from core.messages import MessageMaker as Message
from rest_framework.viewsets import ModelViewSet
from .serializers import TrickSerializer
from .models import Trick
from rest_framework.decorators import action
from .serializers import Trick
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated , AllowAny

class TrickViewSet(ModelViewSet):
    serializer_class = TrickSerializer
    queryset = Trick.objects.all()


    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return [AllowAny()]
    


    def perform_create(self, serializer):
        print("USER:", self.request.user)
        print("AUTH:", self.request.auth)
        serializer.save(creator=self.request.user)


    @action(detail=False, methods=['GET'], url_path='by-game/(?P<game_id>[^/.]+)')
    def by_games(self, request, game_id):
        tricks = Trick.objects.filter(game__id=game_id)
        serializer = TrickSerializer(tricks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], url_path='by-creator/(?P<creator_id>[^/.]+)')
    def by_creator(self, request, creator_id):
        tricks = Trick.objects.filter(creator__id=creator_id)
        serializer = TrickSerializer(tricks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    

