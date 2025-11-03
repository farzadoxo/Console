from django.shortcuts import render
from .models import Platform , PlatformTrick
from django.shortcuts import render , redirect
from django.core.exceptions import ObjectDoesNotExist
from core.messages import MessageMaker as Message 
from .forms import NewPlatformTrickForm
from django.contrib.auth.models import User
from datetime import datetime


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
    


    def new_trick(request,pl_id:int):
        if request.method == 'POST':
            try:
                platform = Platform.objects.get(id=pl_id)
            except ObjectDoesNotExist:
                Message.Platforms.platform_does_not_exist(request)
                return redirect('platforms:all')
            
            if request.user.is_authenticated:
                form = NewPlatformTrickForm(request.POST    )
                if form.is_valid():
                    cd = form.cleaned_data
                    creator = User.objects.get(id=request.user.id)

                    pl_tr = PlatformTrick.objects.create(title=cd['title'],
                                                 description=cd['description'],
                                                 platform=platform,
                                                 creator=creator,
                                                 createdAt=datetime.now())
                    pl_tr.save()


                    Message.Platforms.platform_trick_created(request)
                    return redirect('home:home')  
            
            else:
                Message.Core.login_please(request)
                return redirect('home:home')
            
        else:
            form = NewPlatformTrickForm()

        return render(request,'platform_new_trick.html',context={'form':form})



            


