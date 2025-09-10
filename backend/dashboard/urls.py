from .views import Dash
from django.urls import path
urlpatterns = [
    path('profile/', Dash.my_profile , name='my_profile'),
    path('add_favorite_game/<int:game_id>/' , Dash.add_favorit_games , name="add_favorite_game"),
    path('add_saved_trick/<int:trick_id>/' , Dash.add_saved_tricks , name="add_saved_trick"),
    path('my_favorite_games/', Dash.get_user_favorit_games, name='my_favorite_games'),
    path('my_saved_tricks/', Dash.get_user_saved_tricks, name='my_saved_tricks'),
    path('account/delete/',Dash.delete_account , name='delete_account'),
    path('delete_favorite_game/<int:game_id>/',Dash.delete_favorite_game , name='delete_favorite_game'),

]