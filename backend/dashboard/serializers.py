from rest_framework.serializers import ModelSerializer
from .models import FavoritGame , SavedTrick
from django.contrib.auth.models import User


class FavoritGameSerializer(ModelSerializer):
    class Meta:
        model = FavoritGame
        fields = '__all__'



class SavedTrickSerializer(ModelSerializer):
    class Meta:
        model = SavedTrick
        fields = '__all__'


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['last_name','first_name']
        