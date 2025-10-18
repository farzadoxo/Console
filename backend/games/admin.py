from django.contrib import admin
from .models import Game , ESRB , Genre


admin.site.register(Game)
admin.site.register(ESRB)
admin.site.register(Genre)