from rest_framework import serializers 
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required':True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', None),
            password=validated_data['password']
        )
        return user
    

    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already used")
        return value
    
    def validate_password(srlf,value:str):
        if len(value) < 8:
            raise serializers.ValidationError('Password must be over 8 character')
        return value
