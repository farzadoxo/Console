from django.urls import path , include
from .views import GameTrickViewSet , PlatformTrickViewSet
from rest_framework.routers import DefaultRouter 




gametrick_router = DefaultRouter()
gametrick_router.register('tricks',GameTrickViewSet,basename='tricks')

platformtrick_router = DefaultRouter()
platformtrick_router.register('tricks',PlatformTrickViewSet,basename='tricks')

urlpatterns = [
    path('games/',include(gametrick_router.urls)),
    path('platforms/',include(platformtrick_router.urls))
    
]