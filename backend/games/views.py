
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





# class Games:
#     """
#         This class provide some function and services to work with Games , Platforms , Genres , ESRB and etc 
#         for example create a game , get games and filter them , modifying and applying changs on games application.
#     """




#     """ Gets and Filters """
#     def get_games_by_genre(request,genre_id:int):
#         try:
#             genre = Genre.objects.get(id=genre_id)
#         except ObjectDoesNotExist:
#             Message.Games.genre_code_invalid(request)
#             return redirect('home:home')
        
#         games = Game.objects.filter(genre__id = genre.id)
#         return render(request,'game_by.html',context={'games':games , 'title':"Genre"})




#     def get_games_by_publisher(request,publisher_id:int):
#         try:
#             publisher = Publisher.objects.get(id=publisher_id)
#         except ObjectDoesNotExist:
#             Message.Games.publisher_code_invalid(request)
#             return redirect('home:home')
        
#         games = Game.objects.filter(publisher__id = publisher.id)
#         return render(request,'game_by.html',context={'games':games,'title':"Publisher"})




#     def get_games_by_esrb(request,esrb_sign:str):
#         try:
#             esrb = ESRB.objects.get(sign=esrb_sign.upper())
#         except ObjectDoesNotExist:
#             Message.Games.esrb_sign_invalid(request)
#             return redirect('home:home')
        
#         games = Game.objects.filter(esrb__id = esrb.id)
#         return render(request,'game_by.html', context={'games':games , 'title':"ESRB"})
        



#     def get_all_games(request):
#         all_games = Game.objects.all()
#         return render(request,'all_games.html',context={'games':all_games})





#     """ Action on games"""
#     def game_info(request,game_id:int):
#         try:
#             game = Game.objects.get(id=game_id)
#         except ObjectDoesNotExist:
#             Message.Games.game_does_not_exist(request)
#             return redirect('games:get_all_games')
        
#         game = Game.objects.get(id=game_id)
#         return render(request,'game_info.html', context={'game':game})
