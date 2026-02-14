from rest_framework.routers import DefaultRouter
from .views import GameWallpaperViewset , PlatformWallpaperViewset
from django.urls import path , include



gw_router = DefaultRouter()
pw_router = DefaultRouter()

gw_router.register('games',GameWallpaperViewset,basename='game-wallpapers')
pw_router.register('platforms',PlatformWallpaperViewset,basename='platform-wallpapers')

urlpatterns = [
    path('',include(gw_router.urls)),
    path('',include(pw_router.urls))
]


