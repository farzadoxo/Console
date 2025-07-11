from django.urls import path
from .views import Auth


urlpatterns = [
        path('register/', Auth.register , name='register'),
        path('login/',Auth.login , name='login'),
        path('logout/',Auth.logout , name='logout')
]
