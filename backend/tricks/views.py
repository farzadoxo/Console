from django.shortcuts import render , redirect
from games.models import Game
from .models import Trick
from django.contrib import messages
from .forms import NewTrickForm , UpdateTrickForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from dashboard.models import SavedTrick


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
        try:
            game = Game.objects.get(id=game_id)
        except ObjectDoesNotExist:
            messages.error(request,"This game doesn't exists!",extra_tags='danger')
            return redirect('home:home')
        
        tricks = Trick.objects.filter(game__id = game.id)
        return render(request,'tricks_by.html',context={'tricks':tricks , 'title':f"{game.title}"})

            


    def get_tricks_by_creator(request,creator_id:int):
        try:
            # get user and tricks 
            creator = User.objects.get(id=creator_id)
            tricks = Trick.objects.filter(creator__id = creator.id)
            return render(request,'tricks_by.html',context={'tricks':tricks,'title':f"{creator.username}"})
        
        except ObjectDoesNotExist:
            messages.error(request,"User Not Found!",extra_tags='danger')
            return redirect('home:home')
        


    


    """ Actions on tricks """
    def show_trick(request,trick_id:int):
        trick = Trick.objects.get(id=trick_id)
        return render(request,'show_trick.html',context={'trick':trick})

    



    """ Modifying tricks """
    def new_trick(request,game_id:int):
        if request.method == 'POST':
            if request.user.is_authenticated:
                form = NewTrickForm(request.POST)
                
                if form.is_valid():

                    # get usefull data
                    cd = form.cleaned_data
                    game = Game.objects.get(id=game_id)
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
                    return redirect('home:home')
            
            else:
                messages.warning(request,"Please login first!",extra_tags='warning')
                return redirect('home:home')

        else:
            form = NewTrickForm()

        # render page
        form = NewTrickForm()
        return render(request,'new_trick.html',context={'form':form})
    

    
    
    def delete_trick(request,trick_id):
        try:
            trick = Trick.objects.get(id=trick_id)
        except ObjectDoesNotExist:
            messages.error(request,"Trick not found !",extra_tags='danger')
            return redirect('home:home')
        
        if request.user.is_authenticated:
            if request.user.username == trick.creator.username:
                saved = SavedTrick.objects.filter(trick__id = trick_id)
            # deleting trick
                trick.delete()
                saved.delete()
                messages.info(request,f"{trick.title} deleted!",extra_tags='info')
                return redirect('home:home')
            else:
                messages.warning(request,"You are not creator of this trick!!",'warning')
                return redirect('home:home')
        else:
            messages.warning(request,"Please login first!",extra_tags='warning')
            return redirect('home:home')




    # TODO : Solve instance problem later
    def update_trick(request,trick_id):
        try:
            trick = Trick.objects.get(id=trick_id)
        except ObjectDoesNotExist:
            messages.error(request,"Trick doesn't exists!",extra_tags='danger')
            return redirect('home:home')
        
        if request.method == 'POST':
            if request.user.is_authenticated:
                if request.user.username == trick.creator.username:
                    form = UpdateTrickForm(request.POST, instance=trick)

                    if form.is_valid():
                        form.save()
                        messages.success(request,"Trick updated successfully !",extra_tags='success')
                        return redirect('home:home')
                
                else:
                    messages.warning(request,'You are not creator of this trick !',extra_tags='warning')

            else:
                messages.warning(request,'Please login first !',extra_tags='warning')
                return redirect('home:home')
            
        else:
            form = UpdateTrickForm(instance=trick)
        

        return render(request , 'update_trick.html' , context={'form':form})
