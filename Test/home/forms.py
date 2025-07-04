from django import forms
from .models import User


class CreateUserForm(forms.Form):
    FullName = forms.CharField()
    Email = forms.EmailField()


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =  "__all__"