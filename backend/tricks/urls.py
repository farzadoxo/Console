from django.urls import path , include
from .views import GameTrickViewSet
from rest_framework.routers import DefaultRouter 




gametrick_router = DefaultRouter()
gametrick_router.register('tricks',GameTrickViewSet,basename='tricks')


urlpatterns = [
    path('',include(gametrick_router.urls))
    
]