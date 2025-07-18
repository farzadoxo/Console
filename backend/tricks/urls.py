from django.urls import path
from .views import Tricks



urlpatterns = [
    path('all/',Tricks.get_all_tricks , name='get_all_tricks'),
    path('game/<int:game_id>/',Tricks.get_tricks_by_game , name='get_tricks_by_game'),
    path('new/',Tricks.new_trick , name='new_trick')
]