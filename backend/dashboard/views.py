from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from tricks.models import Trick
from .forms import UpdateUserAccount , UpdateUserProfile



class Dash:
    """"
        This class provid some functions and methods to do some
        action or show data of users and its a user management panel.
    """



    """ Gets and Fiilters """
    def my_profile(request,user_id:int):
        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            messages.error(request,"User doesn't exists!",extra_tags='error')

    
        if request.user.is_authenticated:
            if request.user.username == user.username:
                tricks = Trick.objects.filter(creator__id = user_id)

                return render(request,'my_profile.html' , context={
                    'user':user,
                    'tricks': tricks
                })
            
            else:
                messages.warning(request,"Dont do this again!",extra_tags='warning')
                return redirect('home')
        else:
            messages.warning(request,"Please login first!",extra_tags='warning')
            return redirect('home')


    def edit_user_account(request,user_id:int):
        ...


    def favorit_games(request,user_id:int):
        ...

    
    def saved_tricks(request,user_id:int):
        ...

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
                



    

    
        

