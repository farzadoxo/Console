from django.urls import path
from .views import Home


urlpatterns = [
    path('',Home.home , name='home')
]