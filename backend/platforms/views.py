from django.shortcuts import render
from .models import Platform 
from django.shortcuts import render , redirect
from django.core.exceptions import ObjectDoesNotExist
from core.messages import MessageMaker as Message 


class Platforms:

    def get_all_platforms(request):

        platforms = Platform.objects.all()
        return render(request,'all_platforms.html',contex={'platforms':platforms})


    def show_platform(request,Platform_id:str):
        try:
            platform = Platform.objects.get(id=Platform_id)
        except ObjectDoesNotExist:
            # TODO: some message 
            return redirect('home:home')

        return render(request,'show_platform.html',contex={'platform':platform})



            


