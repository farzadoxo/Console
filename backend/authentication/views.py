from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm , UserLoginForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import login , authenticate , logout
from django.core.exceptions import ObjectDoesNotExist
from core.messages import MessageMaker as Message
from .extentions import password_checker
from django.http import HttpResponse , JsonResponse
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.authentication import BaseAuthentication , SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class RegisterApiView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



class LoginApiView(APIView):
    ...



class AccountInfoApiView(APIView):
    ...



# class Auth:

#     def register(request):
#         if request.method == 'POST':
#             form = UserRegisterForm(request.POST)
            
#             if form.is_valid():
#                 if password_checker(password=form.cleaned_data['password']):
#                     # Check user exist or not
#                     if User.objects.filter(email=form.cleaned_data['email']).count() == 0:
#                         if User.objects.filter(username=form.cleaned_data['username']).count() == 0:
#                             try:

#                                 # Create and save user
#                                 cd = form.cleaned_data
#                                 user = User.objects.create_user(username=cd['username'], email =cd['email'], password=cd['password'])
#                                 user.first_name = cd['firstname']
#                                 user.last_name = cd['lastname']
#                                 user.save()

#                                 # Show message and return 
#                                 Message.Auth.user_registred_success(request,cd['username'])
#                                 return redirect('home:home')

#                             except Exception as e:
#                                 # Show ERROR and return
#                                 Message.Core.error(request,e)
#                                 return redirect('authentication:register')

#                         else:
#                             Message.Auth.username_taken(request)
#                             return redirect('home:home')

#                     else:
#                         Message.Auth.email_used_before(request)
#                         return redirect('home:home')
#                 else:
#                     Message.Auth.password_invalid(request)
#                     return redirect('authentication:register')
            
#         else:
#             # Set request method to: GET
#             form= UserRegisterForm()
#         # Render html file
#         return render(request,'register.html',context={'form':form})


#     def login(request):
#         if request.method == 'POST':
#             form = UserLoginForm(request.POST)
#             if form.is_valid():
#                 cd = form.cleaned_data
#                 user = authenticate(request,username=cd['username'] , password=cd['password'])
#                 if user != None:
#                     login(request,user)

#                     Message.Auth.login_success(request,username=cd['username'])
#                     return redirect('home:home')
                
#                 else:
#                     Message.Auth.pass_or_user_invalid(request)
#                     return redirect('home:home')
                
#         else:
#             form = UserLoginForm()
    
#         return render(request,'login.html',context={'form':form})



#     def logout(request):
#         if request.user.is_authenticated:
#             logout(request)
#             Message.Auth.user_logedout(request)
#             return redirect('home:home')
#         else:
#             Message.Auth.no_one_logedin(request)
#             return redirect('home:home')
