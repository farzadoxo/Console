from django import forms
from django.contrib.auth.models import User


class UpdateUserProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name']



class UpdateUserAccount(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']


class UpdatePassword(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password']

    
