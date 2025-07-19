from django.shortcuts import render , redirect
from games.models import Game
from .models import Trick
from django.contrib import messages
from .forms import NewTrickForm
from django.contrib.auth.models import User


class Tricks:

    def get_all_tricks(request):
        tricks = Trick.objects.all()
        return render(request,'all_tricks.html',context={'tricks':tricks})


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

                    # get usefull data
                    cd = form.cleaned_data
                    game = Game.objects.get(id=cd['game'])
                    creator = User.objects.get(id=request.user.id)

                    # create trick and save it
                    trick = Trick.objects.create(title=cd['title'],
                                                 description=cd['description'],
                                                 game=game,
                                                 creator=creator)
                    trick.save()

                    # show message and redirect to home
                    messages.success(request,"Trick successfully created for {} Game!".format(game.title,creator.username))
                    return redirect('home')
            
            else:
                messages.warning(request,"Please login first!",extra_tags='warning')

        else:
            form = NewTrickForm()

        # render page
        form = NewTrickForm()
        return render(request,'new_trick.html',context={'form':form})

    