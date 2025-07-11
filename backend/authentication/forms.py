from django import forms


class UserRegisterForm(forms.Form):
    FirstName = forms.CharField(label="🤠 Firstname:")
    LastName = forms.CharField(label="😎 Lastname:")
    UserName = forms.CharField(label="🆔 Username:")
    Email = forms.EmailField(label="📧 Email:")
    Password = forms.CharField(label="🔒 Password:")



class UserLoginForm(forms.Form):
    UserName = forms.CharField(label="🆔 Username:")
    Password = forms.CharField(label="🔒 Password:")