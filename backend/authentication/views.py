from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm , UserLoginForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import login , authenticate , logout
from django.core.exceptions import ObjectDoesNotExist
from core.messages import MessageMaker as Message
from extentions import password_checker


class Auth:

    def login(request):
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(request,username=cd['username'] , password=cd['password'])
                if user != None:
                    login(request,user)

                    Message.Auth.login_success(request,username=cd['username'])
                    return redirect('home:home')
                
                else:
                    Message.Auth.pass_or_user_invalid(request)
                    return redirect('home:home')
                
        else:
            form = UserLoginForm()
        
        return render(request,'login.html',context={'form':form})



    def logout(request):
        if request.user.is_authenticated:
            logout(request)
            Message.Auth.user_logedout(request)
            return redirect('home:home')
        else:
            Message.Auth.no_one_logedin(request)
            return redirect('home:home')
