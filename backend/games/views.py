from django.shortcuts import render
from .models import Game

class Games:

    def get_all_games(request):
        all_games = Game.objects.all()
        return render(request,'all_games.html',context={'games':all_games})