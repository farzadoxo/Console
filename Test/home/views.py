from django.shortcuts import render
from .models import User , Book
from django.http import HttpResponse
from django.shortcuts import render , redirect
from .forms import CreateUserForm , UpdateUserForm
import random
# Create your views here.

def home(request):
    all_user = User.objects.all()    
    return render(request,'index.html',context={'users':all_user})



#def user_info(request,user_id:int):
#    user = User.objects.get(id=user_id)
#    return render(request,'user.html',context={'user':user})

def user_info(request,user_id:int):
    user = User.objects.get(id=user_id)
    return render(request,'user.html',context={'user':user})


def delete_user(request,user_id:int):
    user = User.objects.get(id=user_id)
    if user:
        user.delete()
        return redirect('home')
    else:
        return "User does'nt exists!8"


def create_user(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            User.objects.create(id=random.randint(1,500),FullName=form.cleaned_data['FullName'],Email=form.cleaned_data['Email'])
            return redirect('home')
    else:
        form = CreateUserForm()
    return render(request , 'create.html' , context={'form':form})




def update_user(request,user_id:int):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'userinfo',user_id)
    else:
        form = UpdateUserForm(instance=user)

    return render(request,'update.html',context={'form':form})