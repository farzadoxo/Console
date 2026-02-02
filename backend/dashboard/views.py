from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.views import APIView
from .serializers import FavoritGameSerializer , SavedGameTrickSerializer , ProfileSerializer
from .models import FavoritGame , SavedGameTrick
from rest_framework.exceptions import MethodNotAllowed
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from games.models import Game
from games.serializers import GameSerializer




class SavedTrickViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self,request):
        serializer = SavedGameTrickSerializer(data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def list(self,request):
        saved = SavedGameTrick.objects.filter(user = request.user)
        serializer = SavedGameTrickSerializer(saved,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    

    def retrieve(self,request,pk):
        trick = SavedGameTrick.objects.get(id=pk)
        if trick.user.id == request.user.id:
            serializer = SavedGameTrickSerializer(trick)

            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response("This saved trick is not for you!",status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PUT')
    
    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PATCH')




class FavoritGameViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]


    def create(self,request):
        serializer = FavoritGameSerializer(data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save(user=request.user)

            return Response(serializer.data,status=status.HTTP_201_CREATED)    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def list(self,request):
        fa_games = FavoritGame.objects.filter(user = request.user)
        serializer = FavoritGameSerializer(fa_games,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)


    def retrieve(self,request,pk):
        fa_game = FavoritGame.objects.get(id=pk)
        if fa_game.user.id == request.user.id:
            game = Game.objects.get(id=fa_game.game.id)
            serializer = GameSerializer(game)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response("This favorite games is not for you!")
    

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PUT')
    

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PATCH')
    



class UpdateProfileInfo(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self,request):
        serializer = ProfileSerializer(request.user,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)