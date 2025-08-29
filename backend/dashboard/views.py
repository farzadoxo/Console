from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from tricks.models import Trick
from .forms import UpdateUserAccount , UpdateUserProfile
from games.models import Game
from .models import FavoritGame , SavedTrick

class Dash:
    """"
        This class provid some functions and methods to do some
        action or show data of users and its a user management panel.
    """



    """ Gets and Fiilters """
    def my_profile(request):
        if request.user.is_authenticated:
            return render(request,'my_profile.html')
            
        else:
            messages.warning(request,"Please login first!",extra_tags='warning')
            return redirect('home:home')
        
    

    
    def get_user_favorit_games(request):

        if request.user.is_authenticated:
            fav_games = FavoritGame.objects.filter(user__id = request.user.id)
 
            return render(request,'favorit_games.html',context={'fav_games':fav_games})
        
        else:
            messages.warning(request,"Please login first!",extra_tags='warning')
            return redirect('home:home')

        

    
    def get_user_saved_tricks(request):
        if request.user.is_authenticated:
            saved_tricks = SavedTrick.objects.filter(user__id = request.user.id)

            return render(request,'saved_tricks.html',context={'saved_tricks':saved_tricks})
        
        else:
            messages.warning(request,"Please login first!",extra_tags='warning')
            return redirect('home:home')
        


    


    """ Action """
    def edit_user_profile(request,user_id:int):
        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            messages.error(request,"User doesn't exists!",extra_tags='error')
        
        if request.method == "POST":
            if request.user.is_authenticated:
                if request.user.username == user.username:
                    form = UpdateUserProfile(request.POST)

                    if form.is_valid():
                        user.first_name = form.FirstName
                        user.last_name = form.LastName

                        user.save()
                    
                else:
                    ...
            else:
                ...
        else:
            form = UpdateUserProfile()
        

        return render(request,'update_user_profile.html',context={'form':form})
    



    # TODO: Fix this endpoint 
    def add_favorit_games(request,game_id):
        if request.user.is_authenticated:
            try:
                game = Game.objects.get(id=game_id)
            except ObjectDoesNotExist:
                messages.error(request , "Game does not exists!",extra_tags='error')

            user_fav_games = FavoritGame.objects.filter(game__id = game.id)
            if user_fav_games == None:
                favorit_game = FavoritGame.objects.create(user=request.user ,game=game)
                favorit_game.save()

                messages.success(request,f"{game.title} added to your favorit games :)",extra_tags='success')
                return redirect('games:game_info',game_id=game_id)
            
            else:
                messages.success(request,"This game added to your favorite games befor!!!",extra_tags='error')
                return redirect('games:game_info',game_id=game_id)
 
        else:
            messages.warning(request,"Please login first!",extra_tags='error')
            return redirect('games:game_info',game_id=game_id)

        
        


    
    def add_saved_tricks(request,trick_id:int):
        if request.user.is_authenticated:
            try:
                trick = Trick.objects.get(id=trick_id)
            except ObjectDoesNotExist:
                messages.error(request,"Trick does not exists!",extra_tags='eroor')

            
            saved_trick = Trick.objects.create(user=request.user , trick=trick)
            saved_trick.save()

            messages.success(request,"Trick saved successfully!",extra_tags="success")
            return redirect('home')
        



    def edit_user_account(request,trick_id:int):
        ...

                



    

    
        

