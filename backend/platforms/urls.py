from django.urls import path
from .views import Platforms


urlpatterns = [
    path('all/',Platforms.get_all_platforms,name="all"),
    path('<int:platform_id>/',Platforms.show_platform,name='show_platform')

]