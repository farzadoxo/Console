from rest_framework.serializers import ModelSerializer
from .models import GameThemeSong


class GameThemeSongSerializer(ModelSerializer):
    class Meta:
        model = GameThemeSong
        fields= '__all__'