from django.contrib import admin
from .models import Game , Publisher , Platform , ESRB , Genre


admin.site.register(Game)
admin.site.register(Publisher)
admin.site.register(Platform)
admin.site.register(ESRB)
admin.site.register(Genre)