from django import forms
from games.models import Game
from .extentions import game_choise_field


class NewTrickForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    game = forms.ChoiceField(choices=game_choise_field())