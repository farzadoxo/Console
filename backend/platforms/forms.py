from django import forms


class NewPlatformTrickForm(forms.Form):
    title = forms.CharField(label="✍🏻 Title :")
    description = forms.CharField(label="📝 Description :",widget=forms.Textarea({'rows':10 , 'cols':60}))