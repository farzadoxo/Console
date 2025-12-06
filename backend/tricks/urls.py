from django.urls import path , include
from .views import TrickViewSet
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register('tricks',TrickViewSet,basename='tricks')


urlpatterns = [
    path('',include(router.urls))
    
]