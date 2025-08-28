from .views import Dash
from django.urls import path
urlpatterns = [
    path('profile/<int:user_id>/', Dash.my_profile , name='my_profile'),
    path('add_favorite_game/<int:game_id>/' , Dash.add_favorit_games , name="add_favorite_game"),
    path('my_favorite_games/', Dash.get_user_favorit_games, name='my_favorite_games'),
]