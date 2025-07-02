from django.urls import path
from . import views 
urlpatterns = [
        path('home/',views.home,name='home'),
        path('userinfo/<int:user_id>/' , views.user_info,name='userinfo'),
        path('deleteuser/<int:user_id>/' , views.delete_user , name="delete"),
        path('create/' , views.create_user , name="create"),
        path('update/<int:user_id>/',views.update_user , name='update')

]
