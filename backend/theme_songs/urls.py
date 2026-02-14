from rest_framework.routers import DefaultRouter
from .views import GameThemeSongViewset
from django.urls import path,include

gts_router = DefaultRouter()
gts_router.register('games',GameThemeSongViewset,basename='game-themesong')


urlpatterns = [
    path('',include(gts_router.urls))
]