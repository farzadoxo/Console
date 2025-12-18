from rest_framework.serializers import ModelSerializer , ValidationError
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
        read_only_fields =('user',)

        def validate_exist(self,value):
            if SavedTrick.objects.filter(trick__id=value).exists():
                raise ValidationError("This trick saved before!")
            return value


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['last_name','first_name']
        