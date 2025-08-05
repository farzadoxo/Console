from django import forms



class UpdateUserProfile(forms.Form):
    FirstName = forms.CharField()
    LastName = forms.CharField()



class UpdateUserAccount(forms.Form):
    UserName = forms.CharField()
    Email = forms.EmailField()
    