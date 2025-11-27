from django.urls import path,include
from .views import PlatformViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('platforms',PlatformViewSet,basename='platforms')

urlpatterns = [
    path('',include(router.urls))
    # path('all/',Platforms.get_all_platforms,name="all"),
    # path('<int:platform_id>/',Platforms.show_platform,name='show_platform')

]