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
from .serializers import UserRegisterSerializer , UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.authentication import BaseAuthentication , SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token


class RegisterApiView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



class LoginApiView(APIView):
    def post(self, request):
        print("DATA:", request.data)

        username = request.data.get('username')
        password = request.data.get('password')

        print("USERNAME:", username)
        print("PASSWORD:", password)

        user = authenticate(username=username, password=password)

        print("AUTH USER:", user)

        if not user:
            return Response({"message":"User not found"}, status=status.HTTP_404_NOT_FOUND)

        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "username": user.username})





class LogoutAPiView(APIView):
    def post(self,request):
        username = request.data.get('username')

        logout(request)
        return Response('User loged out',status=status.HTTP_200_OK)


class AccountInfoApiView(APIView):
    ...


