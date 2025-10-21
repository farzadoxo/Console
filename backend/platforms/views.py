from django.shortcuts import render
from .models import Platform 
from django.shortcuts import render , redirect
from django.core.exceptions import ObjectDoesNotExist
from core.messages import MessageMaker as Message 


class Platforms:

    def get_all_platforms(request):

        platforms = Platform.objects.all()
        return render(request,'all_platforms.html',context={'platforms':platforms})


    def show_platform(request,platform_id:str):
        try:
            platform = Platform.objects.get(id=platform_id)
        except ObjectDoesNotExist:
            Message.Platforms.platform_does_not_exist(request)
            return redirect('platforms:all')

        return render(request,'show_platform.html',context={'platform':platform})



            


