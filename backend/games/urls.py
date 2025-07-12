from django.urls import path
from .views import Games


urlpatterns = [
    path('all/',Games.get_all_games , name='get_all_games'),
    path('info/?game_id=<int:game_id>' , Games.game_info , name='game_info')
]