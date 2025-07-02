from django import forms

class CreateUserForm(forms.Form):
    FullName = forms.CharField()
    Email = forms.EmailField()


class UpdateUserForm(forms.Form):
    FullName = forms.CharField()
    Email = forms.EmailField()