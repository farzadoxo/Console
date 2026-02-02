from rest_framework.viewsets import ModelViewSet
from .models import GameTrick , PlatformTrick
from rest_framework.decorators import action
from .serializers import GameTrickSerializer , PlatformTrickSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated , AllowAny




class GameTrickViewSet(ModelViewSet):
    serializer_class = GameTrickSerializer
    queryset = GameTrick.objects.all()


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
        tricks = GameTrick.objects.filter(game__id=game_id)
        serializer = GameTrickSerializer(tricks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], url_path='by-creator/(?P<creator_id>[^/.]+)')
    def by_creator(self, request, creator_id):
        tricks = GameTrick.objects.filter(creator__id=creator_id)
        serializer = GameTrickSerializer(tricks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class PlatformTrickViewSet(ModelViewSet):
    serializer_class = PlatformTrickSerializer
    queryset = PlatformTrick.objects.all()


    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated]
        return [AllowAny]
    
    def perform_create(self, serializer):
        print("USER:", self.request.user)
        print("AUTH:", self.request.auth)
        serializer.save(creator=self.request.user)


    
    @action(detail=False, methods=['GET'] ,url_path='by-plat/(?P<plat_id>[^/.]+)')
    def by_plat(self,request,plat_id:int):
        tricks = PlatformTrick.objects.filter(platform__id = plat_id)
        serializer = PlatformTrickSerializer(tricks, many=True)
        return Response(data=serializer.data , status=status.HTTP_200_OK)
    

    @action(detail=False,methods=['GET'],url_path='by-creator/(?P<creator_id>[^/.]+)')
    def by_creator(self,request,creator_id:int):
        tricks = PlatformTrick.objects.filter(creator__id=creator_id)
        serializer = PlatformTrickSerializer(tricks , many=True)
        return Response(data=serializer.data , status=status.HTTP_200_OK)
    