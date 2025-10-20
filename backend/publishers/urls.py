from django.urls import path
from .views import Publishers



urlpatterns = [
    path('all/',Publishers,name="get_all_publishers"),
]