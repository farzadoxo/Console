from django.urls import path

from .views import RegisterApiView , LoginApiView , LogoutAPiView

urlpatterns = [
        path('auth/register/', RegisterApiView.as_view() , name='register'),
        path('auth/login/',LoginApiView.as_view(),name='login'),
        path('auth/logout/',LogoutAPiView.as_view(),name='logout')
]