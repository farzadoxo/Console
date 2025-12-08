from django.urls import path, include
from .views import FavoritGameViewSet , SavedTrickViewSet , UpdateProfileInfo
from rest_framework.routers import DefaultRouter

saved_tricks_router = DefaultRouter()
saved_tricks_router.register('saved-trick',SavedTrickViewSet,basename='saved_trick')

favorit_games_router = DefaultRouter()
favorit_games_router.register('favorit-games',FavoritGameViewSet,basename='favorit-games')




urlpatterns = [
    path('update-profile/',UpdateProfileInfo.as_view()),
    path('',include(saved_tricks_router.urls)),
    path('',include(favorit_games_router.urls)),
    

]