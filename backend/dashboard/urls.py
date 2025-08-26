from .views import Dash
from django.urls import path
urlpatterns = [
    path('profile/<int:user_id>/', Dash.my_profile , name='my_profile'),
    path('user/favorit_games/' , Dash.get_user_favorit_games , name='get_user_favorit_games'),
    path('add_favorit_game/<int:user_id>/' , Dash.add_favorit_games , name="add_favorit_game")
]