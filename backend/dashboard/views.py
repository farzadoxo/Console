from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from tricks.models import Trick
from .forms import UpdateUserAccount , UpdateUserProfile , UpdateUserAccount
from games.models import Game
from .models import FavoritGame , SavedTrick
from django.contrib.auth import logout

class Dash:
    """"
        This class provid some functions and methods to do some
        action or show data of users and its a user management panel.
    """
    

    """ User profile and account """
    def my_profile(request):
        if request.user.is_authenticated:
            return render(request,'my_profile.html',context={'trick_count':Trick.objects.filter(creator__id = request.user.id).count()})
            
        else:
            messages.warning(request,"Please login first!",extra_tags='warning')
            return redirect('home:home')




    def delete_account(request):
        if request.user.is_authenticated:
            try:
                user = User.objects.get(id=request.user.id)
                user.delete()
                logout(request)

                messages.success(request,"Your account deleted !",'success')
                return redirect('home:home')
            except Exception as error:
                messages.error(request,"Somthing went wrong !",'danger')
                return redirect('home:home')
            
    
    def my_tricks(request):
        if request.user.is_authenticated:
            user_tricks = Trick.objects.filter(creator__id=request.user.id)
            return render(request,'my_tricks.html',context={'tricks':user_tricks})
        else:
            messages.warning(request,"Please login first!",extra_tags='warning')
            return redirect('home:home')





    def edit_user_profile(request):
        if request.method == "POST":
            if request.user.is_authenticated:
                try:
                    user = User.objects.get(id=request.user.id)
                except ObjectDoesNotExist:
                    messages.error(request,"User doesn't exists!",extra_tags='error')
                    
        

                    form = UpdateUserProfile(request.POST,instance=user)

                    if form.is_valid():
                        user.first_name = form.FirstName
                        user.last_name = form.LastName

                        user.save()
            else:
                messages.warning(request,"Please login first!",extra_tags='warning')
                return redirect('dashboard:my_prifile')
        else:
            form = UpdateUserProfile(instance=user)
        
        return render(request,'update_user_profile.html',context={'form':form})
    




    def edit_user_account(request):
        if request.user.is_authenticated:
            if request.method == 'POST':
                try:
                    user = User.object.get(id=request.user.id)
                except ObjectDoesNotExist:
                    message.error(request,"User Doesn't exists!",extra_tags='warning')


                form = UpdateUserAccount(request.POST,instance=user)
                if form.is_valid():
                    user.username = form.username
                    user.email = form.email

                    user.save()

            else:
                form = UpdateUserAccount(instance=user)


        else:
            message.warning(request,"Please login first!",extra_flags='warning')
            return redirect('home:home')


        return render(request,'update_user_account.html',contex={'form':form})






    

    """ Favorite games """

    def get_user_favorit_games(request):

        if request.user.is_authenticated:
            fav_games = FavoritGame.objects.filter(user__id = request.user.id)
 
            return render(request,'favorit_games.html',context={'fav_games':fav_games})
        
        else:
            messages.warning(request,"Please login first!",extra_tags='warning')
            return redirect('home:home')
        


    def add_favorit_games(request,game_id):
        if request.user.is_authenticated:
            try:
                game = Game.objects.get(id=game_id)
                user_fav_games = FavoritGame.objects.get(game__id = game.id , user__id = request.user.id)
            except ObjectDoesNotExist:
                favorit_game = FavoritGame.objects.create(user=request.user ,game=game)
                favorit_game.save()

                messages.success(request,f"{game.title} added to your favorit games :)",extra_tags='success')
                return redirect('dashboard:my_favorite_games')
            

            messages.success(request,"This game added to your favorite games befor!!!",extra_tags='warning')
            return redirect('games:get_all_games')
 
        else:
            messages.warning(request,"Please login first!",extra_tags='warning')
            return redirect('games:get_all_games')
        


    def delete_favorite_game(request,game_id:int):
        if request.user.is_authenticated:
            try:
                game = FavoritGame.objects.filter(user__id = request.user.id , game__id = game_id)
                game.delete()
                
                messages.success(request,"Favorite game deleted!",'success')
                return redirect('dashboard:my_favorite_games')
                    
            except Exception as error:
                messages.success(request,f"somthing went wrong! : {error}",'danger')
                return redirect('dashboard:my_favorite_games')
        
        else:
            messages.warning(request,"Please login first!",extra_tags='warning')
            return redirect('home:home')



        
        

    """ Saved tricks """
    def add_saved_tricks(request,trick_id:int):
        if request.user.is_authenticated:
            try:
                trick = Trick.objects.get(id=trick_id)
                user_saved_tricks = SavedTrick.objects.get(trick__id = trick.id , user__id = request.user.id)
            except ObjectDoesNotExist:
                saved_trick = SavedTrick.objects.create(user=request.user , trick=trick)
                saved_trick.save()

                messages.success(request,"Trick saved successfully!",extra_tags="success")
                return redirect('dashboard:my_saved_tricks')
            

            messages.error(request,"This trick saved before!",extra_tags='warning')
            return redirect('tricks:get_all_tricks')

        else:
            messages.warning(request,"Please login first!",extra_tags='danger')
            return redirect('tricks:get_all_tricks')



    def get_user_saved_tricks(request):
        if request.user.is_authenticated:
            saved_tricks = SavedTrick.objects.filter(user__id = request.user.id)

            return render(request,'saved_tricks.html',context={'saved_tricks':saved_tricks})

        else:
            messages.warning(request,"Please login first!",extra_tags='warning')
            return redirect('home:home')
            


    def delete_saved_trick(request,trick_id):
        if request.user.is_authenticated:
            try:
                trick = SavedTrick.objects.filter(user__id = request.user.id , trick__id = trick_id)
                trick.delete()

                messages.success(request,f"Saved Trick deleted!",'success')
                return redirect('dashboard:my_saved_tricks')

            except Exception as error:
                messages.error(request,f"Somthing went wrong! : {error}",extra_tags='error')
                return redirect('home:home')
        else:
            messages.warning(request,"Please login first!",extra_tags='warning')
            return redirect('home:home')
