from django.urls import path
from .views import Games


urlpatterns = [
    path('all/',Games.get_all_games , name='get_all_games')
]