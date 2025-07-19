from django import forms


class NewTrickForm(forms.Form):
    Title = forms.CharField()
    Descreption = forms.CharField()
    Game = forms.ChoiceField()

    # TODO : FILL GAME CHOISE WITH GAMES