from django import forms
from .extentions import game_choise_field
from .models import Trick

class NewTrickForm(forms.Form):
    title = forms.CharField(label="✍🏻 Title :")
    description = forms.CharField(label="📝 Description :",widget=forms.Textarea({'rows':10 , 'cols':60}))
    game = forms.ChoiceField(choices=game_choise_field(),label="🎮 Game :")



class UpdateTrickForm(forms.Form):
    # class Meta:
    #     model = Trick
    #     fields : 
    title = forms.CharField(label="✍🏻 Title :")
    description = forms.CharField(label="📝 Description :",widget=forms.Textarea({'rows':10 , 'cols':60}))
    game = forms.ChoiceField(choices=game_choise_field(),label="🎮 Game :")