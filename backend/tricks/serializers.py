from rest_framework.serializers import ModelSerializer , ReadOnlyField
from .models import GameTrick



class GameTrickSerializer(ModelSerializer):
    creator = ReadOnlyField(source='creator.id')
    
    class Meta:
        model = GameTrick
        fields = '__all__'