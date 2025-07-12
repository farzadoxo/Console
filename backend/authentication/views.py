from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm , UserLoginForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import login , authenticate , logout



class Auth:

    def register(request):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                try:
                    # Create and save user
                    cd = form.cleaned_data
                    user = User.objects.create_user(username=cd['UserName'], email =cd['Email'], password=cd['Password'])
                    user.first_name = cd['FirstName']
                    user.last_name = cd['LastName']
                    user.save()
                    
                    # Show message and return 
                    messages.info(request,f"User {cd['UserName']} registered successfully!")
                    return redirect('home')
                
                except Exception as e:
                    # Show ERROR and return
                    messages.error(request , "{}".format(e))
                    return redirect('register')
  
            else:
                messages.error(request , "Form is not valid !")
                return redirect('register')
        else:
            # Set request method to: GET
            form= UserRegisterForm()
        # Render html file
        return render(request,'register.html',context={'form':form})
    


    def login(request):
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(request,username=cd['UserName'] , password=cd['Password'])
                if user != None:
                    login(request,user)

                    messages.success(request,f"Welcome dear {user.first_name}")

                    return redirect('home')
                else:
                    messages.error(request,"Your password or username is invalid !")
                    return redirect('home')
                
        else:
            form = UserLoginForm()
        
        return render(request,'login.html',context={'form':form})



    def logout(request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request,'User loged out successfully !')
            return redirect('home')
        else:
            messages.error(request,"No one's loged in!")
            return redirect('home')