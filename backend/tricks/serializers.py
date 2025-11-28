from rest_framework.serializers import ModelSerializer , ReadOnlyField
from .models import Trick



class TrickSerializer(ModelSerializer):
    creator = ReadOnlyField(source='creator.id')
    
    class Meta:
        model = Trick
        fields = '__all__'

        