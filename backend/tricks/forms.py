from django import forms
from .models import Trick



class NewTrickForm(forms.Form):
    title = forms.CharField(label="✍🏻 Title :")
    description = forms.CharField(label="📝 Description :",widget=forms.Textarea({'rows':10 , 'cols':60}))



class UpdateTrickForm(forms.Form):
    # class Meta:
    #     model = Trick
    #     fields : 
    title = forms.CharField(label="✍🏻 Title :")
    description = forms.CharField(label="📝 Description :",widget=forms.Textarea({'rows':10 , 'cols':60}))