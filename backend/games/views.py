from django.shortcuts import render
from .models import Game


class Games:

    def get_all_games(request):
        all_games = Game.objects.all()
        for i in all_games:
            print(f"{i.title} {type(i)}")
        return render(request,'all_games.html',context={'games':all_games})
    

    def game_info(request,game_id:int):
        game = Game.objects.get(id=game_id)
        return render(request,'game_info.html', context={'game':game})