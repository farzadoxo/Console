from django.shortcuts import render , redirect
from games.models import Game
from .models import Trick
from django.contrib import messages
from .forms import NewTrickForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime


class Tricks:
    """
        This class provide some function to work with Trciks
        like create new trick , get tricks from database ,
        applying changes on tricks , filter , delete , etc.

    """


    """ Gets and filters trick """
    def get_all_tricks(request):
        tricks = Trick.objects.all()
        return render(request,'all_tricks.html',context={'tricks':tricks})


    def get_tricks_by_game(request,game_id:int):
        game = Game.objects.get(id=game_id)
        if game != None:
            tricks = Trick.objects.filter(game__id = game.id)

            return render(request,'tricks_by.html',context={'tricks':tricks , 'title':f"{game.title}"})
        else:
            messages.error(request,"This game doesn't exists!",extra_tags='error')


    def get_tricks_by_creator(request,creator_id:int):
        try:
            # get user and tricks 
            creator = User.objects.get(id=creator_id)
            tricks = Trick.objects.filter(creator__id = creator.id)
            return render(request,'tricks_by.html',context={'tricks':tricks,'title':f"{creator.username}"})
        
        except ObjectDoesNotExist:
            messages.error(request,"User Not Found!",extra_tags='error')
            return redirect('home')
        

        

    """ Modifying tricks """
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
                                                 creator=creator,
                                                 createdAt=datetime.now())
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
        

    


    """ Actions on tricks """
    def show_trick(request,trick_id:int):
        trick = Trick.objects.get(id=trick_id)
        return render(request,'show_trick.html',context={'trick':trick})

    