from django.urls import path , include
from .views import GameTrickViewSet , PlatformTrickViewSet
from rest_framework.routers import DefaultRouter 




gametrick_router = DefaultRouter()
gametrick_router.register('games',GameTrickViewSet,basename='game-tricks')

platformtrick_router = DefaultRouter()
platformtrick_router.register('platforms',PlatformTrickViewSet,basename='platform-tricks')

urlpatterns = [
    path('',include(gametrick_router.urls)),
    path('',include(platformtrick_router.urls))
      
]   