from django.urls import path
from .views import Games


urlpatterns = [
    path('all/',Games.get_all_games , name='get_all_games'),
    path('info/?game_id=<int:game_id>' , Games.game_info , name='game_info'),
    path('genre/<int:genre_id>/',Games.get_games_by_genre , name='get_games_by_genre'),
    path('publisher/<int:publisher_id>/',Games.get_games_by_publisher , name='get_games_by_publisher'),
    path('esrb/<str:esrb_sign>/',Games.get_games_by_esrb , name='get_games_by_esrb'),
]