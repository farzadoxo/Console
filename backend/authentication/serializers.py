from rest_framework import serializers 
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'




class JsonSerializer:
    def fail_serializer(message:str):
        return {'success':False,
                'message':message}