from django.urls import path
from .views import Tricks



urlpatterns = [
    path('all/',Tricks.get_all_tricks , name='get_all_tricks')
]