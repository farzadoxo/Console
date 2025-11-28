from django.urls import path , include
from .views import TrickViewSet
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register('tricks',TrickViewSet,basename='tricks')


urlpatterns = [
    path('',include(router.urls))
    # path('<int:trick_id>/',Tricks.show_trick , name='show_trick'),
    # path('all/',Tricks.get_all_tricks , name='all'),
    # path('game/<int:game_id>/',Tricks.get_tricks_by_game , name='get_tricks_by_game'),
    # path('new/<int:game_id>/',Tricks.new_trick , name='new_trick'),
    # path('user/<int:creator_id>/',Tricks.get_tricks_by_creator , name='get_tricks_by_creator'),
    # path('delete/<int:trick_id>/',Tricks.delete_trick , name='delete_trick'),
    # path('update/<int:trick_id>/',Tricks.update_trick , name='update_trick'),
    
]