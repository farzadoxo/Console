from django.shortcuts import render
from .models import Platform 
from django.shortcuts import render , redirect
from django.core.exceptions import ObjectDoesNotExist
from core.messages import MessageMaker as Message 
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import PlatformSerializer


class PlatformViewSet(ReadOnlyModelViewSet):
    serializer_class = PlatformSerializer
    queryset = Platform.objects.all()

