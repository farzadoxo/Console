from django.shortcuts import render
from .models import Game , Genre , Publisher , ESRB


class Games:
    """"""

    def get_games_by_genre(request,genre_id:int):
        genres = Genre.objects.get(id=genre_id)
        if genres != None:
            games = Game.objects.filter(genre__id = genre_id)

            return render(request,'game_by.html',context={'games':games , 'title':"Genre"})


    def get_games_by_publisher(request,publisher_id:int):
        publisher = Publisher.objects.get(id=publisher_id)
        if publisher != None:
            games = Game.objects.filter(publisher__id = publisher_id)

            return render(request,'game_by.html',context={'games':games,'title':"Publisher"})
        
    
    def get_games_by_esrb(request,esrb_sign:str):
        esrb = ESRB.objects.get(sign=esrb_sign)
        if esrb != None:
            games = Game.objects.filter(esrb__id = esrb.id)

            return render(request,'game_by.html', context={'games':games , 'title':"ESRB"})
        



    def get_all_games(request):
        all_games = Game.objects.all()
        return render(request,'all_games.html',context={'games':all_games})
    

    def game_info(request,game_id:int):
        game = Game.objects.get(id=game_id)
        return render(request,'game_info.html', context={'game':game})