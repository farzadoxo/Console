from django.urls import path, include
from .views import FavoritGameViewSet , SavedGameTrickViewSet , SavedPlatformTrickViewSet , UpdateProfileInfo
from rest_framework.routers import DefaultRouter

saved_game_tricks_router = DefaultRouter()
saved_game_tricks_router.register('saved-game-tricks',SavedGameTrickViewSet,basename='saved_game_trick')

saved_platform_tricks_router = DefaultRouter()
saved_platform_tricks_router.register('saved-platform-tricks',SavedPlatformTrickViewSet,basename='saved_platform_trick')

favorit_games_router = DefaultRouter()
favorit_games_router.register('favorit-games',FavoritGameViewSet,basename='favorit-games')




urlpatterns = [
    path('update-profile/',UpdateProfileInfo.as_view()),
    path('',include(saved_game_tricks_router.urls)),
    path('',include(saved_platform_tricks_router.urls)),
    path('',include(favorit_games_router.urls)),
    

]