from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from tricks.models import Trick


class Home:
    """
        This class provide some function to work with website
        this class is the main class of project :)
    """



    """ MAIN """
    def home(request):
        return render(request,'index.html')
    



    

    """ Gets and Filters """
    def show_profile(request,user_id):
        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            messages.error(request,"User doesn't exixts !",extra_tags='error')

        # get user tricks 
        tricks = Trick.objects.filter(creator__id = user_id)
        return render(request,'show_profile.html',context={'user':user ,
                                                            'tricks':tricks})
        
