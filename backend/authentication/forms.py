from django import forms


class UserRegisterForm(forms.Form):
    UserName = forms.CharField(label="🆔 Username:")
    Email = forms.EmailField(label="📧 Email:")
    Password = forms.CharField(label="🔒 Password:")


