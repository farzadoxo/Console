from rest_framework.serializers import ModelSerializer
from .models import FavoritGame , SavedGameTrick
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

class FavoritGameSerializer(ModelSerializer):
    class Meta:
        model = FavoritGame
        fields = '__all__'
        read_only_fields= ('user',)


    def validate(self,attrs):
        request = self.context['request']
        user = request.user
        game = attrs.get('game')

        if FavoritGame.objects.filter(game=game,user=user).exists():
            raise ValidationError({"This game is on your favorite games before!"})
        
        return attrs



class SavedGameTrickSerializer(ModelSerializer):
    class Meta:
        model = SavedGameTrick
        fields = '__all__'
        read_only_fields = ('user',)

    def validate(self, attrs):
        request = self.context['request']
        user = request.user
        trick = attrs.get('trick')

        if SavedGameTrick.objects.filter(user=user, trick=trick).exists():
            raise ValidationError({
                "trick": "This trick saved before!"
            })

        return attrs



class ProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['last_name','first_name']