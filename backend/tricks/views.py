from django.shortcuts import render
from games.models import Game
from .models import Trick
from django.contrib import messages
from .forms import NewTrickForm

class Tricks:

    def get_all_tricks(request):
        ...


    def get_tricks_by_game(request,game_id:int):
        game = Game.objects.get(id=game_id)
        if game != None:
            tricks = Trick.objects.filter(game__id = game.id)

            return render(request,'game_tricks.html',context={'tricks':tricks , 'game_name':game.title})
        else:
            messages.error(request,"This game doesn't exists!",extra_tags='error')
        


    def new_trick(request):
        if request.method == 'POST':
            if request.user.is_authenticated:
                form = NewTrickForm(request.POST)
                
                if form.is_valid():
                    cd = form.cleaned_data
                    trick = Trick.objects.create(title=cd['title'],descreption=cd['descreption'],game=['game'],creator=request.user.id)
                    trick.save()

                    # TODO : COMPLETE THIS ENDPOINT

        else:
            form = NewTrickForm()

        return render(request,'new_trick.html',context={'form':form})

    