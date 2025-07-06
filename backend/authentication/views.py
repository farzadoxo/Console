from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.contrib import messages
from django.http import HttpResponse


class Auth:

    def register(request):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = User.objects.create_user(username=cd['UserName'], email =cd['Email'], password=cd['Password'])

                messages.info(request,f"User {cd['UserName']} registered successfully!")

                return HttpResponse("registeres")
        else:
            form= UserRegisterForm()

        return render(request,'register.html',context={'form':form})



