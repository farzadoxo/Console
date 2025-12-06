from django.urls import path , include
from rest_framework import routers
from .views import PublisherViewSet

router = routers.DefaultRouter()
router.register('pub',PublisherViewSet,basename='pub')


urlpatterns = [
    path('',include(router.urls))
]