from rest_framework.serializers import ModelSerializer , ReadOnlyField
from .models import GameTrick , PlatformTrick



class GameTrickSerializer(ModelSerializer):
    creator = ReadOnlyField(source='creator.id')
    
    class Meta:
        model = GameTrick
        fields = '__all__'

    

class PlatformTrickSerializer(ModelSerializer):
    creator = ReadOnlyField(source='creator.id')

    class Meta:
        model = PlatformTrick
        fields = '__all__'