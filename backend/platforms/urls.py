from django.urls import path
from .views import Platforms


urlpatterns = [
    path('all/',Platforms.get_all_platforms,name="get_all_platforms"),

]