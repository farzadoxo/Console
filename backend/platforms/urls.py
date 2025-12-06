from django.urls import path,include
from .views import PlatformViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('platforms',PlatformViewSet,basename='platforms')

urlpatterns = [
    path('',include(router.urls))

]