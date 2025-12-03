from django.shortcuts import render , redirect
from .models import Publisher
from django.core.exceptions import ObjectDoesNotExist
from core.messages import MessageMaker as Message
from .serializers import PublisherSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet




class PublisherViewSet(ReadOnlyModelViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


