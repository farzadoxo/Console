from django import forms


class UserRegisterForm(forms.Form):
    firstname = forms.CharField(label="🤠 Firstname:")
    lastname = forms.CharField(label="😎 Lastname:")
    username = forms.CharField(label="🆔 Username:")
    email = forms.EmailField(label="📧 Email:")
    password = forms.CharField(label="🔒 Password:")



class UserLoginForm(forms.Form):
    username = forms.CharField(label="🆔 Username:")
    password = forms.CharField(label="🔒 Password:")