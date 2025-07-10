from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm , UserLoginForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate , login



class Auth:

    def register(request):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = User.objects.create_user(username=cd['UserName'], email =cd['Email'], password=cd['Password'])

                # set first and last name for user
                user.first_name = cd['FirstName']
                user.last_name = cd['LastName']

                messages.success(request,f"User {cd['UserName']} registered successfully!")

                return HttpResponse("registeres")
        else:
            form= UserRegisterForm()

        return render(request,'register.html',context={'form':form})
    

    def login(request):
        if request.method == "POST":
            form = UserLoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                # check user exists
                user = authenticate(request,username=cd['UserName'] , password=cd['Password'])
                if user != None:
                    # login user
                    login(request,user)

                    messages.info(request ,f"Welcome Dear {cd['Username']}!")

                    return redirect('home')
                else:
                    messages.error(request ,'User is not exists !')

                    return redirect('home')
        
        else:
            form = UserLoginForm()
            
        return render(request,'login.html',context={'form':form})



