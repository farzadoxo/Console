from django.urls import path

from .views import RegisterApiView


urlpatterns = [
        path('auth/register/', RegisterApiView.as_view() , name='register'),
        # path('login/',Auth.login , name='login'),
        # path('logout/',Auth.logout , name='logout')
]
