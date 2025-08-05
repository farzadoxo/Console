from .views import Dash
from django.urls import path
urlpatterns = [
    path('profile/', Dash.my_profile , name='my_profile')
]